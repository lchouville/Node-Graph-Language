from ngl_layout.layout import compute_layout
from ngl_lexer.lexer import tokenize
from ngl_parser.parser import parse
from ngl_render.svg_render import render_svg
from ngl_semantic.validation import validate_flowchart


def run(input_text):
    # Lexer
    tokens = tokenize(input_text)
    # Parser
    graph = parse(tokens)
    # Validation
    validation_errors =[]
    match graph.graph_type:
        case "flowchart":
            validation_errors = validate_flowchart(graph)

    if len(validation_errors) != 0:
        raise ValueError("Some errors occurred", validation_errors)

    # Layout
    positions = compute_layout(graph)

    # Render
    return render_svg(graph, positions)