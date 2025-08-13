# gendiff

[![Actions Status](https://github.com/Jacjaram/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Jacjaram/python-project-174/actions)
[![Maintainability](https://qlty.sh/gh/Jacjaram/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/Jacjaram/projects/python-project-174)
[![Code Coverage](https://qlty.sh/gh/Jacjaram/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/Jacjaram/projects/python-project-174)

**gendiff** es una herramienta de línea de comandos y biblioteca en Python que permite comparar archivos **JSON** o **YAML** y mostrar sus diferencias en varios formatos:  
- `stylish` (por defecto, jerárquico y legible)  
- `plain` (descripción en texto plano)  
- `json` (estructurado para procesar programáticamente)  

---

## 📦 Instalación

Clona el repositorio y usa **Poetry** para instalar las dependencias:

```bash
git clone https://github.com/Jacjaram/python-project-174.git
cd python-project-174
poetry install
```

Si quieres instalar el comando `gendiff` en tu sistema:

```bash
poetry build
pip install dist/*.whl
```

---

## 🚀 Uso en la terminal (CLI)

La sintaxis básica es:

```bash
gendiff [opciones] <archivo1> <archivo2>
```

### Ejemplo formato `stylish` (por defecto):

[![asciicast](https://asciinema.org/a/96TApEsGfutmM54f7i9T1VkzM.svg)](https://asciinema.org/a/96TApEsGfutmM54f7i9T1VkzM)

```bash
gendiff file1.json file2.json
```

Salida:

```
{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

---

### Ejemplo formato `plain`:

[![asciicast](https://asciinema.org/a/GraIsrAgWEcUgf9C7yj3Bn1yn.svg)](https://asciinema.org/a/GraIsrAgWEcUgf9C7yj3Bn1yn)

```bash
gendiff --format plain file1.yaml file2.yaml
```

Salida:

```
Property 'follow' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

---

### Ejemplo formato `json`:

[![asciicast](https://asciinema.org/a/Ek14T2vHoNMO7HFA5g8xgO2De.svg)](https://asciinema.org/a/Ek14T2vHoNMO7HFA5g8xgO2De)

```bash
gendiff --format json file1.json file2.json
```

Salida:

```json
[
  {"key": "follow", "type": "removed", "value": false},
  {"key": "timeout", "type": "changed", "oldValue": 50, "newValue": 20},
  {"key": "verbose", "type": "added", "value": true}
]
```

