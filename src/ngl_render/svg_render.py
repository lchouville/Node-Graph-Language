# Rendering constants
NODE_WIDTH = 160
NODE_HEIGHT = 40
X_SPACING = 220
Y_SPACING = 120
SVG_PADDING = 40

def render_svg(graph, positions):
    """
    Render the graph as an SVG file.
    - Nodes are rectangles
    - Edges are centered vertically
    - Labels are offset for readability
    - SVG size is auto-computed
    """

    # Compute SVG bounds
   
    max_x = max(x for x, _ in positions.values()) + NODE_WIDTH
    max_y = max(y for _, y in positions.values()) + NODE_HEIGHT

    width = max_x + SVG_PADDING
    height = max_y + SVG_PADDING

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}">'
    ]

   
    # Draw edges first (behind nodes)
   
    for edge in graph.edges:
        sx, sy = positions[edge.src]
        tx, ty = positions[edge.tgt]

        x1 = sx + NODE_WIDTH / 2
        y1 = sy + NODE_HEIGHT /2
        x2 = tx + NODE_WIDTH / 2
        y2 = ty + NODE_HEIGHT /2

        svg.append(
            f'<line x1="{x1}" y1="{y1}" '
            f'x2="{x2}" y2="{y2}" '
            f'stroke="#000" />'
        )

        if edge.label:
            lx = (x1 + x2) / 2
            ly = (y1 + y2) / 2 - 6
            svg.append(
                f'<text x="{lx}" y="{ly}" '
                f'text-anchor="middle" '
                f'font-size="12">'
                f'{edge.label}</text>'
            )

   
    # Draw nodes
   
    for node in graph.nodes:
        x, y = positions[node.id]

        svg.append(
            f'<rect x="{x}" y="{y}" '
            f'width="{NODE_WIDTH}" height="{NODE_HEIGHT}" '
            f'fill="#f5f5f5" stroke="#000" />'
        )

        text = node.text or node.id
        svg.append(
            f'<text x="{x + NODE_WIDTH / 2}" '
            f'y="{y + NODE_HEIGHT / 2 + 4}" '
            f'text-anchor="middle" '
            f'font-size="12">'
            f'{text}</text>'
        )

    svg.append('</svg>')
    return [graph.graph_name,"\n".join(svg)]
