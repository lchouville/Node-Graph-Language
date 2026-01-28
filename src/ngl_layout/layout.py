def compute_layout(graph):
    y = 0
    positions = {}
    for node in graph.nodes:
        positions[node.id] = (100, y)
        y += 100
    return positions