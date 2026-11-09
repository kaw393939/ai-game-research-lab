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

## Local audio narration (Apple Silicon)

Kokoro runs through MLX Audio in an isolated Python 3.12 environment. The first run downloads model files and English text-processing data; subsequent runs default to Hugging Face offline mode. No speech API key is required. Generated WAV files and the local environment are ignored by Git.

This machine is already configured. Generate narration from a plain-text file:

```sh
npm run audio:generate -- examples/ai-gaming-one-minute.txt --output audio/explainer.wav --speed 1.11
```

The default preset is `af_heart`. Change it with `--voice`; use `--download` if a newly selected voice is not cached. Existing output files are preserved unless `--force` is passed.

To recreate the environment on a compatible Apple Silicon Mac with Python 3.12:

```sh
sh scripts/setup-tts.sh
npm run audio:generate -- examples/ai-gaming-one-minute.txt --output audio/explainer.wav --download
```

Set `TTS_PYTHON` to the Python 3.12 executable if it is not named `python3.12`. The dependency snapshot is in `requirements/tts-macos-py312.lock.txt`; model weights live in the local Hugging Face cache. This is not a cross-platform dependency lock.

Sources: [MLX Audio Kokoro guide](https://github.com/Blaizzy/mlx-audio/blob/main/docs/models/tts/kokoro.md), [Kokoro MLX model card](https://huggingface.co/mlx-community/Kokoro-82M-bf16). The example's research sources are linked on the site's REA and AI modeling pages. It describes author-reported game examples, not independent replications by this lab.

## Research audio on GitHub Pages

The `/listen` page collects all recordings. Every research page also has a player, an MP3 download, and a collapsible transcript. Audio never autoplays. Starting one player pauses the others on the page.

To update a summary, edit its `text` in `docs/.vitepress/data/narration.json`, then run:

```sh
npm run audio:site
npm run docs:publish
```

Generation uses the locally cached Kokoro model and ffmpeg. It reuses unchanged recordings and updates the downloadable transcripts and duration labels. Review the narration when changing a research page; page edits do not automatically rewrite its summary. Commit the manifest, MP3s, transcripts, and source changes together. The regular site build validates that all research pages have players and that recordings match their transcripts.

Audio assets live in `docs/public/narration/` and are intentionally public. Keep personal recordings and private material in the ignored local `audio/` directory.
