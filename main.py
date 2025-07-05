import gradio as gr

def favorite_colors(selected_colors):
    correct_answer = "Python"

    if selected_colors:   
        return f"Your favorite color are: {', '.join(selected_colors)}"
    else:
        return "Incorrect. You didn't select any colors."

interface = gr.Interface(
    fn=favorite_colors,
    inputs=gr.CheckboxGroup(
        choices=["Red", "Blue", "Green", "Yellow", "Black", "White"],
        label="Select your favorite color",
    ),
    outputs=gr.Textbox(label="Your Selected Color")
)

interface.launch()