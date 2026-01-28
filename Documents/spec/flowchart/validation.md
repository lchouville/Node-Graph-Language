# Flowchart Validation Rules

## 1. Purpose

This document defines the validation rules for flowchart graphs written in **Node Graph Language *(NGL)***.

Validation rules determine:
- what is invalid
- what is ambiguous
- what is allowed but discouraged
This document does not define syntax or rendering behavior.

## 2. Validation Levels

Validation results are classified into three levels:
- Error → the graph is invalid and must not be rendered
- Warning → the graph is valid but ambiguous or unclear
- Info → stylistic or best-practice notice *(optional)*

## 3. Graph-Level Rules
### 3.1 Single Graph Rule

Error
- a file must contain exactly one @flowchart declaration
- multiple flowcharts in the same file are forbidden

### 3.2 Empty Graph

Error
- a flowchart with no node declarations is invalid

## 4. Node Validation Rules
### 4.1 Unique Node Identifiers

Error
- each node identifier must be unique within the graph

### 4.2 Node Without Edges

Warning

- a node with no incoming and no outgoing edges is considered isolated
- isolated nodes reduce graph readability

### 4.3 Node Without Text

Info
- nodes without text are allowed
- providing a descriptive text is recommended for clarity

## 5. Edge Validation Rules
### 5.1 Edge References

Error
- an edge must reference existing nodes
- referencing an undefined node is invalid

### 5.2 Duplicate Edges

Warning
- multiple identical edges between the same nodes are discouraged

### 5.3 Direction Consistency

Info
- edges are directional and should reflect logical progression
- bidirectional edges should be explicitly documented using labels

## 6. Label Validation Rules
### 6.1 Label Syntax

Error
- an edge label must not be empty
- whitespace-only labels are invalid

### 6.2 Multiple Outgoing Edges

Error
- if a node has more than one outgoing edge, all outgoing edges must be labeled

Rationale:
- unlabeled branches are ambiguous and unreadable

### 6.3 Duplicate Labels

Error
- two outgoing edges from the same node must not share the same label

Rationale:
- labels are used to distinguish paths

### 6.4 Single Outgoing Edge with Label

Info
- labeling a single outgoing edge is allowed
- it may improve clarity but is not required

## 7. Loop Validation Rules
### 7.1 Self-Loops

Warning
- self-loops (A --|label| A) are allowed
- a label is strongly recommended to explain the loop purpose

### 7.2 Cyclic Paths

Info
- cycles involving multiple nodes are allowed
- the language does not attempt to detect infinite loops

## 8. Entry and Exit Heuristics (Non-Blocking)

These rules are heuristic and do not invalidate the graph.

### 8.1 Entry Nodes

Warning
- nodes with no incoming edges may represent entry points
- multiple entry nodes should be documented clearly

### 8.2 Exit Nodes

Warning
- nodes with no outgoing edges may represent terminal steps
- multiple exit nodes are allowed but may reduce clarity

## 9. Rendering Preconditions

A graph must not be rendered if:
- it contains validation errors
- edge references are broken
- branching rules are violated
Graphs with warnings may be rendered with visual indicators.

## 10. Stability Rule

Any change that alters validation severity or logic requires a minor or major version update, depending on compatibility.

## 11. Implementation Notes
This section provides implementation guidance for applying the validation rules to the internal AST.
It is informative only and does not define language behavior.

### 11.1 Validation Input

Validation operates on the following AST structures:
- Graph
  - nodes: list of Node
  - edges: list of Edge

Where:
- Node: { id, text }
- Edge: { from, to, label }

### 11.2 Rule Application Mapping
#### Unique Node Identifiers ([4.1](#41-unique-node-identifiers))
- collect all `Node.id`
- if duplicates are found → **Error**

#### Edge References ([5.1](#51-edge-references))
- for each edge:
  - `edge.from` must match an existing `Node.id`
  - `edge.to` must match an existing `Node.id`
- otherwise → **Error**

#### Multiple Outgoing Edges ([6.2](#62-multiple-outgoing-edges))
- group edges by `edge.from`
- if a group contains more than one edge:
  - every edge in the group must have a non-null `label`
- otherwise → **Error**

#### Duplicate Labels ([6.3](#63-duplicate-labels))
- for each node source:
  - collect labels of outgoing edges
  - duplicated labels → **Error**

#### Isolated Nodes ([4.2](#42-node-without-edges))
- a node with:
  - no incoming edges
  - and no outgoing edges
- produces a Warning

#### Self-Loops Without Label ([7.1](#71-self-loops))
- if `edge.from === edge.to`:
  - and `label` is null → **Warning**

### 11.3 Validation Order
1. structural errors (nodes, references)
2. branching and label rules
3. loop-related rules
4. heuristic warnings

If any Error is produced, rendering must be aborted. 