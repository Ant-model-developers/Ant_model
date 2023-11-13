from transformers import AutoTokenizer, pipeline
import gradio as gr
import torch
from huggingface_hub import login

login("hf_XXXX")

model = "Ant-model-developers/Ant_model"
tokenizer = AutoTokenizer.from_pretrained(model)

llama_pipeline = pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
    do_sample=False
)

SYSTEM_PROMPT = f"""<s>[INST] <<SYS>>
You are a helpful bot. Your answers are clear and concise. If you summarize a process, the summary should include, how the process starts, which steps happen afterwards and how it ends. Thereby different XOR- and AND-Gateways as well as the underlying conditions should be described before the following activities are described. Do not mention the gateways themselves. Only describe the consequences of the gateways. If you start to describe one path, describe it completely before you go on to the next path. The summary should not contain any IDs or meta-information.
<</SYS>>

"""

# Formatting function for message and history
def format_message(message: str, history: list, memory_limit: int = 3) -> str:
    """
    Formats the message and history for the Llama model.

    Parameters:
        message (str): Current message to send.
        history (list): Past conversation history.
        memory_limit (int): Limit on how many past interactions to consider.

    Returns:
        str: Formatted message string
    """
    # always keep len(history) <= memory_limit
    if len(history) > memory_limit:
        history = history[-memory_limit:]

    if len(history) == 0:
        return SYSTEM_PROMPT + f"{message} [/INST]"

    formatted_message = SYSTEM_PROMPT + f"{history[0][0]} [/INST] {history[0][1]} </s>"

    # Handle conversation history
    for user_msg, model_answer in history[1:]:
        formatted_message += f"<s>[INST] {user_msg} [/INST] {model_answer} </s>"

    # Handle the current message
    formatted_message += f"<s>[INST] {message} [/INST]"

    return formatted_message

# Generate a response from the Llama model
def get_llama_response(message: str, history: list) -> str:
    """
    Generates a conversational response from the Llama model.

    Parameters:
        message (str): User's input message.
        history (list): Past conversation history.

    Returns:
        str: Generated response from the Llama model.
    """
    query = format_message(message, history)
    response = ""

    sequences = llama_pipeline(
        query,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=10240,
    )

    generated_text = sequences[0]['generated_text']
    response = generated_text[len(query):]  # Remove the prompt from the output

    print("Chatbot:", response.strip())
    return str(response.strip())

demo = gr.ChatInterface(get_llama_response)
demo.queue().launch(share=True)
