from openai import OpenAI

# Configure client to point to local Ollama instance
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Required by SDK format; ignored by Ollama
)

def run_turn(prompt, messages):
    messages.append({
        "role": "user",
        "content": prompt
    })
    response = client.chat.completions.create(
        model="qwen2.5:1.5b",
        temperature=0.2,
        messages=messages
    )
    assistant_reply = response.choices[0].message.content

    print("Model Output:\n")
    print(assistant_reply)
    print("\n---")
    print(f"Usage: {response.usage.prompt_tokens} prompt tokens, "
          f"{response.usage.completion_tokens} completion tokens.")

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "You are a precise technical tutor. Respond in 2 sentences maximum."
        },
    ]
    while True:
        prompt = input("User: ").strip()
        if not prompt:
            continue
        run_turn(prompt, messages)
