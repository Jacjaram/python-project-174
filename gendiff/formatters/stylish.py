def format_value(value, depth=1):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for key, val in value.items():
            lines.append(f'{indent}    {key}: {format_value(val, depth + 1)}')
        lines.append(f'{indent}}}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = ['{']

    def sep(value_str):
        if value_str == "":
            return ":"
        return ": "
    for key, value in diff.items():
        status = value['status']
        if status == 'nested':
            nested = format_stylish(value['children'], depth + 1)
            lines.append(f"{indent}    {key}: {nested}")
        elif status == 'changed':
            old_val = format_value(value['old_value'], depth)
            new_val = format_value(value['new_value'], depth)
            lines.append(f"{indent}  - {key}{sep(old_val)}{old_val}")
            lines.append(f"{indent}  + {key}{sep(new_val)}{new_val}")
        elif status == 'unchanged':
            val = format_value(value['value'], depth)
            lines.append(f"{indent}    {key}{sep(val)}{val}")
        elif status == 'added':
            val = format_value(value['value'], depth)
            lines.append(f"{indent}  + {key}{sep(val)}{val}")
        elif status == 'removed':
            val = format_value(value['value'], depth)
            lines.append(f"{indent}  - {key}{sep(val)}{val}")
    lines.append(f"{indent}}}")
    return '\n'.join(lines)
