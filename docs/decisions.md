# Decision log

Record consequential choices with the alternatives considered and links to evidence.

## DEC-001 — Research publishing stack

**Date:** 2026-11-09  
**Status:** Accepted

Use VitePress and GitHub Pages, as requested for this project. Store research in Markdown, review changes through Git, and publish the built static site from the `gh-pages` branch. Run `npm run docs:publish` to update the live site.

**Deployment constraint:** The available GitHub login cannot upload Actions workflows. Publishing therefore uses an explicit local build and branch push.

**Implications:** The research site is static and public. Experiments requiring model inference or private credentials run separately; the site publishes their documented results.

## Pending decisions

Game genre, target platform, engine, AI models, audio tools, and 3D workflow remain open. Record those decisions after the requirements and experiments provide evidence.
