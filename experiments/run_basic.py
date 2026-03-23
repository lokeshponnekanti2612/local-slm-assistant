from app.ollama_client import generate

model = "llama3.2"
# prompt = "explain Large Language Models"
prompt = input()
# calling Generate function to start the process
output = generate(model, prompt)

print(output)
