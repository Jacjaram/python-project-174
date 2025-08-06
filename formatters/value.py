def format_value(value, depth):
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
    elif value == "":
        return ""  # esto imprimirá `key:` como se espera
    else:
        return str(value)



