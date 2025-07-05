import pyttsx3
import gradio as gr
import tempfile
import os

# Inicializar motor pyttsx3
engine = pyttsx3.init()

def texto_a_voz(texto):
    # Crear archivo temporal para guardar el audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        ruta_audio = f.name
    # Guardar voz en archivo
    engine.save_to_file(texto, ruta_audio)
    engine.runAndWait()
    return ruta_audio

iface = gr.Interface(
    fn=texto_a_voz,
    inputs=gr.Textbox(label="Escribí el texto para convertir a voz"),
    outputs=gr.Audio(label="Audio generado"),
    title="Texto a Voz con pyttsx3 y Gradio",
    description="Convierte texto a voz offline con pyttsx3."
)

iface.launch()
