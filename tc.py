import gradio as gr
from pathlib import Path

# ---------- Tokenizers ----------

def count_openai(text, model="gpt-4o"):
    import tiktoken
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


def count_hf(text, model_name):
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    return len(tok.encode(text))


def count_claude_approx(text):
    return int(len(text) / 3.7)


PROVIDERS = {
    "OpenAI (GPT-4o)": lambda t: count_openai(t),
    "LLaMA 2": lambda t: count_hf(t, "meta-llama/Llama-2-7b-hf"),
    "Mistral": lambda t: count_hf(t, "mistralai/Mistral-7B-v0.1"),
    "Gemini-ish (Gemma)": lambda t: count_hf(t, "google/gemma-7b"),
    "Claude (approx)": count_claude_approx,
}

# ---------- Core logic ----------

def count_tokens(provider, text, file):
    if file is not None:
        text = Path(file.name).read_text(encoding="utf-8")

    if not text.strip():
        return "No input text."

    counter = PROVIDERS[provider]
    tokens = counter(text)

    return f"""
Provider: {provider}
Characters: {len(text):,}
Words: {len(text.split()):,}
Tokens: {tokens:,}
"""

# ---------- UI ----------

with gr.Blocks(title="LLM Token Counter") as demo:
    gr.Markdown("## LLM Token Counter\nUpload a file or paste text.")

    provider = gr.Dropdown(
        choices=list(PROVIDERS.keys()),
        value="OpenAI (GPT-4o)",
        label="LLM Provider"
    )

    file_input = gr.File(
        label="Upload .txt or .md file",
        file_types=[".txt", ".md"]
    )

    text_input = gr.Textbox(
        label="Or paste text here",
        lines=8,
        placeholder="Paste text here if not uploading a file..."
    )

    output = gr.Markdown()

    btn = gr.Button("Count Tokens")
    btn.click(
        fn=count_tokens,
        inputs=[provider, text_input, file_input],
        outputs=output
    )

demo.launch()
