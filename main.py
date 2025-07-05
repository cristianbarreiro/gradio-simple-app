import gradio as gr

def check_answer(selected_option):
    correct_answer = "Python"

    if selected_option == correct_answer:   
        return "Correct! Python is often referred to as the snake language."
    else:
        return "Incorrect. The correct answer is Python."

interface = gr.Interface(
    fn=check_answer,
    inputs=gr.Radio(
        choices=["Java", "C++", "Python", "JavaScript"],
        label="Which programming language is known as the snake language?"
    ),
    outputs=gr.Textbox(label="Your Result")
)

interface.launch()