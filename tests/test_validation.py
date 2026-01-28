from ngl_ast.node import Node
from ngl_ast.edge import Edge
from ngl_ast.graph import Graph
from ngl_semantic.validation import validate_flowchart

def test_validation_ok():
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

    errors = validate_flowchart(graph)
    assert errors == []

def test_validation_undefined_node():
    graph = Graph(
        type="flowchart",
        name=None,
        nodes=[Node("A", "Start", 1)],
        edges=[Edge("A", "B", None, 2)]
    )

    errors = validate_flowchart(graph)
    assert len(errors) == 1
    assert "Undefined target node" in errors[0]

def test_validation_branch_without_labels():
    graph = Graph(
        type="flowchart",
        name=None,
        nodes=[
            Node("A", None, 1),
            Node("B", None, 2),
            Node("C", None, 3),
        ],
        edges=[
            Edge("A", "B", None, 4),
            Edge("A", "C", None, 5),
        ]
    )

    errors = validate_flowchart(graph)
    assert len(errors) == 2
