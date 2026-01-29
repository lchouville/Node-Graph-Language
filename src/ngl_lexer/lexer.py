# ngl_lexer/lexer.py
import re

GRAPH_RE = re.compile(r'^\s*@([a-z][a-z0-9_]*)\s*([A-Za-z][A-Za-z0-9_]*)?\s*$')
NODE_RE = re.compile(r'^\s*([A-Za-z][A-Za-z0-9_]*)\s*\[\s*"([^"]*)"\s*\]\s*$')
EDGE_LABEL_RE = re.compile(r'^\s*([A-Za-z][A-Za-z0-9_]*)\s*--\|\s*([^|]+)\s*\|\s*([A-Za-z][A-Za-z0-9_]*)\s*$')
EDGE_RE = re.compile(r'^\s*([A-Za-z][A-Za-z0-9_]*)\s*--\s*([A-Za-z][A-Za-z0-9_]*)\s*$')
COMMENT_RE = re.compile(r'^\s*//')
EMPTY_RE = re.compile(r'^\s*$')

# transform texted graph version to a tokenized version
def tokenize(text: str):
    tokens = []
    for i, line in enumerate(text.splitlines(), start=1):
        # Detect Empty Line and Comment
        if EMPTY_RE.match(line) or COMMENT_RE.match(line):
            continue

        # Get Graph declaration
        if m := GRAPH_RE.match(line):
            tokens.append(("GRAPH", m.group(1), m.group(2), i))

        # Get Edge label and elements
        elif m := EDGE_LABEL_RE.match(line):
            tokens.append(("EDGE", m.group(1), m.group(3), m.group(2), i))
        elif m := EDGE_RE.match(line):
            tokens.append(("EDGE", m.group(1), m.group(2), None, i))

        # Get Node elements
        elif m := NODE_RE.match(line):
            tokens.append(("NODE", m.group(1), m.group(2), i))

        # Get error if not find
        else:
            raise SyntaxError(f"Invalid syntax at line {i}: {line}")

    return tokens
