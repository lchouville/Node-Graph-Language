from ngl_ast.node import Node
from ngl_ast.edge import Edge
from ngl_ast.graph import Graph
from ngl_render.svg_render import render_svg

def test_render_svg_basic():
    graph = Graph(
        type="flowchart",
        name="Test",
        nodes=[
            Node("A", "Start", 1),
            Node("B", "End", 2),
        ],
        edges=[
            Edge("A", "B", None, 3)
        ]
    )

    positions = {
        "A": (0, 0),
        "B": (0, 100)
    }

    svg = render_svg(graph, positions)

    assert svg.startswith("<svg")
    assert "</svg>" in svg
    assert "<rect" in svg
    assert "<line" in svg
    assert 'width="' in svg
    assert 'height="' in svg
