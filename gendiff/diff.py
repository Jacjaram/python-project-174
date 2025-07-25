from gendiff.parser import parse_file
import json


def generate_diff(file_path1, file_path2):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    diff = {}
    agregados = set(file2.keys()) - set(file1.keys())
    eliminados = set(file1.keys()) - set(file2.keys())
    claves_comunes = set(file1.keys()) & set(file2.keys())

    for i in claves_comunes:
        if file1[i] == file2[i]:
            diff.update({i: file1[i]})
        else:
            eliminados.add(i)
            agregados.add(i)

    diff.update({f'- {k}': file1[k] for k in eliminados if k in file1})
    diff.update({f'+ {k}': file2[k] for k in agregados if k in file2})

    def clave_sin_prefijo(clave):
        return clave[2:] if clave.startswith(('+ ', '- ')) else clave

    diff_ordenado = dict(sorted(diff.items(),
                                key=lambda item: clave_sin_prefijo(item[0])))
    lineas = ["{"]
    for clave, valor in diff_ordenado.items():
        prefijo = "  "
        if clave.startswith('- '):
            prefijo = "  - "
            clave = clave[2:]
        elif clave.startswith('+ '):
            prefijo = "  + "
            clave = clave[2:]
        else:
            prefijo = "    "
        lineas.append(f"{prefijo}{clave}: {json.dumps(valor)}")
    lineas.append("}")
    return "\n".join(lineas)
