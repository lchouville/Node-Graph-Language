# Pipeline

```txt
Input (.ngl)
  → Lexer
  → Parser
  → AST (nodes, edges)
  → Validation
  → Layout
  → Renderer (SVG)
```

## 1. Input
An `.ngl` text file
### Responsability
- provide the plain text in the next step

## 3. Lexer
### Role
- Read the text line by line.
- Ignore comments (//).
- Identify the main structures:
- node declaration
- edge declaration
- chart declaration

## 3. Parser

Read the file and convert it into internal data.

For example :
```md
parsing["Parsing step"]
parsing -- validation
```

becomes :
```json
"nodes" [
    {
        "id": "parsing",
        "text": "Parsing step"
    }
]
```
```json
"Edges" [
    {
        "from": "parsing",
        "to": "validation",
        "label": null
    }
]
```

### Responsibility
- understanding syntax
- building internal structures
- does not check logic

## 4. AST (internal structure)
**Node**
- id
- text

**Edge**
- from
- to
- label (optionnel)

**Graph**
- nodes: list
- edges: list
- name

## 5. Validation
### Responsibility
- Reject ambiguous graphs
- Protect the renderer

## 6. Layout
### Responsibility
- decide where to place the nodes
- decide where the edges go

## 7. Renderer
### Responsibility
- convert the layout to SVG