<h1>
    <a href="README.md"><img src="https://img.icons8.com/color/48/000000/great-britain-circular.png" width="30" alt="English"/></a> 
    <a href="README-FR.md"><img src="https://img.icons8.com/color/48/000000/france-circular.png" width="30" alt="Français"/></a>
    Glossary — NGL
</h1>

### NGL (Node Graph Language)
A typed declarative language designed to describe graphs in a textual and compilable form.

### NGL Source File
A text file with the extension `.ngl`, containing a  definition of a graph.

### Node
The fundamental entity of a graph.
A node has:
- a unique identifier
- an explicit type
- an optional set of attributes

A node represents a step, action, or decision in a flowchart.

### Edge
A directional link between two nodes.
An edge expresses a logical flow in the graph.

An edge can have:
- a source
- a target
- optional attributes (label, condition, etc.)

### Compiler
Set of steps that transform an .ngl file into a graphical output.
The NGL compiler follows a strict pipeline:
- parsing
- validation
- normalization
- rendering
- export

### Parser
Component responsible for transforming the source text into a syntactic structure (AST).
The parser does not validate the business logic.

### AST
Structured representation of the source graph, independent of rendering.
The AST is immutable and constitutes the central boundary of the compiler.

### Validator
Component responsible for checking the consistency of the graph:
- valid references
- compatible types
- rules specific to the graph type

No automatic corrections are made.


### Normalizer
Step that transforms the validated AST into a normalized form that is explicit and usable by the renderer.
Examples:
- resolution of default values
- expansion of implicit syntaxes

### Renderer
Component responsible for transforming the normalized AST into graphic primitives.
The renderer does not contain any business logic.

### Export
Component responsible for generating the final format (SVG, PNG, etc.).

### Diagnostics
Structured message produced by the compiler to report:
- errors
- warnings
- information

Diagnostics are precise, localized, and explicit.

### Strict Mode
Default mode of NGL where any ambiguity or inconsistency results in a compilation error.
