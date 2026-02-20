#!/usr/bin/env python3
"""
Build an interactive D3.js mind-map HTML from ProcessCatalogue.json.
Output: ../ProcessCatalogue_MindMap.html
"""

import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOGUE = os.path.join(SCRIPT_DIR, 'ProcessCatalogue.json')
OUTPUT    = os.path.join(SCRIPT_DIR, '..', 'ProcessCatalogue_MindMap.html')

# ── Load & transform ────────────────────────────────────────────────
with open(CATALOGUE, 'r', encoding='utf-8') as f:
    raw = json.load(f)

VALID_TYPES = {'End to end', 'Process area', 'Process', 'Scenario', 'System process'}

def trim(s, maxlen=300):
    s = (s or '').strip()
    return s[:maxlen] + '...' if len(s) > maxlen else s

def build_tree(node):
    ntype = node.get('type', '')
    if ntype not in VALID_TYPES and ntype != 'Tree':
        return None
    out = {
        'name': node.get('title', ''),
        'type': ntype,
        'seq':  node.get('sequenceId', ''),
        'desc': trim(node.get('description', '')),
        'ref':  node.get('microsoftReference', '') or '',
        'apqc': node.get('apqcDescription', '') or '',
    }
    kids = node.get('children', [])
    child_nodes = []
    for c in kids:
        ct = build_tree(c)
        if ct:
            child_nodes.append(ct)
    if child_nodes:
        out['children'] = child_nodes
    return out

root_node = raw['processTree'][0]
tree = build_tree(root_node)

# Prune Scenario/System process from tree, keep counts
def prune_to_process(node):
    kids = node.get('children', [])
    if not kids:
        return
    kept = []
    scenario_count = 0
    for c in kids:
        if c['type'] in ('Scenario', 'System process'):
            scenario_count += 1
        else:
            prune_to_process(c)
            kept.append(c)
    if scenario_count > 0:
        node['leafCount'] = scenario_count
    if kept:
        node['children'] = kept
    else:
        node.pop('children', None)

prune_to_process(tree)

tree_json = json.dumps(tree, ensure_ascii=False, separators=(',', ':'))

# Count stats
def count_types(node, counts=None):
    if counts is None:
        counts = {}
    t = node.get('type', '')
    counts[t] = counts.get(t, 0) + 1
    for c in node.get('children', []):
        count_types(c, counts)
    return counts

stats = count_types(tree)
n_e2e  = stats.get('End to end', 0)
n_area = stats.get('Process area', 0)
n_proc = stats.get('Process', 0)

# ── HTML ────────────────────────────────────────────────────────────
HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>D365 Process Catalogue - Interactive Mind Map</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {
    --bg:       #0b0f14;
    --bg2:      #111820;
    --surface:  #161e2a;
    --text:     #c8d0dc;
    --muted:    #6b7a90;
    --bright:   #eef2f7;
    --link:     #2d3a50;
    --e2e:      #7a93b6;
    --area:     #6f9b8e;
    --proc:     #b39bc8;
    --accent:   #5f90c8;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg);
    color: var(--text);
    overflow: hidden;
    height: 100vh; width: 100vw;
  }

  body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background:
      radial-gradient(1100px 700px at 8% -8%, rgba(122,147,182,.10), transparent 55%),
      radial-gradient(800px 500px at 92% 8%, rgba(111,155,142,.08), transparent 55%);
  }

  .hdr {
    position: fixed; top: 0; left: 0; right: 0; z-index: 20;
    display: flex; align-items: center; gap: 16px;
    padding: 14px 24px;
    background: linear-gradient(180deg, rgba(11,15,20,.96) 60%, rgba(11,15,20,.4) 90%, transparent);
    pointer-events: none;
  }
  .hdr > * { pointer-events: auto; }
  .hdr h1 { font-size: 18px; font-weight: 700; letter-spacing: -.02em; color: var(--bright); white-space: nowrap; }
  .hdr .sub { font-size: 11px; color: var(--muted); white-space: nowrap; }

  .legend { display: flex; gap: 14px; margin-left: 20px; }
  .legend-item { display: flex; align-items: center; gap: 5px; font-size: 11px; color: var(--muted); }
  .legend-dot { width: 10px; height: 10px; border-radius: 50%; }

  .toolbar { display: flex; gap: 8px; margin-left: auto; align-items: center; }

  .btn {
    background: linear-gradient(180deg, #18243a, #111c2e);
    border: 1px solid #28374e;
    color: var(--text); padding: 5px 13px; border-radius: 8px;
    font-size: 12px; font-family: inherit; cursor: pointer; transition: .2s;
  }
  .btn:hover { border-color: #4a5e7a; box-shadow: 0 0 0 3px rgba(95,144,200,.18); }

  .search-box { position: relative; }
  .search-box input {
    background: #111920; border: 1px solid #28374e;
    color: var(--text); padding: 5px 10px 5px 28px;
    border-radius: 8px; font-size: 12px; font-family: inherit;
    width: 190px; outline: none; transition: .2s;
  }
  .search-box input:focus { border-color: var(--accent); width: 260px; }
  .search-box::before {
    content: '\\2315'; position: absolute; left: 8px; top: 4px;
    color: var(--muted); font-size: 14px; pointer-events: none;
  }

  .stats {
    position: fixed; bottom: 14px; left: 14px; z-index: 20;
    display: flex; gap: 16px;
    background: var(--surface); border: 1px solid #222e42; border-radius: 10px;
    padding: 8px 16px; font-size: 11px; color: var(--muted);
  }
  .stats span { color: var(--text); font-weight: 600; }

  .help {
    position: fixed; bottom: 14px; right: 14px; z-index: 20;
    background: var(--surface); border: 1px solid #222e42; border-radius: 10px;
    padding: 8px 14px; font-size: 11px; color: var(--muted);
  }
  .help kbd {
    background: #1a2436; border: 1px solid #28354b;
    padding: 1px 5px; border-radius: 4px; font-size: 10px;
    font-family: 'JetBrains Mono', monospace; color: var(--text);
  }

  svg { cursor: grab; position: relative; z-index: 1; }
  svg:active { cursor: grabbing; }

  .link {
    fill: none;
    stroke: var(--link);
    stroke-width: 1.2;
    stroke-opacity: .5;
  }

  .node { cursor: pointer; }
  .node circle {
    stroke-width: 2;
    transition: r .15s, filter .2s;
  }
  .node circle:hover {
    filter: drop-shadow(0 0 6px rgba(95,144,200,.4));
  }
  .node text {
    font-family: 'Inter', sans-serif;
    fill: var(--text);
    font-size: 12px;
    pointer-events: none;
  }
  .node .badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    fill: var(--muted);
  }
  .node.collapsed circle {
    stroke-dasharray: 3 2;
  }
  .node.dimmed circle { opacity: .18; }
  .node.dimmed text   { opacity: .12; }
  .node.dimmed .badge { opacity: .12; }
  .link.dimmed { stroke-opacity: .06; }
  .node.highlight circle { filter: drop-shadow(0 0 8px rgba(95,144,200,.6)); }

  .tip {
    position: fixed; z-index: 100; pointer-events: none;
    background: var(--surface); border: 1px solid #2b3b55;
    padding: 12px 16px; border-radius: 10px;
    max-width: 420px; font-size: 12px; color: var(--text);
    opacity: 0; transition: opacity .12s;
    box-shadow: 0 12px 40px rgba(0,0,0,.5);
    line-height: 1.5;
  }
  .tip.show { opacity: 1; }
  .tip .t-type { font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
  .tip .t-name { font-weight: 700; font-size: 14px; color: var(--bright); margin: 2px 0 6px; }
  .tip .t-desc { color: var(--muted); }
  .tip .t-meta { margin-top: 6px; font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #4e5e74; }
  .tip a { color: #7a93b6; text-decoration: none; }
  .tip a:hover { text-decoration: underline; }
</style>
</head>
<body>

<div class="hdr">
  <h1>D365 Process Catalogue</h1>
  <span class="sub">Interactive Mind Map</span>
  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:var(--e2e)"></div>End to end</div>
    <div class="legend-item"><div class="legend-dot" style="background:var(--area)"></div>Process area</div>
    <div class="legend-item"><div class="legend-dot" style="background:var(--proc)"></div>Process</div>
  </div>
  <div class="toolbar">
    <div class="search-box"><input id="search" placeholder="Search processes..." /></div>
    <button class="btn" id="btnDepth">Depth: 2</button>
    <button class="btn" onclick="expandAll()">Expand All</button>
    <button class="btn" onclick="collapseAll()">Collapse</button>
    <button class="btn" onclick="resetView()">Reset View</button>
  </div>
</div>

<div class="tip" id="tip">
  <div class="t-type" id="tip-type"></div>
  <div class="t-name" id="tip-name"></div>
  <div class="t-desc" id="tip-desc"></div>
  <div class="t-meta" id="tip-meta"></div>
</div>

<div class="stats">
  <div>End-to-end: <span>""" + str(n_e2e) + """</span></div>
  <div>Process areas: <span>""" + str(n_area) + """</span></div>
  <div>Processes: <span>""" + str(n_proc) + """</span></div>
</div>

<div class="help">
  <kbd>Click</kbd> expand / collapse &ensp;
  <kbd>Scroll</kbd> zoom &ensp;
  <kbd>Drag</kbd> pan &ensp;
  <kbd>Hover</kbd> details
</div>

<svg id="tree"></svg>

<script>
// ── DATA ──
const SOURCE = """ + tree_json + """;

// ── CONFIG ──
const TYPE_COLOR = {
  'Tree':           '#5a6a82',
  'End to end':     '#7a93b6',
  'Process area':   '#6f9b8e',
  'Process':        '#b39bc8',
  'Scenario':       '#8b8b8b',
  'System process': '#8b8b8b'
};
const TYPE_RADIUS = {
  'Tree': 10, 'End to end': 8, 'Process area': 6, 'Process': 4.5
};

let maxDepth = 2;
let rootData;
const ORIGINAL = JSON.parse(JSON.stringify(SOURCE));

// ── HELPERS ──
function initTree(node, depth) {
  node._depth = depth;
  if (node.children) {
    node.children.forEach(function(c) { initTree(c, depth + 1); });
    if (depth >= maxDepth) {
      node._children = node.children;
      node.children = null;
    }
  }
}

function toggle(d) {
  if (d.children) {
    d._children = d.children;
    d.children = null;
  } else if (d._children) {
    d.children = d._children;
    d._children = null;
  }
}

function expandNode(d) {
  if (d._children) {
    d.children = d._children;
    d._children = null;
  }
  if (d.children) d.children.forEach(expandNode);
}

function collapseNode(d, depth) {
  if (d.children) {
    if (depth >= 1) {
      d._children = d.children;
      d.children = null;
    } else {
      d.children.forEach(function(c) { collapseNode(c, depth + 1); });
    }
  }
  if (d._children && depth < 1) {
    d.children = d._children;
    d._children = null;
    d.children.forEach(function(c) { collapseNode(c, depth + 1); });
  }
}

function countLeavesData(n) {
  if (!n.children || !n.children.length) return 1;
  return n.children.reduce(function(s, c) { return s + countLeavesData(c); }, 0);
}

function colorOf(d) { return TYPE_COLOR[d.type] || '#5a6a82'; }
function hasKids(d) { return d.children || d._children; }
function truncName(s, max) { return s && s.length > max ? s.slice(0, max) + '...' : s; }

// ── LAYOUT ──
var width  = window.innerWidth;
var height = window.innerHeight;

var svg = d3.select('#tree')
  .attr('width', width)
  .attr('height', height);

var gMain = svg.append('g');

var zoomBehavior = d3.zoom()
  .scaleExtent([0.08, 4])
  .on('zoom', function(e) { gMain.attr('transform', e.transform); });
svg.call(zoomBehavior);

var gLinks = gMain.append('g').attr('class', 'links');
var gNodes = gMain.append('g').attr('class', 'nodes');

var treemap = d3.tree();

var tip      = document.getElementById('tip');
var tipType  = document.getElementById('tip-type');
var tipName  = document.getElementById('tip-name');
var tipDesc  = document.getElementById('tip-desc');
var tipMeta  = document.getElementById('tip-meta');

function showTip(ev, d) {
  var dd = d.data;
  tipType.textContent = dd.type || '';
  tipName.textContent = dd.name || '';
  var descHtml = dd.desc || '';
  if (dd.ref) descHtml += '<br><a href="' + dd.ref + '" target="_blank">Microsoft Learn &rarr;</a>';
  tipDesc.innerHTML = descHtml;
  var meta = [];
  if (dd.seq) meta.push(dd.seq);
  if (dd.apqc) meta.push('APQC: ' + dd.apqc);
  if (dd.leafCount) meta.push(dd.leafCount + ' scenarios');
  tipMeta.textContent = meta.join(' \\u00b7 ');
  tip.classList.add('show');
  moveTip(ev);
}

function moveTip(ev) {
  var x = ev.clientX + 16, y = ev.clientY + 12;
  if (x + 440 > window.innerWidth) x = ev.clientX - 440;
  if (y + 160 > window.innerHeight) y = ev.clientY - 160;
  tip.style.left = x + 'px';
  tip.style.top  = y + 'px';
}

function hideTip() { tip.classList.remove('show'); }

// ── DIAGONAL ──
function diagonal(s, d) {
  return 'M ' + s.y + ' ' + s.x +
         ' C ' + ((s.y + d.y) / 2) + ' ' + s.x +
         ', ' + ((s.y + d.y) / 2) + ' ' + d.x +
         ', ' + d.y + ' ' + d.x;
}

// ── RENDER ──
var nodeId = 0;

function update(source) {
  var root = d3.hierarchy(rootData);
  var leaves = countLeavesData(rootData);
  var dynHeight = Math.max(height - 100, leaves * 22);

  treemap.size([dynHeight, Math.max(800, width - 500)]);
  var treeData = treemap(root);
  var nodes = treeData.descendants();
  var links = treeData.links();

  nodes.forEach(function(d) { d.y = d.depth * 260; });

  // ── Links ──
  var link = gLinks.selectAll('.link')
    .data(links, function(d) { return d.target.id || (d.target.id = ++nodeId); });

  var linkEnter = link.enter().append('path')
    .attr('class', 'link')
    .attr('d', function() {
      var o = { x: source.x0 || 0, y: source.y0 || 0 };
      return diagonal(o, o);
    });

  linkEnter.merge(link).transition().duration(400)
    .attr('d', function(d) { return diagonal(d.source, d.target); });

  link.exit().transition().duration(300)
    .attr('d', function() {
      var o = { x: source.x || 0, y: source.y || 0 };
      return diagonal(o, o);
    }).remove();

  // ── Nodes ──
  var node = gNodes.selectAll('.node')
    .data(nodes, function(d) { return d.id || (d.id = ++nodeId); });

  var nodeEnter = node.enter().append('g')
    .attr('class', function(d) { return 'node' + (d.data._children ? ' collapsed' : ''); })
    .attr('transform', function() { return 'translate(' + (source.y0 || 0) + ',' + (source.x0 || 0) + ')'; })
    .on('click', function(ev, d) {
      ev.stopPropagation();
      toggle(d.data);
      update(d);
    })
    .on('mouseenter', showTip)
    .on('mousemove', moveTip)
    .on('mouseleave', hideTip);

  nodeEnter.append('circle')
    .attr('r', 1e-6)
    .style('fill', function(d) { return hasKids(d.data) ? colorOf(d.data) : '#0b0f14'; })
    .style('stroke', function(d) { return colorOf(d.data); });

  nodeEnter.append('text')
    .attr('dy', '.35em')
    .attr('x', function(d) { return hasKids(d.data) ? -14 : 14; })
    .attr('text-anchor', function(d) { return hasKids(d.data) ? 'end' : 'start'; })
    .text(function(d) { return truncName(d.data.name, 48); });

  // badge
  nodeEnter.append('text')
    .attr('class', 'badge')
    .attr('dy', '-.7em')
    .attr('x', function(d) { return hasKids(d.data) ? -14 : 14; })
    .attr('text-anchor', function(d) { return hasKids(d.data) ? 'end' : 'start'; })
    .text(function(d) {
      var lc = d.data.leafCount;
      return lc ? lc + ' scenarios' : '';
    });

  // merge
  var nodeUpdate = nodeEnter.merge(node);

  nodeUpdate.transition().duration(400)
    .attr('transform', function(d) { return 'translate(' + d.y + ',' + d.x + ')'; })
    .attr('class', function(d) { return 'node' + (d.data._children ? ' collapsed' : ''); });

  nodeUpdate.select('circle').transition().duration(400)
    .attr('r', function(d) { return TYPE_RADIUS[d.data.type] || 5; })
    .style('fill', function(d) { return hasKids(d.data) ? colorOf(d.data) : '#0b0f14'; })
    .style('stroke', function(d) { return colorOf(d.data); });

  // exit
  var nodeExit = node.exit().transition().duration(300)
    .attr('transform', function() { return 'translate(' + (source.y || 0) + ',' + (source.x || 0) + ')'; })
    .remove();
  nodeExit.select('circle').attr('r', 1e-6);
  nodeExit.select('text').style('fill-opacity', 1e-6);

  // stash positions
  nodes.forEach(function(d) {
    d.data.x0 = d.x;
    d.data.y0 = d.y;
  });
  source.x0 = source.x || treeData.x;
  source.y0 = source.y || treeData.y;
}

// ── FIT VIEW ──
function fitView(dur) {
  setTimeout(function() {
    var root = d3.hierarchy(rootData);
    var lc = countLeavesData(rootData);
    treemap.size([Math.max(600, lc * 22), Math.max(800, width - 500)]);
    var td = treemap(root);
    var nodes = td.descendants();
    nodes.forEach(function(d) { d.y = d.depth * 260; });

    var xs = nodes.map(function(d) { return d.x; });
    var ys = nodes.map(function(d) { return d.y; });
    if (!xs.length) return;
    var pad = 60;
    var minX = Math.min.apply(null, xs) - pad;
    var maxX = Math.max.apply(null, xs) + pad;
    var minY = Math.min.apply(null, ys) - 180;
    var maxY = Math.max.apply(null, ys) + 280;
    var bw = maxY - minY;
    var bh = maxX - minX;
    var scale = Math.min(width / bw, height / bh, 1) * 0.88;
    var tx = (width - bw * scale) / 2 - minY * scale;
    var ty = (height - bh * scale) / 2 - minX * scale;
    svg.transition().duration(dur || 600).call(
      zoomBehavior.transform,
      d3.zoomIdentity.translate(tx, ty).scale(scale)
    );
  }, 120);
}

// ── INIT ──
rootData = JSON.parse(JSON.stringify(SOURCE));
initTree(rootData, 0);
rootData.x0 = height / 2;
rootData.y0 = 0;
update(rootData);
fitView(600);

// ── CONTROLS ──
function expandAll() {
  expandNode(rootData);
  update(rootData);
  fitView(800);
}

function collapseAll() {
  collapseNode(rootData, 0);
  update(rootData);
  fitView(800);
}

function resetView() {
  maxDepth = 2;
  rootData = JSON.parse(JSON.stringify(ORIGINAL));
  initTree(rootData, 0);
  rootData.x0 = height / 2;
  rootData.y0 = 0;
  update(rootData);
  fitView(600);
  document.getElementById('btnDepth').textContent = 'Depth: ' + maxDepth;
}

// depth toggle
document.getElementById('btnDepth').addEventListener('click', function() {
  maxDepth = (maxDepth % 4) + 1;
  document.getElementById('btnDepth').textContent = 'Depth: ' + maxDepth;
  rootData = JSON.parse(JSON.stringify(ORIGINAL));
  initTree(rootData, 0);
  rootData.x0 = height / 2;
  rootData.y0 = 0;
  update(rootData);
  fitView(600);
});

// search
var searchInput = document.getElementById('search');
var searchTimer;
searchInput.addEventListener('input', function() {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(doSearch, 200);
});

function doSearch() {
  var q = searchInput.value.trim().toLowerCase();
  var allNodes = gNodes.selectAll('.node');
  var allLinks = gLinks.selectAll('.link');

  if (!q) {
    allNodes.classed('dimmed', false).classed('highlight', false);
    allLinks.classed('dimmed', false);
    return;
  }

  var matchSet = new Set();
  function findMatches(d) {
    var name = (d.name || '').toLowerCase();
    var desc = (d.desc || '').toLowerCase();
    var apqc = (d.apqc || '').toLowerCase();
    if (name.indexOf(q) !== -1 || desc.indexOf(q) !== -1 || apqc.indexOf(q) !== -1) {
      matchSet.add(d.name + '|' + d.seq);
    }
    (d.children || []).forEach(findMatches);
    (d._children || []).forEach(findMatches);
  }
  findMatches(rootData);

  // mark ancestors
  function markAncestors(d, path) {
    var key = d.name + '|' + d.seq;
    if (matchSet.has(key)) {
      path.forEach(function(p) { matchSet.add(p.name + '|' + p.seq); });
    }
    var kids = (d.children || []).concat(d._children || []);
    kids.forEach(function(c) { markAncestors(c, path.concat([d])); });
  }
  markAncestors(rootData, []);

  allNodes.each(function(d) {
    var key = d.data.name + '|' + d.data.seq;
    var match = matchSet.has(key);
    d3.select(this).classed('dimmed', !match)
      .classed('highlight', match && (d.data.name || '').toLowerCase().indexOf(q) !== -1);
  });

  allLinks.classed('dimmed', function(d) {
    var tKey = d.target.data.name + '|' + d.target.data.seq;
    return !matchSet.has(tKey);
  });
}

// resize
window.addEventListener('resize', function() {
  width = window.innerWidth;
  height = window.innerHeight;
  svg.attr('width', width).attr('height', height);
});
<\/script>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"Generated: {os.path.basename(OUTPUT)}")
print(f"  End-to-end: {n_e2e}  |  Process areas: {n_area}  |  Processes: {n_proc}")
print(f"  File size: {os.path.getsize(OUTPUT) / 1024:.0f} KB")

# ── JSON export for future reference ────────────────────────────────
JSON_OUTPUT = os.path.join(SCRIPT_DIR, 'ProcessCatalogue_MindMap.json')

mindmap_export = {
    "metadata": {
        "title": "D365 Business Process Catalogue - Mind Map",
        "description": "Hierarchical mind map of D365 Finance & Operations business processes from the Business Process Library.",
        "source": "ProcessCatalogue.json",
        "generatedBy": "build_mindmap.py",
        "stats": {
            "endToEndProcesses": n_e2e,
            "processAreas": n_area,
            "processes": n_proc,
        }
    },
    "tree": tree,
}

with open(JSON_OUTPUT, 'w', encoding='utf-8') as jf:
    json.dump(mindmap_export, jf, indent=2, ensure_ascii=False)

print(f"JSON exported: {os.path.basename(JSON_OUTPUT)} ({os.path.getsize(JSON_OUTPUT) / 1024:.0f} KB)")
