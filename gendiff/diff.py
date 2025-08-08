from gendiff.parser import parse_file
from formatters.stylish import format_stylish
from formatters.plain import format_plain
from formatters.json import format_json


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
                'value': data2[key]
            }

        elif key not in data2:
            diff[key] = {
                'status': "removed",
                'value': data1[key]
            }

        else:
            val1 = data1[key]
            val2 = data2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                children = build_diff(val1, val2)
                diff[key] = {
                    'status': "nested",
                    'children': children
                }

            elif val1 == val2:
                diff[key] = {
                    'status': "unchanged",
                    'value': val1
                }
            else:
                diff[key] = {
                    'status': "changed",
                    'old_value': val1,
                    'new_value': val2
                }
    return diff


def format_diff(dict, format_name, depth=1):
    if format_name == 'stylish':
        return format_stylish(dict, depth)
    elif format_name == 'plain':
        return format_plain(dict)
    else:
        return format_json(dict)
