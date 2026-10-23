"""Execute the teaching notebook's Python cells and retain real stdout outputs.

This minimal runner is for this synchronous notebook. For interactive use, open
it with a Jupyter kernel from the repository virtual environment.
"""
import contextlib
import io
import json
from pathlib import Path

path = Path(__file__).with_name('svu-kjsce-laboratory.ipynb')
notebook = json.loads(path.read_text())
namespace = {'__name__': '__main__'}
count = 0
for cell in notebook['cells']:
    if cell['cell_type'] != 'code':
        continue
    count += 1
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(''.join(cell['source']), f'{path.name}:cell-{count}', 'exec'), namespace)
    cell['execution_count'] = count
    cell['outputs'] = [{'output_type': 'stream', 'name': 'stdout', 'text': output.getvalue().splitlines(True)}] if output.getvalue() else []
path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + '\n')
print(f'Executed {count} notebook cells successfully.')
