# Flowchart Grammar

## 1. Grammar objectives

Define the formal syntax of flowchart graphs on the **Node Graph Language *(NGL)***:
- Authorised structure `.ngl`
- Elements key
- Declaration order

## 2. General principles

- The grammar is declarative.
- The order of declarations is arbitrary (unless otherwise specified).
- The language is case-sensitive.
- Identifiers are stable and unique.
- No implicit behavior is allowed.

## 3. Overall structure of an .ngl file
An .ngl file contains exactly one graph.

```md
    @flowchart <ChartName>
    <declarations>
```
- `ChartName` is optional; if it is not specified, it will take the name of the file.
- `declaration` is the declaration of the chart elements.

## 4. Reserved keywords

## 5. Identifier
### 5.1 Rules
An identifier:
- begins with a letter (a-z, A-Z)
- can contain `letters`, `numbers`, and `_`
- does not contain any spaces

## 6. Node Declaration
### 6.1 Syntax
```md
    <identifier>["<text>"]
```
### 6.2 Syntax Constraints
- `<identifier>` must be unique in the graph

## 7. edge Declaration
### 7.1 Syntax
```md
    <SourceNode> -- <TargetNode>
```
with label
```md
    <SourceNode> --|"<text>"| <TargetNode>
```
### 8.2 Contraintes syntaxiques
- `--` is mandatory
- `<SourceNode>` and `<TargetNode>` are the node identifiers
- an edge is directional

## 9. Declaration Orders
Within a flowchart:
- node and edge declarations can be mixed
- no order is imposed by the grammar

## 10. Comments
### 10.1 Syntaxe
```md
    // this is a comment
```

### Exemple of flowchart

```md
@flowchart CompilerFlow
// Nodes declarations
parsing["Parsing step"]
validation["Validation Step"]
normalisation["Nomalisation Step"]
rendering["Renering Step"]
export["Exporting Step"]

// edges declarations
parsing -- validation
validation -- normalisation
normalisation -- rendering
rendering -- export
```