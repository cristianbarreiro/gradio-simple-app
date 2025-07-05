# 🗣️ Texto a Voz con Gradio + Edge TTS

Este proyecto utiliza **Gradio** y **edge-tts** (el motor de texto a voz de Microsoft Edge) para crear una interfaz web que convierte texto en voz, con soporte para múltiples idiomas y voces.

## 🚀 Requisitos

- Python 3.7 o superior
- Conexión a internet (edge-tts requiere conectarse al servicio de voz de Microsoft)
- pip

## ⚙️ Instalación

1. Crear y activar un entorno virtual (opcional pero recomendado):

### En Windows

```bash
python -m venv venv
.env\Scriptsctivate
```

### En macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar las dependencias:

```bash
pip install gradio edge-tts
```

## 💡 Cómo usar

1. Crear un archivo `app.py` con el siguiente contenido:

```python
import gradio as gr
import asyncio
import edge_tts
import uuid

async def generar_audio(texto):
    nombre_archivo = f"voz_{uuid.uuid4()}.mp3"
    comunicador = edge_tts.Communicate(text=texto, voice="es-MX-DaliaNeural")
    await comunicador.save(nombre_archivo)
    return nombre_archivo

def texto_a_voz(texto):
    return asyncio.run(generar_audio(texto))

gr.Interface(
    fn=texto_a_voz,
    inputs=gr.Textbox(label="Texto para convertir a voz"),
    outputs=gr.Audio(label="Audio generado"),
    title="Texto a Voz con Edge TTS",
    description="Convierte texto a voz utilizando Microsoft Edge TTS (requiere conexión a internet)"
).launch()
```

2. Ejecutar la aplicación:

```bash
python app.py
```

3. Escribir el texto en la interfaz y escuchar la voz generada.

## 🌎 Cambiar la voz

Podés cambiar la voz en esta línea:

```python
voice="es-MX-DaliaNeural"
```

Algunas voces recomendadas:

| Voz | Descripción |
|-----|-------------|
| `es-MX-DaliaNeural` | Mujer mexicana |
| `es-ES-ElviraNeural` | Mujer española |
| `en-US-JennyNeural` | Mujer estadounidense |
| `en-GB-RyanNeural` | Hombre británico |

Lista completa de voces disponibles: https://github.com/rany2/edge-tts#voices

## 🧼 Desactivar el entorno virtual

```bash
deactivate
```

## 📁 .gitignore recomendado

```gitignore
venv/
__pycache__/
*.pyc
voz_*.mp3
```

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y personales.
