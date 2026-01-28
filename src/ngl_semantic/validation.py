def validate_flowchart(graph):
    errors = []
    node_ids = {n.id for n in graph.nodes}

    if not graph.nodes:
        errors.append("Flowchart must contain at least one node")

    for edge in graph.edges:
        if edge.src not in node_ids:
            errors.append(f"Undefined source node '{edge.src}' at line {edge.line}")
        if edge.tgt not in node_ids:
            errors.append(f"Undefined target node '{edge.tgt}' at line {edge.line}")

    outgoing = {}
    for edge in graph.edges:
        outgoing.setdefault(edge.src, []).append(edge)

    for src, edges in outgoing.items():
        if len(edges) > 1:
            for e in edges:
                if not e.label:
                    errors.append(f"Missing label on branching edge at line {e.line}")

    return errors
