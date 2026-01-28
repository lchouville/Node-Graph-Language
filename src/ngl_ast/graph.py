from typing import List
from ngl_ast.node import Node
from ngl_ast.edge import Edge

class Graph:
    def __init__(self, graph_type: str, graph_name: str, nodes: List[Node], edges: List[Edge]):
        self.graph_type = graph_type
        self.graph_name = graph_name
        self.nodes = nodes
        self.edges = edges

    def __repr__(self):
        return f"Graph(type='{self.graph_type}', name='{self.graph_name}', nbNodes={len(self.nodes)}, nbEdges={len(self.edges)})"

    def __str__(self):
        node_str = "\n".join([f"        {node}" for node in self.nodes])
        edge_str = "\n".join([f"        {edge}" for edge in self.edges])

        return (
            f"Graph(type='{self.graph_type}',\n"
            f"  name='{self.graph_name}',\n"
            f"  nbNodes={len(self.nodes)},\n"
            f"  nbEdges={len(self.edges)},\n"
            f"  nodes=[\n{node_str}\n      ],\n"
            f"  edges=[\n{edge_str}\n      ])"
        )