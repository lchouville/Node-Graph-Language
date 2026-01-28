def render_svg(graph, positions):
    NODE_W = 160
    NODE_H = 40
    MARGIN = 40

    # 1. Calcul bounding box
    min_x = min(x for x, _ in positions.values())
    min_y = min(y for _, y in positions.values())
    max_x = max(x + NODE_W for x, _ in positions.values())
    max_y = max(y + NODE_H for _, y in positions.values())

    width = (max_x - min_x) + MARGIN * 2
    height = (max_y - min_y) + MARGIN * 2

    offset_x = -min_x + MARGIN
    offset_y = -min_y + MARGIN

    # 2. Début SVG
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
    ]

    # 3. Rendu edges
    for edge in graph.edges:
        x1, y1 = positions[edge.src]
        x2, y2 = positions[edge.tgt]
        svg.append(
            f'<line '
            f'x1="{x1 + 80 + offset_x}" y1="{y1 + 40 + offset_y}" '
            f'x2="{x2 + 80 + offset_x}" y2="{y2 + offset_y}" '
            f'stroke="#000"/>'
        )
        if edge.label:
            svg.append(
                f'<text '
                f'x="{(x1 + x2) // 2 + offset_x}" '
                f'y="{(y1 + y2) // 2 + offset_y}">'
                f'{edge.label}</text>'
            )

    # 4. Rendu nodes
    for node in graph.nodes:
        x, y = positions[node.id]
        x += offset_x
        y += offset_y
        svg.append(
            f'<rect x="{x}" y="{y}" '
            f'width="{NODE_W}" height="{NODE_H}" '
            f'fill="#eee" stroke="#000"/>'
        )
        svg.append(
            f'<text x="{x + 10}" y="{y + 25}">'
            f'{node.text or node.id}</text>'
        )

    svg.append('</svg>')
    return [graph.graph_name,"\n".join(svg)]
