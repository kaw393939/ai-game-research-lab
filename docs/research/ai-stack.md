# Languages and libraries for AI-assisted game work

**Reviewed: 2026-11-09.** This is a capability map, not a popularity ranking or an AI coding benchmark.

## Choose by job

AI can write code for an application, operate it through tools, or run as part of the finished application. Those three roles need different libraries. An engine API or geometry library is not itself an AI model.

| Layer | Languages and libraries | Why investigate it |
| --- | --- | --- |
| Asset automation | Python, [Blender bpy](https://docs.blender.org/api/current/), [CadQuery](https://cadquery.readthedocs.io/en/latest/), [Trimesh](https://trimesh.org/) | Generate editable geometry, batch-process assets, and inspect meshes. |
| Model experimentation | Python, [PyTorch](https://pytorch.org/), [Transformers](https://huggingface.co/docs/transformers/index) | Evaluate local models when hardware and model support fit the experiment. Not required just to ask a coding assistant for a script. |
| Model deployment | [ONNX Runtime](https://onnxruntime.ai/docs/) with Python, C++, C#, or JavaScript interfaces | Test supported model inference outside the original training stack. Conversion and operator compatibility need validation. |
| Browser prototype | JavaScript/TypeScript and [Three.js](https://threejs.org/docs/) | A shareable asset viewer and small interactive tests. Rendering is one part of a full game runtime. |
| Godot gameplay | [GDScript, C#, and C/C++ through GDExtension](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_languages.html) | Compare short iteration loops and integration effort on our vertical slice. |
| Unity gameplay | [C# scripts and Unity APIs](https://docs.unity.com/en-us/engine/6000.7/manual/scripting/get-started/creating-scripts) | Candidate if its editor and asset ecosystem fit our project. |
| Unreal tooling | [Editor Python](https://dev.epicgames.com/documentation/unreal-engine/scripting-the-unreal-editor-using-python?lang=en-US) | Useful for editor automation; this Python environment is not packaged-game gameplay scripting. |
| CAD automation | [AutoLISP, ObjectARX, and platform-dependent AutoCAD APIs](https://aps.autodesk.com/developer/overview/autocad-api) | Research only against the installed product's supported interfaces. |
| Agent integration | [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture) | Connect agents to exposed tools and resources. MCP is an integration protocol, not a game engine or an intelligence model. |
| Reconstruction reference | [Rust + SDL2 in the Ski or Die community project](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | A concrete reported example of implementing behavior recovered through REA. Not evidence that Rust is best for our game. |

## Proposed initial stack

Use **Python for asset scripts and measurements**, **TypeScript for small browser viewers**, and **one engine's native gameplay language** for the playable slice. Keep model-provider details behind a small interface if we later add runtime inference.

Avoid training a model or installing a large agent framework until an experiment requires it. First establish whether a direct script and explicit tests solve the task.

## What to measure in AI coding trials

Ask for the same door interaction, save/reset behavior, and one bug repair. Measure first-pass correctness, time to a working build, hallucinated APIs, regression rate, human intervention, and ease of a requested change.

Record model/version, engine/library version, documentation supplied, tools available, and attempt count. Differences in editor access and API documentation can dominate the result; do not attribute every failure to the programming language.

## Two kinds of game AI

**Development-time AI** helps build assets and code. **Runtime AI** executes while someone plays. The latter adds latency, reliability, cost, and reproducibility requirements. We should establish a working conventional game loop before testing runtime model features.
