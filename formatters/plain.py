from formatters.value import format_value

def format_plain(diff, path=''):
    lines = []
    for key, value in diff.items():
        status = value['status']
        new_path = f"{path}.{key}" if path else key
                
        if status == 'nested':
            lines.append(format_plain(value['children'], new_path))
        elif status == 'changed':
            lines.append(f"Property '{new_path}' was updated. From {format_value(value['old_value'], 1, 'plain')} to {format_value(value['new_value'], 1, 'plain')}")
        # elif status == 'unchanged':
        #     print('no cambió')
        elif status == 'added':
            lines.append(f"Property '{new_path}' was added with value: {format_value(value['value'], 1, 'plain')}")
        elif status == 'removed':
            lines.append(f"Property '{new_path}' was removed")

    return '\n'.join(lines)