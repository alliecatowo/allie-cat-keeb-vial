import shell from 'shelljs';
import fs from 'fs';
import path from 'path';

const API_DIR = path.join('docs', '_api');
const DOCS_DIR = 'docs';

if (shell.exec('doxygen').code !== 0) {
  shell.echo('Doxygen failed');
  shell.exit(1);
}
shell.rm('-rf', API_DIR);
shell.mkdir('-p', API_DIR);
if (shell.exec(`npx moxygen -g -o 'docs/_api/%s.md' docs/_doxygen/xml`).code !== 0) {
  shell.echo('moxygen failed');
  shell.exit(1);
}

shell.find(API_DIR).filter(f => /README\.md$/i.test(f)).forEach(f => {
  shell.mv(f, path.join(path.dirname(f), 'index.md'));
});

function collect(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).sort().map(name => {
    const p = path.join(dir, name);
    if (fs.statSync(p).isDirectory()) {
      return { text: name, items: collect(p) };
    }
    if (name.endsWith('.md')) {
      const link = '/' + path.relative('docs', p).replace(/\\/g, '/');
      return { text: name.replace(/\.md$/, ''), link };
    }
    return null;
  }).filter(Boolean);
}

function collectDocs(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .sort()
    .filter(name => !['_api', '.vitepress', 'public'].includes(name))
    .map(name => {
      const p = path.join(dir, name);
      if (fs.statSync(p).isDirectory()) {
        const items = collectDocs(p);
        return items.length ? { text: name, items } : null;
      }
      if (name.endsWith('.md')) {
        const link = '/' + path.relative('docs', p).replace(/\\/g, '/');
        return { text: name.replace(/\.md$/, ''), link };
      }
      return null;
    })
    .filter(Boolean);
}

const sidebar = [
  { text: 'Guide', items: collectDocs(DOCS_DIR) },
  { text: 'API', items: collect(API_DIR) }
];

fs.writeFileSync(path.join('docs', '.vitepress', 'auto_sidebar.json'), JSON.stringify(sidebar, null, 2));

