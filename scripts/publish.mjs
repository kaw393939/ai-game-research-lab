import { mkdtempSync, cpSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';
const dir = mkdtempSync(join(tmpdir(), 'game-lab-pages-'));
const git = (...args) => execFileSync('git', args, { cwd: dir, stdio: 'inherit' });
try {
  git('init', '-b', 'gh-pages');
  git('remote', 'add', 'origin', 'https://github.com/kaw393939/ai-game-research-lab.git');
  const auth = ['-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential'];
  // Preserve deployment history when the branch already exists.
  const refs = execFileSync('git', [...auth, 'ls-remote', '--heads', 'origin', 'gh-pages'], { cwd: dir, encoding: 'utf8' });
  if (refs.trim()) {
    git(...auth, 'fetch', 'origin', 'gh-pages');
    git('checkout', '-B', 'gh-pages', 'FETCH_HEAD');
    git('rm', '-r', '--ignore-unmatch', '.');
  }
  cpSync('docs/.vitepress/dist', dir, { recursive: true });
  writeFileSync(join(dir, '.nojekyll'), '');
  git('add', '.');
  git('commit', '--allow-empty', '-m', 'Publish research site');
  git(...auth, 'push', 'origin', 'gh-pages');
} finally { rmSync(dir, { recursive: true, force: true }); }
