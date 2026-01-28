from ngl_lexer.lexer import tokenize

def test_tokenize_flowchart_decl():
    src = "@flowchart MyChart"
    tokens = tokenize(src)
    assert tokens == [("GRAPH", "flowchart", "MyChart", 1)]

def test_tokenize_node():
    src = 'node1["Hello"]'
    tokens = tokenize(src)
    assert tokens == [("NODE", "node1", "Hello", 1)]

def test_tokenize_edge():
    src = "A -- B"
    tokens = tokenize(src)
    assert tokens == [("EDGE", "A", "B", None, 1)]

def test_tokenize_edge_with_label():
    src = "A --|yes| B"
    tokens = tokenize(src)
    assert tokens == [("EDGE", "A", "B", "yes", 1)]

def test_tokenize_ignore_comment_and_empty():
    src = """
    // comment
    A -- B
    """
    tokens = tokenize(src)
    assert len(tokens) == 1
    assert tokens[0][0] == "EDGE"

def test_tokenize_invalid_line():
    src = "A --- B"
    try:
        tokenize(src)
        assert False
    except SyntaxError:
        assert True
