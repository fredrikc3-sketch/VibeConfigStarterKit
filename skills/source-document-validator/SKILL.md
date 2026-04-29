---
name: source-document-validator
description: Use as a HARD GATE at the start of Phase 1.1 (and any time new files arrive in `Requirements/`) to validate that every source document can actually be read and that the extracted content is sufficient. Detects encrypted/password-protected files, corrupt files, scanned-image PDFs that need OCR, empty or suspiciously short extractions, unsupported formats, and macro-enabled Office files. Produces `Documentation/source-document-validation.json` (machine-readable) and `Documentation/source-document-validation.md` (human-readable). If ANY document is classified as `blocker`, Phase 1.1 (`d365-requirements-analysis`) MUST NOT proceed — surface the blocker list to the user and request unencrypted/readable replacements before continuing.
---

# Source Document Validator (Phase 1.0 — pre-flight)

> **Cardinal rule**: Garbage in → garbage out. If we cannot fully read a requirement document, we cannot trust the requirement matrix that follows. This is a hard gate — never silently proceed with incomplete extraction.

## When to invoke

- **Always** at the very start of Phase 1.1, before `d365-requirements-analysis` reads any document.
- Whenever new files are dropped into `Requirements/` mid-project.
- On user request ("validate sources", "check the requirement docs", "did all the docs load?").

## Inputs

- Every file under `Requirements/` (recursively).
- Optional: `<projectId>/Requirements/` if project-id namespacing is active (see `d365-knowledge-routing` §5).

## Outputs

| Artefact | Location | Purpose |
|---|---|---|
| Validation report (machine) | `Documentation/source-document-validation.json` | Schema: `schemas/source-document-validation.schema.json` |
| Validation report (human)  | `Documentation/source-document-validation.md`   | Summary + blocker list + remediation guidance |

If `summary.gateStatus == "blocked"`, also write a banner to `Documentation/_status/1.0/gate-status.md` so the orchestrator detects the block during phase transition.

---

## Per-document procedure

For each file:

### 1. Identify
- Compute `sha256`, `size`, MIME/extension → `format` enum.
- If extension is unrecognised → finding `UNSUPPORTED_FORMAT` (severity warning unless this is the only doc, then blocker).

### 2. Read & extract
Attempt extraction by format. Capture the **first 1 KB of extracted text** as `extractedTextSample` for traceability.

| Format | Extraction approach | Encrypted-detection signal |
|---|---|---|
| pdf  | `pypdf` / `pdfplumber` text extraction | `pypdf.PdfReader.is_encrypted` true OR opening raises `PyCryptodomeNotInstalledError` / "File has not been decrypted" → `ENCRYPTED` (blocker). If extraction succeeds but text length < 50 chars while file size > 100 KB → `SCANNED_IMAGE_PDF` / `OCR_REQUIRED` (blocker). |
| docx | `python-docx` or unzip + parse `word/document.xml` | If the zip central directory contains `EncryptedPackage` stream, or `zipfile.BadZipFile` is raised on a valid `.docx` extension → `PASSWORD_PROTECTED` (blocker). |
| doc  | `antiword` / `textract` / pandoc fallback | If extraction yields binary noise → `BINARY_NOT_TEXT` + recommend conversion to `.docx`. |
| xlsx | `openpyxl` (`load_workbook`) | `zipfile.BadZipFile` or `InvalidFileException` with header `"Encrypted"` → `PASSWORD_PROTECTED` (blocker). |
| xls  | `xlrd` (≤ 2.0) or pandas | If only structural bytes extracted → `BINARY_NOT_TEXT`. |
| pptx | `python-pptx` | Same encryption check as docx. |
| txt / md / csv | direct read with `chardet` for encoding | Unknown encoding → `UNKNOWN_ENCODING` (warning). |
| rtf  | `striprtf` or pandoc | — |
| html | strip tags, keep text | — |
| image | OCR (Tesseract) if available | If no OCR → `OCR_REQUIRED` (blocker). |
| other | best-effort text read; if not UTF-8/ASCII viable → `UNSUPPORTED_FORMAT` |

> **Tooling note**: extraction is best-effort. If the runtime cannot perform an extraction (e.g. no pypdf installed), the agent narrates the planned step, attempts a fallback (e.g. raw byte read + heuristic), and records `result: skipped` with `detail` describing what's needed. Skipped extractability is itself a `blocker` finding (`OTHER`, severity blocker, message "extraction toolchain unavailable") unless the user explicitly waives it.

### 3. Run check matrix

For every document, populate `checks`:

| Check | Pass criteria | Fail / warn semantics |
|---|---|---|
| `readable`    | OS opened the file without error | `READ_ERROR` (blocker) |
| `extractable` | Format-specific extractor returned text | `ENCRYPTED` / `PASSWORD_PROTECTED` / `OCR_REQUIRED` (all blockers) |
| `complete`    | Extracted text ≥ 200 chars AND ≥ 0.5 % of file size for binary-bearing formats | `EMPTY` (blocker), `SUSPICIOUSLY_SHORT` (warning unless file is >200 KB then blocker), `TRUNCATED` (warning) |
| `integrity`   | File parsed without structural errors | `CORRUPT` (blocker) |
| `sensitivity` | No obvious secrets/PII (informational scan: AKS / Azure conn-strings, SSN-like patterns, JWT tokens, base64 PEM) | `PII_DETECTED` / `SECRET_DETECTED` (warning — never blocker; surfaces a remediation tip but does not stop the pipeline). |

### 4. Classify document status
- `blocker` if any finding has severity `blocker`.
- `warning` if no blockers but ≥ 1 finding with severity `warning`.
- `ok` otherwise.

### 5. Suggest remediation
For each blocker, populate `remediation`:

| Finding | Remediation message |
|---|---|
| `ENCRYPTED`, `PASSWORD_PROTECTED` | "Re-supply the file without password protection, or share the password through a secure channel. **If the file is IRM/sensitivity-label protected (most common cause for corporate Office docs), see §6 — auto-remediation via `PurviewInformationProtection`** before falling back to user re-supply." |
| `SCANNED_IMAGE_PDF` / `OCR_REQUIRED` | "Re-supply a text-bearing PDF, or run OCR (Adobe / Tesseract) before re-uploading." |
| `CORRUPT` | "File appears truncated or damaged — re-export from the source application." |
| `EMPTY` | "File contains no extractable text — confirm it's the right document." |
| `BINARY_NOT_TEXT` | "Convert legacy `.doc` / `.xls` to `.docx` / `.xlsx` and re-upload." |
| `UNSUPPORTED_FORMAT` | "Convert to PDF, DOCX, XLSX, MD, TXT, or CSV." |
| `MACRO_ENABLED` | "Strip macros before review, or convert to a non-macro format (`.docx` / `.xlsx`)." |

### 6. Suggested auto-remediation for IRM-protected files

In enterprise environments the **most likely cause** of an `ENCRYPTED` / `PASSWORD_PROTECTED` finding on Office files (`.docx`, `.xlsx`, `.pptx`, `.pdf`) is **Microsoft Purview Information Protection (MPIP / formerly AIP) sensitivity labels with encryption**, not a user-set password. Before asking the user to re-supply, attempt this remediation **provided the running identity has Extract / Export usage rights on the label** (Information Protection Admins, label owners, or co-authors).

High-level flow:

1. **Detect** IRM signals (EncryptedPackage stream, MSIPC PDF producer, OLE `\x05DRMSourceData`).
2. **Copy** the file to a working folder (`Requirements/_decrypted/`) — never decrypt in place.
3. **Decrypt** with `Remove-FileLabel` from the `PurviewInformationProtection` PowerShell module (auth via `Set-Authentication` for unattended runs).
4. **Re-run** the §2 extractor against the decrypted working copy to capture text and images.
5. **Purge** the decrypted working copy in a `try / finally` block (prefer `sdelete` if available).
6. **Record** outcome in the per-document `notes` and Challenge Journal (tag `irm-auto-remediation`); flip the original document's status from `blocker` → `ok` if no other findings remain.

If rights are insufficient, the module is unavailable, or the file is not actually IRM-protected, fall back to the standard `ENCRYPTED` remediation (request unprotected copy from the user).

> **Full procedure, cmdlet syntax, failure modes, and mandatory safety rules**: see `irm-remediation.md` in this skill folder.

---

## Gate logic

```
if summary.blockers > 0:
    summary.gateStatus = "blocked"
    write Documentation/_status/1.0/gate-status.md with the blocker list
    surface ALL blocking documents to the user with their remediation messages
    stop — do NOT invoke d365-requirements-analysis
else:
    summary.gateStatus = "open"
    write the markdown report
    proceed to Phase 1.1 (d365-requirements-analysis)
```

The gate is **hard**. The user can override only by explicitly waiving specific blockers, in which case the waived findings are still recorded and the report annotates `remediation` with `"WAIVED BY USER on <date>"`.

## Markdown report skeleton

`Documentation/source-document-validation.md`:

```markdown
# Source Document Validation — <date>

**Gate status**: 🚫 BLOCKED (3 blockers across 18 documents) | ✅ OPEN

## Blockers (must resolve before Phase 1.1)
| Document | Finding | Remediation |
|---|---|---|
| Requirements/SOW.pdf | ENCRYPTED | Re-supply without password |
| Requirements/legacy-process.doc | BINARY_NOT_TEXT | Convert to .docx |
| Requirements/scanned-form.pdf | SCANNED_IMAGE_PDF | Run OCR before upload |

## Warnings (informational)
| Document | Finding | Notes |
|---|---|---|
| Requirements/spec.docx | PII_DETECTED | One SSN-like pattern; redact before publishing |

## Passed (15)
- Requirements/business-rules.md
- Requirements/process-list.xlsx
- …

## Next step
Resolve the 3 blockers above and re-run `source-document-validator`.
```

## Rules
- **Never** allow Phase 1.1 to start if `gateStatus == "blocked"`.
- **Never** silently truncate or guess content — always record what was actually extracted.
- **Always** log each blocker as a Challenge Journal entry (category `"requirements-ingestion"`, severity matching the finding) so recurring patterns are caught (e.g., a customer who repeatedly sends scanned PDFs).
- **Always** record `sha256` so re-uploads can be detected and re-validated automatically.
- **Project-id namespacing** applies — write outputs under `<projectId>/Documentation/` when active.

## Cross-references
- Schema: `schemas/source-document-validation.schema.json`
- IRM auto-remediation reference: `skills/source-document-validator/irm-remediation.md`
- Phase 1.1 entry point: `skills/d365-requirements-analysis/SKILL.md`
- Reinforcement-learning hooks: `skills/reinforcement-learning/SKILL.md`
