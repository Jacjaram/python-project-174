import yaml
import json
import os


def parse_file(path):
    ext = os.path.splitext(path)[1]
    with open(path) as f:
        if ext in ('.json',):
            return json.load(f)
        elif ext in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
