def format_value(value, depth=1, format='stylish'):
    
    if format == 'plain':
        if isinstance(value, dict) or isinstance(value, list):
            return '[complex value]'
        elif isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return "null"
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value)

    elif format == 'stylish':
        if isinstance(value, dict):
            indent = '    ' * depth
            lines = ['{']
            for key, val in value.items():
                lines.append(f'{indent}    {key}: {format_value(val, depth + 1, format)}')
            lines.append(f'{indent}}}')
            return '\n'.join(lines)
        elif isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return "null"
        else:
            return str(value)

    elif format == 'json':
        import json
        return json.dumps(value)

    else:
        raise ValueError(f"Formato desconocido: {format}")




