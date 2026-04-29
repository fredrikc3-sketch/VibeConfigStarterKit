# IRM auto-remediation reference

Companion to `SKILL.md` §6. Use when an `ENCRYPTED` / `PASSWORD_PROTECTED` finding is suspected to come from a Microsoft Purview Information Protection (MPIP, formerly AIP) sensitivity label rather than a user-set password.

## Detection signals

- Office file opens with `zipfile` but the central directory contains an `EncryptedPackage` stream **and** a `\6DataSpaces\DRMEncryptedTransform` entry.
- PDF metadata contains `/EncryptMetadata` with an `MSIPC` or `MicrosoftIRMServices` producer.
- File header bytes match the OLE compound-document magic (`D0 CF 11 E0`) and contain `\x05DRMSourceData`.

## Required rights

The running identity must have **Extract / Export** usage right on the label that is currently applied. Typical roles:

- Information Protection Admin
- Co-author / Owner of the label
- Member of a group that the label policy explicitly grants Extract to

If the identity does not have those rights, do **not** retry — the file remains a `blocker` and the user is asked to supply an unprotected copy or request a less restrictive label.

## Remediation procedure (Windows / PowerShell)

```powershell
# One-time install (per agent host; uses PSGallery)
Install-Module -Name PurviewInformationProtection -Scope CurrentUser -Force

# Authenticate. For interactive runs, simply load the module:
Import-Module PurviewInformationProtection
# For unattended (CI / scheduled) runs, use a service principal:
#   Set-Authentication -AppId <appId> -AppSecret <secret> -TenantId <tid> -DelegatedUser <upn>

# Per-file decrypt loop (run from a working copy folder, NEVER the original Requirements/ tree)
$workDir = "Requirements\_decrypted"
New-Item -ItemType Directory -Path $workDir -Force | Out-Null
Copy-Item "Requirements\<file>" -Destination $workDir

Get-FileStatus -Path "$workDir\<file>"          # confirms IsLabeled / IsRMSProtected / RMSTemplateId
Remove-FileLabel -Path "$workDir\<file>" -JustificationMessage `
    "Automated extraction for D365 F&O implementation requirements analysis"
Get-FileStatus -Path "$workDir\<file>"          # IsRMSProtected should now be False
```

## After successful decryption

1. Re-run the SKILL.md §2 extractor on the **decrypted working copy** to obtain text and embedded images.
2. Persist only the extracted text (and OCR'd image text) into `Documentation/source-document-validation.json` under `extractedTextSample` and into the per-document analysis pipeline. Do **not** commit, push, upload, or e-mail the decrypted working copy.
3. **Securely delete the decrypted working copy** as soon as extraction is complete:

   ```powershell
   try {
       # extraction code here
   }
   finally {
       Remove-Item "$workDir\<file>" -Force -ErrorAction SilentlyContinue
       # If SDelete is available, prefer it for verifiable wipe:
       #   sdelete -p 3 -nobanner "$workDir\<file>"
       Remove-Item $workDir -Recurse -Force -ErrorAction SilentlyContinue
   }
   ```

4. Record in the per-document `notes`: `"IRM-decrypted via PurviewInformationProtection on <utc-ts>; working copy purged"`. The original document's `findings[].remediation` becomes `"AUTO-REMEDIATED via Remove-FileLabel"` and the document status flips from `blocker` → `ok` (or `warning` if other findings remain).

## Failure modes & fallbacks

| Outcome | Meaning | Action |
|---|---|---|
| `Remove-FileLabel` returns `User does not have rights` | Running identity lacks Extract usage right on that label | Do **not** retry. Surface as blocker; request file from a user with rights, or ask the data owner to apply a less restrictive label. |
| `Get-FileStatus` reports `IsRMSProtected: False` but extractor still fails | Encryption is not IRM (likely user-set password) | Fall back to standard `ENCRYPTED` remediation — request password / unprotected copy. |
| Module not installable on host (offline / restricted PSGallery) | Toolchain unavailable | Record `result: skipped`; surface as blocker with remediation `"Run source-document-validator on a host with PurviewInformationProtection installed, or supply unprotected copies."` |
| Decrypted copy still classified as `SCANNED_IMAGE_PDF` / `OCR_REQUIRED` | Decryption succeeded but content needs OCR | Apply OCR remediation in addition. |

## Mandatory rules

- **Never** decrypt files in place — always operate on a copy under `Requirements/_decrypted/` (or the project-id-namespaced equivalent).
- **Never** commit, push, upload, or e-mail the decrypted working copy. Only the extracted text/images ever leave the host.
- **Always** purge the working copy after extraction, even on failure (`try / finally`).
- **Always** add a Challenge Journal entry tagged `irm-auto-remediation` with the label name and outcome — this lets the reinforcement-learning loop track which customers consistently send IRM-protected files so the project plan can request a label exemption up front.
- **Respect the gate**: if rights are insufficient or the module is unavailable, the document remains `blocker` and the user is asked to supply an unprotected copy.

## References

- [PurviewInformationProtection PowerShell module](https://learn.microsoft.com/powershell/module/purviewinformationprotection/?view=azureipps)
- `Remove-FileLabel`, `Get-FileStatus`, `Set-Authentication` cmdlets
