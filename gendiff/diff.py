from gendiff.parser import parse_file
import json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = build_diff(file1, file2)
    return format_diff(diff, format_name)


def build_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:

        if key not in data1:
            diff[f'+ {key}'] = data2[key]

        elif key not in data2:
            diff[f'- {key}'] = data1[key]
        else:
            val1 = data1[key]
            val2 = data2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                children = build_diff(val1, val2)
                diff[f'  {key}'] = children

            elif val1 == val2:
                diff[f'  {key}'] = val1
            else:
                diff[f'- {key}'] = val1
                diff[f'+ {key}'] = val2

    return diff


def format_diff(diff, format_name, depth=1):
    indent = '    ' * (depth - 1)
    lines = ['{']

    for key, value in diff.items():
        if key.startswith('- '):
            prefix = '  - '
            real_key = key[2:]
        elif key.startswith('+ '):
            prefix = '  + '
            real_key = key[2:]
        else:
            prefix = '    '
            real_key = key.strip()

        if isinstance(value, dict):
            formatted_value = format_diff(value, format_name, depth + 1)
            
        else:
            if isinstance(value, str):

                if value == "":
                    lines.append(f"{indent}{prefix}{real_key}:")
                    continue  # saltar agregar línea al final para no repetir
                else:
                    formatted_value = value
            else:
                formatted_value = json.dumps(value)

        lines.append(f"{indent}{prefix}{real_key}: {formatted_value}")

    lines.append(indent + '}')
    return '\n'.join(lines)
