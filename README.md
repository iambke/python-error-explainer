# Python Error Explainer – RAG-powered Traceback Interpreter

Explains Python errors in plain English using retrieval-augmented generation (RAG) + Groq.

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline to explain Python error messages in simple terms. It retrieves relevant explanations from a local dataset and uses a language model to generate clear, beginner-friendly responses.

### Key Features

- Retrieves explanations for common Python errors from a curated text file.
- Embeds and indexes explanations using `sentence-transformers` and `FAISS`.
- Accepts full Python tracebacks as user input (multi-line supported).
- Queries Groq’s LLM (`gemma-2-9b-it`) using retrieved context only — no hallucination.
- Returns clear, human-readable error explanations.

## Project Structure

```
python_error_explainer/
├── run.py                   # Main entry point
├── .env                     # API key configuration
├── requirements.txt         # Python dependencies
├── data/
│   └── errors.txt           # Common Python errors + explanations
└── rag/
    ├── embedder.py          # Handles document and query embeddings
    ├── retriever.py         # Uses FAISS to retrieve top relevant documents
    ├── prompt_template.py   # Formats prompt for the language model
    └── llm_generator.py     # Sends prompt to the LLM and returns the response
````

## Requirements

Install all required dependencies using:

```bash
pip install -r requirements.txt
````


This project depends on:

* `faiss-cpu`
* `sentence-transformers`
* `requests`
* `python-dotenv`
* `numpy`

## Setup

1. Create a `.env` file in the root directory with the following content:

   ```
   GROQ_API_KEY=your_api_key_here
   ```

2. Ensure `errors.txt` is in the `data/` folder. This file contains 69 beginner-friendly Python error explanations formatted for retrieval.

## Usage

Run the program with:

```bash
python run.py
```


You will be prompted to paste a Python error message. The script will:

* Embed your input using `sentence-transformers`
* Retrieve the most relevant explanations using `FAISS`
* Generate a simplified explanation using the Groq LLM API

### Example

```
Paste your Python error (press Enter twice to finish):
Traceback (most recent call last):
  File "<main.py>", line 2, in <module>
KeyError: 'gender'

--- Explanation ---
This error means your program is trying to find something called "gender" inside a dictionary, but that "gender" isn't actually there...
```

## Notes

* The model used for generation is `gemma2-9b-it`, queried via Groq's API.
* Retrieval is limited to the provided `errors.txt` context to ensure factual explanations.
