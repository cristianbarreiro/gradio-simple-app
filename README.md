# 🐍 Proyecto Python + Gradio

Este repositorio contiene un ejemplo básico de cómo crear una aplicación web interactiva utilizando [Gradio](https://gradio.app/) y Python. Gradio permite construir interfaces gráficas para funciones de Python en solo unas pocas líneas de código.

## ✅ Requisitos previos

Antes de comenzar, asegurate de tener instalado:

- Python 3.8 o superior
```bash
python --version
```

- pip (el gestor de paquetes de Python)
```bash
pip --version
```

## ⚙️ Activar Python, crear entorno virtual e instalar Gradio

### 1. Crear un entorno virtual

```bash
python -m venv venv
```

Esto crea una carpeta `venv/` con un entorno Python aislado.

### 2. Activar el entorno virtual

- En Windows (CMD o PowerShell):

```bash
.env\Scriptsctivate
```

- En macOS / Linux:

```bash
source venv/bin/activate
```

Cuando el entorno esté activo, verás algo como `(venv)` al inicio de tu línea de comandos.

### 3. Instalar Gradio

Con el entorno activado, ejecutá:

```bash
pip install gradio
```

También podés crear un archivo `requirements.txt` con este contenido:

```text
gradio
```

Y luego instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar tu aplicación

Si tu archivo principal se llama `app.py`, ejecutalo con:

```bash
python app.py
```

Esto abrirá una interfaz web en tu navegador en la siguiente dirección:

```
http://127.0.0.1:7860
```

## 🧪 Ejemplo básico

Creá un archivo llamado `app.py` y pegá el siguiente código:

```python
import gradio as gr

def saludar(nombre):
    return f"Hola, {nombre}!"

gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text",
    title="Hola con Gradio",
    description="Una app básica que saluda al usuario."
).launch()
```

## 🌍 Compartir tu app públicamente

Si querés compartir tu aplicación con otras personas mediante un enlace público, agregá el parámetro `share=True`:

```python
gr.Interface(...).launch(share=True)
```

Esto generará una URL pública temporal que podés enviar a otros para probar tu app.

## 🔚 Desactivar el entorno virtual

Cuando termines de trabajar, podés desactivar el entorno con:

```bash
deactivate
```

## 🧼 Limpieza (opcional)

Para borrar el entorno virtual:

- En macOS / Linux:

```bash
rm -rf venv/
```

- En Windows:

```bash
rmdir /s /q venv
```

### 2. Crear .gitignore

Archivo `.gitignore` recomendado:

```gitignore
venv/
__pycache__/
*.pyc
```
