import json

# Build visualization data from the flat catalogue
with open('ProcessCatalogue_flat.json', 'r', encoding='utf-8') as f:
    flat_data = json.load(f)

processes = flat_data['processes']
children_of = {}
for p in processes:
    pid = p.get('parentId')
    if pid is not None:
        children_of.setdefault(pid, []).append(p)

viz_data = []
for p in processes:
    if p.get('type') != 'End to end':
        continue
    e2e = {
        'id': p['id'],
        'title': p['title'],
        'seq': p.get('sequenceId', ''),
        'desc': (p.get('description', '') or '')[:200],
        'ref': p.get('microsoftReference', ''),
        'areas': []
    }
    for area in sorted(children_of.get(p['id'], []), key=lambda x: x.get('sequenceId', '')):
        if area.get('type') != 'Process area':
            continue
        a = {
            'id': area['id'],
            'title': area['title'],
            'seq': area.get('sequenceId', ''),
            'desc': (area.get('description', '') or '')[:200],
            'processes': []
        }
        for proc in sorted(children_of.get(area['id'], []), key=lambda x: x.get('sequenceId', '')):
            if proc.get('type') != 'Process':
                continue
            scenarios = [s for s in children_of.get(proc['id'], []) if s.get('type') in ('Scenario', 'System process')]
            a['processes'].append({
                'id': proc['id'],
                'title': proc['title'],
                'seq': proc.get('sequenceId', ''),
                'desc': (proc.get('description', '') or '')[:200],
                'scenarios': len(scenarios)
            })
        e2e['areas'].append(a)
    viz_data.append(e2e)

viz_json = json.dumps(viz_data, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
<title>Process Map</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

  :root {{
    --bg: #0b1118;
    --bg-2: #0f1724;
    --card: #131b2b;
    --muted: #7a8aa0;
    --text: #d7dde6;
    --accent: #86a8d6;
    --accent-2: #9bbf9a;
    --accent-3: #b39bc8;
    --line: #2a3548;
    --glow: rgba(134, 168, 214, 0.18);
  }}

  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: 'Manrope', sans-serif;
    background: radial-gradient(1000px 600px at 70% -10%, #1a2638 0%, var(--bg) 55%), var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow: hidden;
  }}

  .ambient {{
    position: absolute;
    inset: -20% -10% auto -10%;
    height: 60vh;
    background: radial-gradient(350px 220px at 15% 40%, rgba(134,168,214,0.12), transparent 60%),
                radial-gradient(420px 240px at 85% 20%, rgba(155,191,154,0.12), transparent 60%);
    filter: blur(10px);
    animation: drift 18s ease-in-out infinite;
    pointer-events: none;
  }}

  @keyframes drift {{
    0% {{ transform: translateY(0) translateX(0); }}
    50% {{ transform: translateY(8px) translateX(-12px); }}
    100% {{ transform: translateY(0) translateX(0); }}
  }}

  header {{
    position: relative;
    z-index: 2;
    padding: 28px 36px 10px;
  }}

  h1 {{
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin: 0 0 8px;
  }}

  .subtle {{
    color: var(--muted);
    font-size: 13px;
  }}

  .toolbar {{
    display: flex;
    gap: 10px;
    align-items: center;
    margin-top: 14px;
    flex-wrap: wrap;
  }}

  .btn {{
    background: linear-gradient(180deg, #162033, #111a2a);
    border: 1px solid #28354b;
    color: var(--text);
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
  }}

  .btn:hover {{
    border-color: #3c4c69;
    box-shadow: 0 0 0 3px var(--glow);
  }}

  .crumbs {{
    margin-left: auto;
    font-size: 12px;
    color: var(--muted);
  }}

  .crumbs span {{
    color: var(--text);
    font-weight: 600;
  }}

  .stage {{
    position: relative;
    z-index: 2;
    height: calc(100vh - 140px);
    padding: 8px 20px 24px;
  }}

  .canvas-wrap {{
    background: linear-gradient(180deg, var(--bg-2), #0b131f 70%);
    border: 1px solid #1f2a3f;
    border-radius: 14px;
    height: 100%;
    overflow: auto;
    box-shadow: 0 20px 60px rgba(0,0,0,0.45);
  }}

  #map-svg {{
    width: 1300px;
    height: 700px;
    display: block;
  }}

  .map-label {{
    font-size: 11px;
    fill: var(--muted);
    font-weight: 700;
    letter-spacing: 0.08em;
  }}

  .map-edge {{
    fill: none;
    stroke: #6f83a633;
    stroke-width: 2;
  }}

  .map-edge.strong {{
    stroke: #9bb0d744;
    stroke-width: 2.5;
  }}

  .map-node {{
    cursor: pointer;
  }}

  .map-node rect {{
    fill: #111a2a;
    stroke: #2e3d56;
    stroke-width: 1;
    rx: 10;
    ry: 10;
    transition: all 0.2s ease;
  }}

  .map-node text {{
    fill: var(--text);
    font-size: 12px;
  }}

  .map-node.active rect {{
    stroke: var(--accent);
    fill: #16243b;
    filter: drop-shadow(0 6px 10px rgba(134,168,214,0.18));
  }}

  .map-node.dim rect {{
    stroke: #1f2a3f;
    fill: #0f1724;
  }}

  .tip {{
    position: fixed;
    background: #141f31;
    border: 1px solid #2b3b55;
    padding: 10px 12px;
    border-radius: 8px;
    font-size: 12px;
    color: var(--text);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.12s ease;
    max-width: 340px;
    z-index: 5;
  }}

  .tip.visible {{ opacity: 1; }}
  .tip .seq {{ color: var(--muted); font-family: 'JetBrains Mono', monospace; font-size: 11px; }}
  .tip .title {{ font-weight: 700; margin: 2px 0 4px; }}
</style>
</head>
<body>
<div class=\"ambient\"></div>
<header>
  <h1>Integrated Business Planning Map</h1>
  <div class=\"subtle\">Drillable map of end-to-end processes, areas, and processes</div>
  <div class=\"toolbar\">
    <button class=\"btn\" onclick=\"mapReset()\">Reset</button>
    <button class=\"btn\" onclick=\"mapFit()\">Fit</button>
    <div class=\"crumbs\">Focus: <span id=\"bc-e2e\"></span> / <span id=\"bc-area\"></span></div>
  </div>
</header>
<div class=\"stage\">
  <div class=\"canvas-wrap\">
    <svg id=\"map-svg\" viewBox=\"0 0 1300 700\" preserveAspectRatio=\"xMinYMin meet\"></svg>
  </div>
</div>
<div class=\"tip\" id=\"tip\">
  <div class=\"seq\" id=\"tip-seq\"></div>
  <div class=\"title\" id=\"tip-title\"></div>
  <div id=\"tip-desc\"></div>
</div>

<script>
const DATA = {viz_json};

const COLORS = [
  '#86a8d6','#9bbf9a','#b39bc8','#b9a47a','#8fb0aa',
  '#a49bb3','#9ea9c8','#87a1c1','#a2b788','#b1a58b',
  '#8aa1c7','#9f9bc8','#b3a19b','#8fb3a2','#9fa0b8'
];

const mapState = {{
  selectedE2E: 0,
  selectedAreaId: null,
  width: 1300,
  height: 700
}};

function initMap() {{
  if (!DATA.length) return;
  mapState.selectedE2E = 0;
  mapState.selectedAreaId = DATA[0].areas[0] ? DATA[0].areas[0].id : null;
  renderMap();
  window.addEventListener('resize', () => renderMap());
}}

function mapReset() {{
  mapState.selectedE2E = 0;
  mapState.selectedAreaId = DATA[0].areas[0] ? DATA[0].areas[0].id : null;
  renderMap();
}}

function mapFit() {{
  const svg = document.getElementById('map-svg');
  svg.setAttribute('viewBox', `0 0 ${{mapState.width}} ${{mapState.height}}`);
}}

function renderMap() {{
  const svg = document.getElementById('map-svg');
  if (!svg || !DATA.length) return;
  while (svg.firstChild) svg.removeChild(svg.firstChild);

  const e2eNodes = DATA;
  const e2e = DATA[mapState.selectedE2E] || DATA[0];
  const areas = e2e.areas || [];
  const area = areas.find(a => a.id === mapState.selectedAreaId) || areas[0] || null;
  if (area) mapState.selectedAreaId = area.id;
  const processes = area ? area.processes : [];

  document.getElementById('bc-e2e').textContent = e2e ? e2e.title : 'None';
  document.getElementById('bc-area').textContent = area ? area.title : 'None';

  const colX = {{ e2e: 140, area: 560, proc: 980 }};
  const top = 70;
  const gap = 46;
  const e2eHeight = top + e2eNodes.length * gap + 60;
  const areaHeight = top + areas.length * gap + 60;
  const procHeight = top + processes.length * gap + 60;
  mapState.height = Math.max(620, e2eHeight, areaHeight, procHeight);
  mapState.width = 1300;
  svg.setAttribute('viewBox', `0 0 ${{mapState.width}} ${{mapState.height}}`);
  svg.setAttribute('height', mapState.height);

  addMapLabel(svg, colX.e2e, 30, 'END-TO-END');
  addMapLabel(svg, colX.area, 30, 'PROCESS AREAS');
  addMapLabel(svg, colX.proc, 30, 'PROCESSES');

  e2eNodes.forEach((node, i) => {{
    const y = top + i * gap;
    const active = node.id === e2e.id;
    addMapNode(svg, colX.e2e, y, node, COLORS[i % COLORS.length], 'e2e', active, !active);
  }});

  areas.forEach((node, i) => {{
    const y = top + i * gap;
    const active = area && node.id === area.id;
    addMapNode(svg, colX.area, y, node, '#8aa1c7', 'area', active, !active);
  }});

  processes.forEach((node, i) => {{
    const y = top + i * gap;
    addMapNode(svg, colX.proc, y, node, '#7fa3b5', 'proc', false, false);
  }});

  const e2eIndex = e2eNodes.findIndex(n => n.id === e2e.id);
  const e2eY = top + e2eIndex * gap;
  areas.forEach((node, i) => {{
    const y = top + i * gap;
    addMapEdge(svg, colX.e2e + 120, e2eY, colX.area - 120, y, true);
  }});

  if (area) {{
    const areaIndex = areas.findIndex(n => n.id === area.id);
    const areaY = top + areaIndex * gap;
    processes.forEach((node, i) => {{
      const y = top + i * gap;
      addMapEdge(svg, colX.area + 120, areaY, colX.proc - 120, y, false);
    }});
  }}
}}

function addMapLabel(svg, x, y, text) {{
  const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  t.setAttribute('x', x - 90);
  t.setAttribute('y', y);
  t.setAttribute('class', 'map-label');
  t.textContent = text;
  svg.appendChild(t);
}}

function addMapEdge(svg, x1, y1, x2, y2, strong) {{
  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  const c1x = x1 + 140;
  const c2x = x2 - 140;
  const d = `M ${{x1}} ${{y1}} C ${{c1x}} ${{y1}}, ${{c2x}} ${{y2}}, ${{x2}} ${{y2}}`;
  path.setAttribute('d', d);
  path.setAttribute('class', strong ? 'map-edge strong' : 'map-edge');
  svg.appendChild(path);
}}

function addMapNode(svg, x, y, node, color, kind, active, dim) {{
  const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  g.setAttribute('class', `map-node${{active ? ' active' : ''}}${{dim ? ' dim' : ''}}`);

  const label = node.title;
  const w = Math.min(250, Math.max(140, label.length * 7));
  const h = 28;
  const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  rect.setAttribute('x', x - w / 2);
  rect.setAttribute('y', y - h / 2);
  rect.setAttribute('width', w);
  rect.setAttribute('height', h);
  rect.setAttribute('rx', 10);
  rect.setAttribute('ry', 10);
  rect.setAttribute('stroke', color + '66');
  g.appendChild(rect);

  const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  text.setAttribute('x', x);
  text.setAttribute('y', y + 4);
  text.setAttribute('text-anchor', 'middle');
  text.textContent = label;
  g.appendChild(text);

  g.addEventListener('mouseenter', (e) => {{
    showTip(e, node);
  }});
  g.addEventListener('mousemove', (e) => moveTip(e));
  g.addEventListener('mouseleave', hideTip);

  g.addEventListener('click', () => {{
    if (kind === 'e2e') {{
      const idx = DATA.findIndex(n => n.id === node.id);
      mapState.selectedE2E = idx === -1 ? 0 : idx;
      const areas = DATA[mapState.selectedE2E].areas || [];
      mapState.selectedAreaId = areas[0] ? areas[0].id : null;
      renderMap();
    }} else if (kind === 'area') {{
      mapState.selectedAreaId = node.id;
      renderMap();
    }}
  }});

  svg.appendChild(g);
}}

const tip = document.getElementById('tip');
function showTip(e, node) {{
  document.getElementById('tip-title').textContent = node.title || '';
  document.getElementById('tip-seq').textContent = node.seq || '';
  document.getElementById('tip-desc').textContent = node.desc || '';
  tip.classList.add('visible');
  moveTip(e);
}}
function moveTip(e) {{
  let x = e.clientX + 14, y = e.clientY + 12;
  if (x + 360 > window.innerWidth) x = e.clientX - 360;
  if (y + 140 > window.innerHeight) y = e.clientY - 140;
  tip.style.left = x + 'px';
  tip.style.top = y + 'px';
}}
function hideTip() {{
  tip.classList.remove('visible');
}}

initMap();
</script>
</body>
</html>
"""

output_path = '../ProcessCatalogue_MapOnly.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated HTML file: {output_path}")
