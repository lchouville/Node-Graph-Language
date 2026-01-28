# AST (Internal Structure)
## 1. Graph
An `.ngl` file becomes a single Graph object.

### Responsibilities
- carry the name of the flowchart
- contain nodes + edges

### Conceptual data
- name
- nodes
- edges

## 2. Node
A node is a declarative entity.

### Data
- id (string)
- text (string | null)

### Implicit rules:
- no logic
- no type
- no position

## 3. Edge
An edge is a directional relationship.

### Data
- from (node ID)
- to (node ID)
- label (string | null)

### Important:
- the edge does NOT know the nodes themselves,
- only their identifiers.