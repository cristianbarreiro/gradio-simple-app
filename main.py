import gradio as gr

def add_numbers(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn=add_numbers,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2")
    ],
    outputs=gr.Number(label="Sum"),
)

interface.launch()