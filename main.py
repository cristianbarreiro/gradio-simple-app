import gradio as gr

def calculator(number1, number2, operation):
    if operation == "Addition":
        return number1 + number2
    elif operation == "Subtraction":
        return number1 - number2
    elif operation == "Multiplication":
        return number1 * number2
    elif operation == "Division":
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero is not allowed."

interface = gr.Interface(
    fn=calculator,
    inputs=[  
        gr.Number(label="First Number"),
        gr.Number(label="Second Number)"),
        gr.Dropdown(choices=["Addition", 
                             "Subtraction", 
                             "Multiplication", 
                             "Division"], label="Operation")
        ],
     outputs=gr.Number(label="Result")
)

interface.launch()