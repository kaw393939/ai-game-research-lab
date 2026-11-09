import { readFileSync, existsSync, statSync, readdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { createHash } from 'node:crypto';
const root = resolve(import.meta.dirname, '..');
const items = JSON.parse(readFileSync(resolve(root, 'docs/.vitepress/data/narration.json'), 'utf8'));
const ids = new Set();
for (const item of items) {
  if (ids.has(item.id)) throw new Error(`Duplicate audio ID: ${item.id}`);
  ids.add(item.id);
  const signature = createHash('sha256').update(item.text + '|Kokoro-82M-bf16|af_heart|1.04|mp3-96k').digest('hex');
  if (signature !== item.generationHash) throw new Error(`Regenerate changed narration: ${item.id}`);
  const base = resolve(root, 'docs/public/narration', item.id);
  if (!existsSync(`${base}.mp3`) || statSync(`${base}.mp3`).size < 1000) throw new Error(`Missing audio: ${item.id}`);
  if (readFileSync(`${base}.txt`, 'utf8').trim() !== item.text.trim()) throw new Error(`Transcript mismatch: ${item.id}`);
  if (!(item.durationSeconds > 0)) throw new Error(`Missing duration: ${item.id}`);
}
for (const file of readdirSync(resolve(root, 'docs/research')).filter(f => f.endsWith('.md'))) {
  const page = readFileSync(resolve(root, 'docs/research', file), 'utf8');
  const match = page.match(/<AudioSummary id="([^"]+)"/);
  if (!match || !ids.has(match[1])) throw new Error(`Missing research player: ${file}`);
}
console.log(`Verified ${items.length} recordings, transcripts, and research-page players.`);
