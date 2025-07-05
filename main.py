import gradio as gr

def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    # resized_image.save("resized_image.png")
    return resized_image

interface = gr.Interface(
    fn=resize_image,
    inputs= [
        gr.Image(type="pil", label="Upload an Image"),
        gr.Number(label="Width(px)"),
        gr.Number(label="Height(px)")
    ],
     outputs=gr.Image(label="World Count Result")
)

interface.launch()