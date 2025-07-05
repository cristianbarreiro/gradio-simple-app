import gradio as gr
import asyncio
import edge_tts
import uuid
import os

async def generar_audio(texto):
    nombre_archivo = f"voz_{uuid.uuid4()}.mp3"
    comunicador = edge_tts.Communicate(text=texto, voice="es-MX-DaliaNeural")  # Cambia la voz aquí si querés
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
