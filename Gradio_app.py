import gradio as gr

iface = gr.Interface.load('Gyimah3/Finetuned_bert','models',
examples=[["This covid is very real"],['tips:Label_0=Negative, Label_1=Neutral , Label_2=Positive']]
)
iface.launch()