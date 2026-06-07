## in cmd type ollama run llama3
from ollama import chat

question=input("Ask a question      ")

client=chat(
    
    model="llama3",
    messages=[
        {
            "role":"user",
            "content":question
        }
    ]
)
print(client["message"]["content"])