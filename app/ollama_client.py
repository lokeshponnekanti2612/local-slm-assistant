import ollama

# function to call ollama API and generate content as it takes input modela nd prompt


def chat(model: str, prompt: str, stream: bool = False, options: dict = None):
    return ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt, }],
        stream=stream,
        options=options or {}
    )


def generate(model, prompt):
    response = chat(model, prompt)
    return response["message"]["content"]
