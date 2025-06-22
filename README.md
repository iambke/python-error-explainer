# Python Error Explainer (RAG Pipeline)

This project implements a Retrieval-Augmented Generation (RAG) pipeline designed to explain Python error messages in simple terms. It retrieves relevant explanations from a local dataset and uses a language model to generate clear, beginner-friendly responses.

## Overview

- Retrieves explanations for common Python errors from a curated text file.
- Embeds and indexes explanations using `sentence-transformers` and `FAISS`.
- Accepts user input (an error message), retrieves the most relevant context, and queries a language model (via Groq API).
- Generates a simplified explanation using a structured prompt and the retrieved context.

## Project Structure

python\_error\_explainer/
├── run.py                      # Main entry point
├── .env                        # API key configuration
├── requirements.txt            # Python dependencies
├── data/errors.txt             # List of common Python errors + explanations
└── rag/
├── embedder.py             # Handles document and query embeddings
├── retriever.py            # Uses FAISS to retrieve top relevant documents
├── prompt\_template.py      # Formats prompt for the language model
└── llm\_generator.py        # Sends prompt to the LLM and returns the response


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

2. Ensure `errors.txt` is located in the `data/` folder. This file contains error explanations used for retrieval.

## Usage

Run the program with:

```bash
python run.py
```

You will be prompted to paste a Python error message. The script will:

* Embed your input
* Retrieve the most relevant error explanations
* Generate a clear explanation using the Groq LLM API

### Example

```
Paste your Python error: IndexError: list index out of range

--- Explanation ---
This error occurs when you try to access an index in a list that doesn’t exist...
```

## Notes

* The model used for generation is `gemma2-9b-it`, queried via Groq's API.
* Retrieval is restricted to the context provided in `errors.txt`. The LLM is instructed not to hallucinate.

## License

This project is shared for educational and demonstration purposes only.
