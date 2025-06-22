def format_prompt(context_list, query):
    context = "\n".join(context_list)
    return f"""
You are a Python tutor. A student has pasted a Python error message.
Your job is to explain what the error means in very simple and clear language.

Use the context provided, and explain the error in a way that a beginner would understand.
Don't give code examples unless they are extremely necessary.

Only use information from the context. If you're unsure, say "I'm not sure about that one."

Context:
{context}

Error Message:
{query}

Explain it simply:
""".strip()
