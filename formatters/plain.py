def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_plain(diff, path=''):
    lines = []
    for key, value in diff.items():
        status = value['status']
        new_path = f"{path}.{key}" if path else key

        if status == 'nested':
            lines.append(format_plain(value['children'], new_path))
        elif status == 'changed':
            lines.append(
                f"Property '{new_path}' was updated. From "
                f"{format_value(value['old_value'])} to "
                f"{format_value(value['new_value'])}"
            )
        elif status == 'added':
            lines.append(
                f"Property '{new_path}' was added with value: "
                f"{format_value(value['value'])}"
            )
        elif status == 'removed':
            lines.append(f"Property '{new_path}' was removed")

    return '\n'.join(lines)
