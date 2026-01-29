from collections import defaultdict, deque

# Rendering constants
NODE_WIDTH = 160
NODE_HEIGHT = 40
X_SPACING = 220
Y_SPACING = 120
SVG_PADDING = 40

def compute_layout(graph):
    """
    Compute a grid-based layout for a flowchart graph.

    Rules:
    - grid_y represents vertical flow
    - grid_x represents branching
    - first outgoing edge is the main path
    - secondary edges are placed laterally
    - collisions are resolved by pushing nodes downward
    """

    incoming = defaultdict(list)
    outgoing = defaultdict(list)

    for edge in graph.edges:
        outgoing[edge.src].append(edge.tgt)
        incoming[edge.tgt].append(edge.src)

    grid_pos = {}
    occupied = set()

    # Root nodes
    roots = [node.id for node in graph.nodes if node.id not in incoming]

    for i, node_id in enumerate(roots):
        grid_pos[node_id] = (i, 0)
        occupied.add((i, 0))

    queue = deque(roots)

    while queue:
        parent = queue.popleft()
        parent_x, parent_y = grid_pos[parent]
        children = outgoing.get(parent, [])

        if not children:
            continue

        # Main path (first child)
        main_child = children[0]
        if main_child not in grid_pos:
            gx = parent_x
            gy = parent_y + 1
            while (gx, gy) in occupied:
                gy += 1
            grid_pos[main_child] = (gx, gy)
            occupied.add((gx, gy))
            queue.append(main_child)

        # Secondary branches
        for offset, child in enumerate(children[1:], start=1):
            if child in grid_pos:
                continue
            gx = parent_x + offset
            gy = parent_y + 1
            while (gx, gy) in occupied:
                gy += 1
            grid_pos[child] = (gx, gy)
            occupied.add((gx, gy))
            queue.append(child)

    # Convert grid → pixels
    positions = {
        node_id: (gx * X_SPACING, gy * Y_SPACING)
        for node_id, (gx, gy) in grid_pos.items()
    }

    # --------------------------------------------------------
    # Post-pass: center parents above multiple children
    # --------------------------------------------------------
    for parent, children in outgoing.items():
        if len(children) > 1 and parent in positions:
            child_x = [positions[c][0] for c in children if c in positions]
            if child_x:
                avg_x = sum(child_x) / len(child_x)
                px, py = positions[parent]
                positions[parent] = (avg_x, py)

    return positions