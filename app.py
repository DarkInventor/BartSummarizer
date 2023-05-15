# -*- coding: utf-8 -*-
"""Summarizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xFgoaSQnO4qWdFdHgY1ysa8udOqQp2iC
"""

# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ARTICLE = """ Gradio is an open-source Python library that provides a simple and intuitive interface for building and sharing custom machine learning models. It allows users to create interfaces for their models using a web-based GUI, which can be used to input data and get predictions.

# With Gradio, users can quickly prototype, test, and deploy their machine learning models without any web development experience. It supports a wide range of models and frameworks, including TensorFlow, PyTorch, Scikit-Learn, and more.

# Gradio also makes it easy to share your models with others by generating a shareable link that can be used to access your model's interface. Overall, Gradio is a powerful and user-friendly tool that can help make machine learning more accessible and usable for everyone.
# """
# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))

import gradio as gr

def greet(Text, max_len):
    return summarizer(ARTICLE, max_length=max_len, min_length=30, do_sample=False)

demo = gr.Interface(fn=greet, inputs=["text", gr.inputs.Slider(0, 100)], outputs=["text"])

demo.launch()
