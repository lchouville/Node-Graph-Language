# Flowchart Semantics

## 1. Purpose

This document defines the semantic meaning of flowchart graphs written in **Node Graph Language *(NGL)***.

It describes:
- what each node type represents
- how edges are interpreted
- how a flowchart should be logically read
This document does not define syntax or validation rules.

## 2. Flowchart Concept

A flowchart represents a sequential and/or conditional process.
- Nodes represent steps
- Edges represent execution flow
- The graph is directional
- The flowchart describes a logical ordering, not an executable program


## 3. Node Semantics
### 3.1 Node Definition

A node represents a single step or stage in the flowchart.

Semantic properties:
- a node is an abstract unit of work or meaning
- the textual content of a node is descriptive
- nodes do not embed logic or behavior
The node identifier is a reference handle and has no semantic meaning by itself.

### 3.2 Node Text

The text associated with a node:
```md
    identifier["text"]
```
Semantic meaning:
- the text is a human-readable description
- it explains the purpose of the step
- it has no effect on flow or logic
If the text is omitted, the node still exists semantically but is name are the identifier.

## 4. Edge Semantics
### 4.1 Directed Flow

An edge represents a directed relationship between two nodes.
```md
A -- B
```

Semantic meaning:
- A precedes B
- the process flows from A to B
- execution or progression is conceptual, not literal
Edges do not carry conditions, labels, or metadata in v0.

### 4.2 Labeled Edges

An edge may optionally carry a label.
```md
A --|label| B
```

Semantic meaning:
- the label represents a logical condition, outcome, or transition reason
- labels are descriptive, not evaluated by the language
- labels are used to distinguish multiple outgoing paths
The language does not interpret the label content; it only preserves it.

### 4.3 Branching Semantics

When a node has multiple outgoing edges:
- the flowchart represents a choice point
- each outgoing edge represents a possible path
- labeled edges distinguish the possible outcomes
No priority or default path is implied unless explicitly expressed by structure or labeling.

### 4.4 Loop Semantics

A loop exists when a path leads back to a previously traversed node.

Example:
```md
A --|retry| A
```

Semantic meaning:
- the loop represents a conceptual repetition
- loops indicate iteration, retry, or cyclic behavior
- the language does not define termination conditions
Loops are descriptive and do not imply execution control.

## 5. Flow Interpretation Model

A flowchart is interpreted as follows:
1. Identify all nodes
2. Identify directed edges and their labels
3. Interpret edges as possible transitions between steps
4. At branching points, consider each labeled edge as a distinct path
5. Cycles represent repetition in the conceptual process
The interpretation is descriptive, not operational, and does not define execution rules.