import gradio as gr

def start(name, morning_is, temp):
            msg = "Good morning" if morning_is else "Good evening"
            greeting = "%s %s. It is %s degrees today" % (msg, name, temp)
            cels = (temp - 32) * 5 / 9
            return greeting, round(cels, 2)

face = gr.Interface(fn=start, inputs=["text", "checkbox",
                                     gr.inputs.Slider(0, 100)],
                                    outputs=["text", "number"])
face.launch()