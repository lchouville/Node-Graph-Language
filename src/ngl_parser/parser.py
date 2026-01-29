import sys
from typing import List, Tuple, Any

from ngl_ast.node import Node
from ngl_ast.edge import Edge
from ngl_ast.graph import Graph

# parse tokens to create graph object
def parse(tokens: List[Tuple[str, Any]]) -> Graph:
    graph_type = None
    graph_name = None
    nodes = []
    edges = []


    for token in tokens:
        try:
            # Get grah details
            if token[0] == "GRAPH":
                if graph_type is not None:
                    raise ValueError(f"Multiple graph declarations at line {token[-1]}")
                graph_type, graph_name = token[1], token[2]

            # Get node details
            elif token[0] == "NODE":
                _, node_id, text, line = token
                nodes.append(Node(node_id, text, line))

            # Get token details
            elif token[0] == "EDGE":
                _, src, tgt, label, line = token
                edges.append(Edge(src, tgt, label, line))

            # error if unknow token
            else:
                raise ValueError(f"Unknown token type '{token[0]}' at line {token[-1]}")

        except Exception as e:
            print(f"Error processing token {token}: {e}", file=sys.stderr)
            raise

    if graph_type is None:
        raise ValueError("Missing graph declaration")

    return Graph(graph_type, graph_name, nodes, edges)