# AI Game Research Lab

A public research notebook exploring the limits of AI-assisted video game development: programming, audio, 3D assets, animation, and integration.

**Site:** https://kaw393939.github.io/ai-game-research-lab/

## Local development

Requires Node.js 22 or newer and npm.

```sh
npm ci
npm run docs:dev
```

Build with `npm run docs:build`; inspect the build with `npm run docs:preview`.

## Contributing research

Start with `docs/guide.md`, copy `docs/experiments/template.md`, and add your experiment to the register. Document versions, dates, prompts, costs, failed attempts, and evidence. Proposed experiments are not completed results.

## Deployment

Run `npm run docs:publish` with an authenticated GitHub CLI (`gh`) to build and publish to the `gh-pages` branch. GitHub Pages serves that branch. Commit and push source changes to `main` separately.

The current GitHub login lacks the workflow scope needed to upload GitHub Actions workflows, so publishing is explicit rather than automatic on source pushes.

Vite is pinned to patched version 6.4.6 through an npm override; the VitePress production build has been verified with this version.
