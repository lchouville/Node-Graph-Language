# Layout & Renderer

## 1. Layout
### 1.1 Objectiv
Determine for each node:
- a position `(x, y)`
- a size `(width, height)`

### 1.2 Default Layout
**Rules**
- nodes are placed from top to bottom
- order = declaration order or simple topological order
- constant spacing between nodes
- fixed width
- fixed height

```md
[ Node A ]
    |
[ Node B ]
    |
[ Node C ]
 ```

### 1.3 Data produced by the layout
The layout transforms the AST into an enriched (but temporary) structure:
- PositionedNode
  - id
  - text
  - x, y
  - width, height
- PositionedEdge
  - from
  - to
  - label
  - start(x, y)
  - end(x, y)

## 2. SVG Rederer
### 2.1 What the renderer receives
- Positioned nodes
- Positioned edges
- Labels

The renderer does not know the grammar or validation.

### 2.2 Minimal SVG representation
**Node**
- `<rect>` → the node
- `<text>` → the node's text
- Horizontally centered text
- Optional multi-line text (bonus)

**Edge**
- `<line>` or `<path>`
- single arrow (SVG marker or triangle)
- `<text>` for the label (in the middle of the line)

### 2.3 Drawing order (important)
1. edges (below)
2. edge labels
3. nodes
4. node texts

## 3. Minimum visual rules
Even if simple, your rendering must comply with:
- aligned nodes
- legible text
- visible labels
- no invisible edges

The style can be ugly.
The information must be clear.

## 4. Special cases to handle (without complexity)
### 4.1 Branching
If a node has multiple outgoing edges:
- slightly shift the exit points
- visible labels that do not overlap

No need for advanced algorithms.
A simple offset is sufficient.

### 4.2 Loops
For a self-loop:
- draw a simple curve on the side
- label close to the curve

Even if it is approximate, it is acceptable.