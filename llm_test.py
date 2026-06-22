import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Extract JSON from this text:\n\nJenkins Job: CustomerPortal_Build\nEnvironment: UAT\nBranch: main"
        }
    ]
)

print(response["message"]["content"])