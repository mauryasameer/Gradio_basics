import gradio as gr

def greet(name):
    return f"Hello {name} !"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=3, placeholder="__ Name Here __"),
    outputs="text",
)
demo.launch()