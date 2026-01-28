from typing import Optional

class Node:
    def __init__(self, p_id: str, p_text: Optional[str], p_line: int):
        self.id = p_id
        self.text = p_text
        self.line = p_line

    def __repr__(self):
        return f"Node(ID='{self.id}', text='{self.text}', line={self.line})"
