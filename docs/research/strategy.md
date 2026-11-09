# Research plan: from evidence to a playable room

**Reviewed: 2026-11-09.** This is an initial source review and proposed experiment plan. External demonstrations have not been independently reproduced by this lab.

## Recommendation

Start with Blender and Python for editable assets, CadQuery for precision geometry, and one small game prototype. Evaluate a hosted mesh generator alongside scripted modeling. Use REA to investigate one bounded mechanic in a small, inspectable game. Select the game engine after a short integration test.

Our main question is: **How much useful, editable, tested work can an AI complete, and how much human repair does it require?**

## Four separate research tracks

| Track | Question | Deliverable |
| --- | --- | --- |
| [REA and games](./rea.md#documented-game-examples) | Can an agent recover a behavior with verifiable evidence? | A behavior specification and independent tests |
| [3D and CAD](./ai-modeling.md) | Which workflow produces useful geometry and survives revisions? | Editable source, exported asset, and quality report |
| [Languages and libraries](./ai-stack.md) | Which stack lets the agent build and repair our feature reliably? | A working feature and regression test |
| Integration | Can the outputs function together? | A playable room with a door, prop, interaction, and sound |

## Evidence levels

Label every finding as one of: **documented API**, **author-reported demonstration**, **independently reproduced**, or **validated in our game**. Repository popularity and attractive videos do not move a claim up this ladder. A documented feature is evidence of an available interface, not evidence that it will meet our quality target.

For every candidate, record its exact version, source URL, review date, host requirements, license/asset terms, price at test time, and known limitations. Keep inputs, prompts, failures, and cleanup revisions alongside the best output.

## First experiment sequence

| Experiment | Same brief for each candidate | Main acceptance checks |
| --- | --- | --- |
| EXP-005: REA behavior recovery | A small movement, aiming, or sound-pan function; hide known source during analysis | Compare inferred behavior with ground truth and boundary cases |
| EXP-006: Editable prop | A crate with named lid and body, prescribed dimensions, pivot, and material budget | Correct dimensions; lid opens; clean engine import; revision succeeds |
| EXP-007: Precision CAD | A bracket with specified holes, thickness, and spacing | Dimensions and valid solid; change one parameter without breaking the model |
| EXP-008: Code and repair | An opening door with interaction range and a reset action | Correct behavior; deliberately introduced bug fixed; no regressions |
| EXP-009: End-to-end room | Integrate one accepted prop and door with sound | Packaged build works; collision, scale, audio, and frame time checked |

These are proposed extensions to EXP-001 through EXP-004, not completed tests.

## How to compare fairly

1. Write the specification and acceptance tests before prompting.
2. Establish a manual or known-good baseline.
3. Give each workflow the same inputs, iteration limit, and time budget.
4. Run at least three independent attempts when practical; report the range as well as the best result.
5. Request a realistic change after the first success. Editability matters more than a single attractive render.
6. Count prompting, cleanup, integration, and verification in total human time.

Use the same model and comparable tool access for language comparisons where possible. Keep documentation available for both candidates. Report engine and tooling effects separately from language effects; this is not a universal language leaderboard.

## Measures that matter

- **Correctness:** acceptance checks passed, defects, and regressions.
- **3D usefulness:** silhouette, dimensions, topology, UVs, materials, pivots, collision, and export behavior.
- **Editability:** success of the second requested change and time to make it.
- **Efficiency:** generation time, human minutes, retries, and actual cost.
- **Runtime:** frame time, memory, and loading on the chosen target hardware.
- **Traceability:** source and asset provenance, versions, and repeatable steps.

Do not compress all of these into a single score initially. A cheap mesh with hours of cleanup may lose to a slower script that remains editable.

## Decision gates

**First:** one prop and one mechanic pass their tests. **Next:** both survive a change request. **Then:** the integrated room runs on our target machine. Expand to characters, rigging, large environments, or runtime AI only after these gates.

Use the [experiment template](../experiments/template.md) for every trial. The next concrete step is EXP-006: a small editable prop made with Blender Python, compared with a generated mesh.
