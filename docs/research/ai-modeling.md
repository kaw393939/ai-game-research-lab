# AI for 3D modeling and CAD

**Source review: 2026-11-09.** Candidates below have not been benchmarked by this lab. Recommendations describe our proposed tests.

## Three distinct workflows

1. **AI writes modeling instructions:** Python or CAD code creates geometry with parameters we can revise.
2. **AI generates mesh data:** text or images become a mesh, followed by cleanup and integration.
3. **AI assists an established task:** search, automation, deformation, or other narrowly defined operations inside a modeling application.

We should evaluate these separately. Visual resemblance, a well-formed solid, and an animation-ready mesh are different outcomes.

## Candidate map

| Tool | Documented interface or capability | Proposed use and limitation |
| --- | --- | --- |
| Blender | [Python API](https://docs.blender.org/api/current/) for scene and data operations | Start here for scripted props, scene assembly, and exports. Measure whether AI scripts preserve editable structure. |
| Community MCP for Blender | [Project](https://github.com/ahujasid/mcp-for-blender) connects an agent to a Blender add-on and Python server | Compare interactive tool control with direct scripts. It is a community project, not an official Blender Foundation integration. |
| AutoCAD | [Assistant](https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-WhatsNew/files/GUID-A656580B-871D-48A8-9559-AC71FC357E03.htm) provides AI-guided help; [Automation APIs](https://aps.autodesk.com/automation-apis) can run scripts and routines against DWGs | Treat product help and geometry automation as separate capabilities. Do not infer general prompt-to-model support from an assistant. |
| CadQuery | [Python library](https://cadquery.readthedocs.io/en/latest/) for parametric CAD | Test precise mechanical props with dimensions and revisions. CAD output still needs a suitable mesh conversion for game use. |
| Houdini | [ML workflow documentation](https://www.sidefx.com/docs/houdini/ml/building_blocks/framework.html) covers data, training, and inference stages | A later candidate for controlled procedural and learned workflows; measure setup effort before adopting it. |
| Meshy | [API](https://docs.meshy.ai/en/api/text-to-3d) documents text/image generation and related remesh, UV, rigging, and animation operations | Compare rapid mesh generation with scripted assets. API availability does not establish topology quality for our use. |
| TRELLIS.2 | [Microsoft research repository](https://github.com/microsoft/TRELLIS.2) provides a 3D generation implementation | Research candidate; check its current hardware and dependency requirements before assuming local Mac execution. |

## What the research literature adds

[SceneCraft](https://arxiv.org/abs/2403.01248) investigates generating Blender-executable Python for scenes. [Text-to-CadQuery](https://arxiv.org/abs/2505.06507) explores translating natural language into parametric CAD code. These are useful evidence that code-based modeling is an active research direction; paper results are not a guarantee on our props or hardware.

## Our first comparison

Give all workflows a crate brief with a separate opening lid, known dimensions, a specified hinge pivot, and an engine asset budget. Compare Blender scripting with a mesh-generation route; keep the precision bracket experiment separate for CadQuery and AutoCAD.

Request a second version with a wider lid and unchanged hinge behavior. Inspect named parts, dimensions, normals, UVs, material slots, texture size, and collision. Export and run it in the actual engine. A rendered screenshot alone cannot pass the test.

## AutoCAD on this Mac

Autodesk documents different programming interfaces across platforms. Confirm the specific product, edition, and version before choosing AutoLISP, .NET, or ObjectARX. Do not assume a Windows automation example will work on macOS. [Platform interface matrix](https://help.autodesk.com/cloudhelp/2024/ENU/AutoCAD-MAC-Customization/files/GUID-E6429154-36DF-4D84-8ABC-9FCA15B66158.htm) (versioned 2024 reference; recheck against the installed release).

My starting preference is Blender for game assets and CadQuery for the precision experiment. AutoCAD becomes a higher priority if our project needs DWG workflows or existing CAD content. This is a scope decision, not a claim that one application is universally better.
