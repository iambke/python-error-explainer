import os
from dotenv import load_dotenv
from rag.embedder import Embedder
from rag.retriever import Retriever
from rag.prompt_template import format_prompt
from rag.llm_generator import generate_answer

load_dotenv()

# Load error explanations
with open("data/errors.txt", "r", encoding="utf-8") as f:
    raw = f.read().strip().split("\n\n")
    docs = [block.strip() for block in raw if block.strip()]

print(f"✅ Loaded {len(docs)} error explanations")

# Embed
embedder = Embedder()
doc_embeddings = embedder.embed_documents(docs)
retriever = Retriever(doc_embeddings)

# Ask user
print("Paste your Python error (press Enter twice to finish):")
lines = []
while True:
    try:
        line = input()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break  # Handles Ctrl+D / end-of-input in some environments

query = "\n".join(lines)

query_embedding = embedder.embed_documents([query])[0]
top_k_indices = retriever.retrieve(query_embedding)
context = [docs[i] for i in top_k_indices]

prompt = format_prompt(context, query)
print("\n--- Explanation ---")
print(generate_answer(prompt))