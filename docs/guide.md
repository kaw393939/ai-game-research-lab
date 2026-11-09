# Mission & method

Explore the limits of advanced AI across the full game creation pipeline. Our target is a small playable vertical slice, with enough evidence to explain which tools helped, which failed, and how much human work remained.

## Principles

- Start with a constrained task and a clear acceptance test.
- Preserve prompts, tool versions, settings, inputs, and output revisions.
- Compare AI-assisted work with a practical manual baseline.
- Record failed attempts and repair time, not just the best output.
- Separate observed results from hypotheses and vendor claims.

## Shared evaluation dimensions

| Dimension | What we record |
| --- | --- |
| Functional quality | Acceptance tests passed and defects discovered |
| Creative control | Ability to follow direction and reproduce style |
| Integration | Import failures, conversion work, and engine compatibility |
| Human effort | Setup, prompting, review, cleanup, and debugging minutes |
| Cost | Actual billed usage and relevant hardware costs |
| Runtime | Frame time, memory, latency, and asset size where relevant |
| Reproducibility | Version, date, inputs, seed where available, and repeat outcomes |
| Usage rights | Source terms, asset provenance, attribution, and unresolved questions |

## Evidence standard

A result needs an artifact or commit, a repeatable procedure, and a dated observation. A capability is **untested** until we run it. Use **promising**, **blocked**, or **validated for this task** only when evidence supports the label. A successful narrow test is not a claim of general capability.

## Publishing research

Write findings as Markdown under `docs/`. Keep credentials and private inputs out of the repository. Put large source assets in appropriate asset storage and link to a versioned manifest. Record an asset's origin and usage terms before treating it as shippable.
