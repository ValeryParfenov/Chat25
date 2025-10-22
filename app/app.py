import gradio as gr
import time

from model import generate_response, _load_model


def chat_gradio(message, history):
    """
    This is the main function that powers the Gradio chat interface.
    It takes a user message and the chat history, then returns the model's response.
    """
    full_response = generate_response(message)
    new_text = full_response[len(message):].strip()

    response = ""
    for char in new_text:
        response += char
        time.sleep(0.02)
        yield response


if __name__ == '__main__':
    _load_model()

    gr.ChatInterface(
        fn=chat_gradio,
        title="GPT-2 Chatbot",
        description="A simple web interface for a GPT-2 model. Enter your message and get a response.",
        theme="soft",
        examples=["Hello, how are you?", "What is the capital of France?", "Write a short poem about the sea."]
    ).launch(server_name="0.0.0.0", server_port=7860)
