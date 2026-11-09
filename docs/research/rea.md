# REA: investigating how games work

<AudioSummary id="rea" />

**Reviewed:** 2026-11-09 · **CLI tested:** rea-agents 6.8.0 · **Status:** Initial static inspection completed; gameplay analysis remains untested.

[REA on GitHub](https://github.com/morluto/rea) is an agent-facing reverse-engineering toolkit. Its CLI and MCP interface connect analysis workflows to an AI assistant. It is useful for investigating existing software; it does not generate a complete game or recover an original source repository automatically. Native disassembly and pseudocode workflows require a supported analysis provider, such as Hopper, Ghidra, IDA, or Kuna. [Project overview](https://github.com/morluto/rea#readme)

## Why investigate it for our game?

Our proposed use is to study a narrowly defined behavior, write down what the evidence supports, and build an independent implementation for our own prototype.

| Research track | Proposed question | Useful outcome |
| --- | --- | --- |
| Programming | How does a small interaction change state? | A state diagram and tests for our own implementation |
| Audio | How does a positional sound calculation behave? | A measured formula and a listening test |
| 3D integration | Which runtime and asset containers are actually present? | A map of the asset pipeline and its unknowns |
| Reliability | Can an agent distinguish evidence from guesses? | A reproducible investigation with explicit limits |

These are proposed experiments, not demonstrated capabilities on our target games.

## Start with an installation inventory

REA's `inspect-desktop-application` command inventories a selected directory and inspects bounded headers and metadata. It does not launch the target or modify it. It can suggest runtime families and follow-up probes, but those candidates do not prove that a component executes. A directory inventory is not archive extraction or decompilation. [Desktop inspection guide](https://github.com/morluto/rea/blob/main/docs/desktop-applications.md)

```sh
rea inspect-desktop-application /absolute/path/to/game --json
```

Save the output outside the game installation. Review coverage and limitations before interpreting results. An empty candidate list alone does not prove that a game is absent or identify its engine.

## Local feasibility test

A first test used REA 6.8.0 on macOS with Node 22.23.4. The selected Steam game directory contained leftover logs rather than a game executable. The operation returned an inventory, with no runtime candidate or follow-up binary probe. This establishes that the inventory workflow runs locally; it does **not** establish successful analysis of a game's implementation.

The CLI also inventoried a launcher shortcut and a separate user-data directory. Raw reports remain local. Personal save names, profile paths, logs, screenshots, and save contents are not part of this public page.

**Result:** Installation discovery works for this narrow test. Native game analysis is blocked until a complete installation or a suitable executable is available.

## A bounded next experiment

1. Select a complete installation and one concrete behavior to investigate.
2. Inventory the directory and identify the actual executable.
3. Check provider compatibility with that executable format and architecture.
4. Collect the smallest relevant evidence set and preserve its limitations.
5. Implement a small original analogue in our prototype.
6. Compare behavior with explicit tests and record human effort.

For a first gameplay study, a small open-source sample game would let us compare inferred behavior against known source code. That gives us a way to measure the agent's accuracy before tackling a large commercial title.

## Setup and limits

The tested package requires a newer Node runtime than the machine's existing Node 22.22.2. This trial used a separate npm-provided Node 22.23.4 runtime and did not register a persistent MCP server. Future runs should record the exact package and provider versions. Consult the current [installation requirements](https://github.com/morluto/rea#what-you-can-analyze) before setup.

CLI results can be saved and inspected later through REA's evidence workflows. Separate command invocations are separate processes; preserve reports when you need continuity. [CLI and evidence guide](https://github.com/morluto/rea/blob/main/docs/getting-started/cli.md)

Use the [experiment template](../experiments/template.md) to record the hypothesis, inputs, evidence, failure cases, and conclusion. Do not treat filenames, model guesses, or a plausible-looking pseudocode listing as proof of gameplay behavior.

## Documented game examples

Reviewed 2026-11-09. These are external reports, not reproductions by this lab.

| Example | Reported work | What we can learn |
| --- | --- | --- |
| [DX-Ball](https://rea.tools/showcase/dx-ball/) | An official showcase traces sound panning through instructions, callers, and constants. It reports 3,205 original-code comparisons and 63 matching compiled bytes for the highlighted function. | Inspect assembly when pseudocode is incomplete; verify the recovered behavior with independent tests. The broader reconstruction is still described as in progress. |
| [Touhou 4](https://rea.tools/showcase/th04/) | An official showcase traces bullet-ring angle calculations in a 16-bit DOS executable, with compiler checks for the surrounding reconstructed code. | Pick a small mathematical mechanic with visible inputs and outputs. |
| [Ski or Die: Snowball War](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | A community author reports using REA and Ghidra to recover rules and implement the minigame in Rust with SDL2. The repository documents setup and evidence. | Study the path from binary evidence to a written specification and implementation. Playability and fidelity remain author-reported until we reproduce them. |

These examples support a narrow investigation workflow. They do not establish automatic recovery of a complete modern game, its original project files, or a reusable 3D asset pipeline. Our first replication should use a small source-available target so we can compare the agent's answer against ground truth.
