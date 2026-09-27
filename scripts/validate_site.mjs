import crypto from 'node:crypto';
import fs from 'node:fs';

const failures = [];
const html = fs.readFileSync('index.html', 'utf8');
const app = fs.readFileSync('app.js', 'utf8');
const graphBytes = fs.readFileSync('data/research-graph.json');
const graph = JSON.parse(graphBytes);
const provenance = JSON.parse(fs.readFileSync('data/provenance.json', 'utf8'));
const digest = crypto.createHash('sha256').update(graphBytes).digest('hex');

const projectCount = graph.nodes.filter((node) => node.type === 'Project').length;
if (graph.nodes.length !== 182 || graph.edges.length !== 393 || projectCount !== 85) {
  failures.push('graph counts must remain 182 nodes / 393 edges / 85 projects');
}
if (digest !== provenance.sha256) failures.push('graph SHA-256 differs from provenance');
if (!app.includes("const GRAPH_URL='data/research-graph.json'")) {
  failures.push('runtime graph must use the pinned local snapshot');
}
for (const unsupported of ['0.37 px', '91%', '84.6 h', '>LOCKED<']) {
  if (html.includes(unsupported)) failures.push(`unsupported performance claim: ${unsupported}`);
}
for (const id of ['project-count', 'node-count', 'edge-count', 'evidence']) {
  if (!html.includes(`id="${id}"`)) failures.push(`missing evidence interface id: ${id}`);
}
if (html.includes('Research Quality Upgrade') || html.includes('before and after')) {
  failures.push('reader-facing upgrade scorecard language is forbidden');
}
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Validated ${projectCount} projects across ${graph.nodes.length} nodes and ${graph.edges.length} edges.`);
