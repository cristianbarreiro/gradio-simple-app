import gradio as gr

def square_number(number):
    return number ** 2

interface = gr.Interface(
    fn=square_number,
    inputs=gr.Slider(minimum=0, maximum=100, step=1, label="Input Number"),
     outputs=gr.Number(label="Result (Square of Input Number)"),
)

interface.launch()