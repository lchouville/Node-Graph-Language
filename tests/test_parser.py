from ngl_parser.parser import parse

def test_parse_simple_graph():
    tokens = [
        ("GRAPH", "flowchart", "Test", 1),
        ("NODE", "A", "Start", 2),
        ("NODE", "B", "End", 3),
        ("EDGE", "A", "B", None, 4),
    ]

    graph = parse(tokens)

    assert graph.type == "flowchart"
    assert graph.name == "Test"
    assert len(graph.nodes) == 2
    assert len(graph.edges) == 1
    assert graph.edges[0].source == "A"
    assert graph.edges[0].target == "B"

def test_parse_missing_graph_decl():
    tokens = [
        ("NODE", "A", "Start", 1)
    ]

    try:
        parse(tokens)
        assert False
    except ValueError:
        assert True
