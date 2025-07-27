### Hexlet tests and linter status:
[![Actions Status](https://github.com/Jacjaram/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Jacjaram/python-project-174/actions)

[![Maintainability](https://qlty.sh/gh/Jacjaram/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/Jacjaram/projects/python-project-174)

[![Code Coverage](https://qlty.sh/gh/Jacjaram/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/Jacjaram/projects/python-project-174)

# gendiff

**gendiff** es una herramienta de línea de comandos y biblioteca en Python que permite comparar archivos JSON y mostrar sus diferencias de manera legible.

---

## 📦 Instalación

```bash
git clone https://github.com/Jacjaram/python-project-174.git
cd python-project-174
poetry install# trigger

# 📽 Ejemplo de uso

[![asciicast](https://asciinema.org/a/96TApEsGfutmM54f7i9T1VkzM.svg)](https://asciinema.org/a/96TApEsGfutmM54f7i9T1VkzM)

```bash
$ gendiff file1.json file2.json
{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}

