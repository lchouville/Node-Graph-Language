<h1>
    <a href="README.md"><img src="https://img.icons8.com/color/48/000000/great-britain-circular.png" width="30" alt="English"/></a> 
    <a href="README-FR.md"><img src="https://img.icons8.com/color/48/000000/france-circular.png" width="30" alt="Français"/></a>
    Node Graph Language
</h1>

## ℹ️ Introduction

**Node Graph Language *(NGL)*** is a typed declarative language and compiler for describing and generating graph-based structures from plain text files.

**NGL** focuses on explicit typing, strict validation, and a clean compilation pipeline, transforming `.ngl` files into visual outputs such as `SVG` or `PNG`.

The project is intentionally designed as a compiler, not a renderer-first tool. Source files are parsed into an Abstract Syntax Tree `(AST)`, validated, normalized, and then rendered through a dedicated backend.

### Scope actuel

The initial implementation of **NGL** targets flowcharts only.
- This limitation is deliberate: it allows the language rules, type system, and compilation pipeline to remain strict and predictable, while keeping the architecture open to future graph types such as:
- state machines
- dependency graphs
- execution pipelines
- node-based systems

### Design Goal

**NGL** is built around the following principles:
- Strict syntax: no ambiguous or implicit behavior
- Typed nodes and edges: structure errors are caught early
- Separation of concerns: parsing, validation, and rendering are isolated
- Extensibility: new graph types can be added without breaking existing ones
- Tooling-first mindset: the language is designed to support editor tooling (e.g. VS Code extensions)

### File format

**NGL** source files use the `.ngl` extension.

### Project status

**NGL** is currently in an early development stage.
The focus is on language definition, compiler architecture, and flowchart support before expanding to additional graph types.

## 🛠️ Installation

## 📚 Documentations

## 👤 Authors & Collaborators

<table style="border-collapse: collapse; border: none; width: 100%">