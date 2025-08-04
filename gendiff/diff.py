from hmac import new
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
            diff[key] = {
                'status': "added",
                'value' : data2[key]
            }
            

        elif key not in data2:
            diff[key] = {
                'status' : "removed",
                'value' : data1[key]
            }

        else:
            val1 = data1[key]
            val2 = data2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                children = build_diff(val1, val2)                
                diff[key]= {
                    'status' : "nested",
                    'children' : children
                }

            elif val1 == val2:
                diff[key] = {
                'status' : "unchanged",
                'value' : val1
            }
            else:
                diff[key] = {
                'status' : "changed",
                'old_value' : val1,
                'new_value' : val2
            }
    return diff

    
def format_diff(dict, format_name, depth=1):
    indent = '    ' * (depth - 1)
    lines = ['{']
    if format_name == 'stylish':
        for key, value in dict.items():
            if value['status'] == 'nested':
                nested = format_diff(value['children'], format_name, depth + 1)
                lines.append(f"{indent}    {key}: {nested}")
            elif value['status'] == 'changed':
                lines.append(f"{indent}  - {key}: {format_value(value['old_value'], depth)}")
                lines.append(f"{indent}  + {key}: {format_value(value['new_value'], depth)}")
            elif value['status'] == 'unchanged':
                lines.append(f"{indent}    {key}: {format_value(value['value'], depth)}")
            elif value['status'] == 'added':
                lines.append(f"{indent}  + {key}: {format_value(value['value'], depth)}")
            else:
                lines.append(f"{indent}  - {key}: {format_value(value['value'], depth)}")  
        return '\n'.join(lines) + '\n' + indent + '}'
    else:
        return json.dumps(dict, indent=4)


def format_value(value, depth):
    indent = '    ' * depth

    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()

    return str(value)

    

    #         if key.startswith('- '):
    #             prefix = '  - '
    #             real_key = key[2:]
    #         elif key.startswith('+ '):
    #             prefix = '  + '
    #             real_key = key[2:]
    #         else:
    #             prefix = '    '
    #             real_key = key.strip()

    #         if isinstance(value, dict):
    #             formatted_value = format_diff(value, format_name, depth + 1)
                
    #         else:
    #             if isinstance(value, str):

    #                 if value == "":
    #                     lines.append(f"{indent}{prefix}{real_key}:")
    #                     continue  # saltar agregar línea al final para no repetir
    #                 else:
    #                     formatted_value = value
    #             else:
    #                 formatted_value = json.dumps(value)

    #         lines.append(f"{indent}{prefix}{real_key}: {formatted_value}")

    #     lines.append(indent + '}')
    #     return '\n'.join(lines)
    # else:
    #     return dict
