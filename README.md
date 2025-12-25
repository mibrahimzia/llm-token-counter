
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Gradio](https://img.shields.io/badge/ui-gradio-orange)
![Tokenization](https://img.shields.io/badge/LLM-token%20counter-purple)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

# LLM Token Counter (Gradio)

A simple Gradio-based tool to count tokens for different LLM providers.  
Supports file upload (`.txt`, `.md`) or pasted text, with model-specific tokenization where available.

Built for people who actually need to **plan context limits**, not guess.

````
## Features

- 📄 Upload `.txt` or `.md` files  
- ✍️ Paste raw text directly  
- 🔁 Switch between major LLM tokenizers  
- 📊 See characters, words, and token counts  
- 🧠 Honest handling of models without public tokenizers (Claude)

---

## Supported Providers

| Provider | Accuracy |
|--------|----------|
| OpenAI (GPT-4o) | ✅ Exact (`tiktoken`) |
| LLaMA 2 | ✅ Exact (HF tokenizer) |
| Mistral | ✅ Exact (HF tokenizer) |
| Gemini-ish (Gemma) | ✅ Exact (HF tokenizer) |
| Claude | ⚠️ Approximate (char-based estimate) |

> Claude does **not** publish an official tokenizer. Counts are estimates only.

---

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/llm-token-counter.git
cd llm-token-counter
````

### 2. Install dependencies

```bash
pip install gradio tiktoken transformers sentencepiece
```

> Python 3.9+ recommended.

---

## Usage

Run the app locally:

```bash
python app.py
```

Gradio will launch a local server and open the UI in your browser.

### In the UI

1. Select an **LLM provider**
2. Either:

   * Upload a `.txt` / `.md` file
   * OR paste text into the textbox
3. Click **Count Tokens**
4. View:

   * character count
   * word count
   * token count (provider-specific)

---

## Important Notes

* Token counts **will differ across providers** — this is expected.
* Large inputs (>100k tokens) may be slow depending on tokenizer and hardware.
* For Claude, always leave a **safety buffer** (10–15%) when budgeting context.

---

## Why This Exists

Context limits matter.
This tool makes token sizes visible *before* you blow up a prompt or a dev workflow.

No dashboards. No APIs. Just counts.

---

## License

MIT

```


Those are easy polish wins, but this already looks legit.
```
