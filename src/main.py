# main.py
import sys
from pathlib import Path
from typing import List

import ngl_pipeline.pipeline

def main(args: List[str]):
    for arg in args:
        try:
            # Use Path for better path handling
            file_path = Path("") / arg

            # print(f"Trying to open: {file_path}")
            # print(f"Absolute path: {file_path.resolve()}")
            # print(f"Exists: {file_path.exists()}")
            # print(f"Current directory: {Path.cwd()}")
            # print("---")

            # Validate file exists and has .ngl extension
            if not file_path.exists():
                print(f"Error: File '{file_path}' not found", file=sys.stderr)
                continue

            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()

            # Run through ngl_pipeline with error handling
            result = ngl_pipeline.pipeline.run(source_code)

            # Success
            output_path = (Path("")/result[0]).with_suffix(".svg")
            output_path.write_text(result[1], encoding="utf-8")

            print(f"SVG generated: {output_path}")

        except Exception as e:
            print(f"Error processing {arg}: {e}", file=sys.stderr)
            continue

    input("Press Enter to continue...")

main(sys.argv[2:])
