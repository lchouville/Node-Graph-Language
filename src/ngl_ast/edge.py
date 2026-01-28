from typing import Optional

class Edge:
    def __init__(self, src: str, tgt: str, label: Optional[str], line: int):
        self.src = src
        self.tgt = tgt
        self.label = label
        self.line = line

    def __repr__(self):
        return f"Edge(src='{self.src}', tgt='{self.tgt}', label='{self.label}', line={self.line})"
