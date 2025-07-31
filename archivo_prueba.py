import json

with open("tests/fixtures/file1.json") as f:
    datos1 = json.load(f)

with open("tests/fixtures/file2.json") as y:
    datos2 = json.load(y)

# for key, value in datos1.items():
# # for key in (sorted((set(datos1.keys())|set(datos2.keys())))):
#     if isinstance(value, dict):
#         print(key)

def recorrer_json(nodo, nivel=0):
    indent = "    " * nivel
    if isinstance(nodo, dict):
        for clave, valor in nodo.items():
            if isinstance(valor, dict):
                print(f"{indent}{clave}:")
                recorrer_json(valor, nivel + 1)
            else:
                print(f"{indent}{clave}: {valor}")
    else:
        print(f"{indent}{nodo}")

# Usar la función con datos1
recorrer_json(datos1)
