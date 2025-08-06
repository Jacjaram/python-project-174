from formatters.value import format_value


def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = ['{']
    for key, value in diff.items():
        status = value['status']
        if status == 'nested':
            nested = format_stylish(value['children'], depth + 1)
            lines.append(f"{indent}    {key}: {nested}")
        elif status == 'changed':
            lines.append(
                f"{indent}  - {key}: {format_value(value['old_value'], depth)}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(value['new_value'], depth)}"
            )
        elif status == 'unchanged':
            lines.append(
                f"{indent}    {key}: {format_value(value['value'], depth)}"
            )
        elif status == 'added':
            lines.append(
                f"{indent}  + {key}: {format_value(value['value'], depth)}"
            )
        elif status == 'removed':
            lines.append(
                f"{indent}  - {key}: {format_value(value['value'], depth)}"
            )
    lines.append(f"{indent}}}")
    return '\n'.join(lines)
