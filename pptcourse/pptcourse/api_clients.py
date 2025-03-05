import requests
import os
from openai import OpenAI

# Load API keys from environment variables (Set in .env or your shell)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-60a0e4bd39f94846a5c710eaad56f8f5")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-60a0e4bd39f94846a5c710eaad56f8f5")


def call_deepseek(prompt: str) -> str:
    """
    Calls DeepSeek API to generate text based on a prompt.
    """
    # url = "https://api.deepseek.com/v1/completions"  # Replace with actual API URL
    # payload = {"model": "deepseek-chat", "prompt": prompt, "max_tokens": 200}
    # headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    #
    # response = requests.post(url, json=payload, headers=headers)
    #
    # if response.status_code == 200:
    #     return response.json().get("choices", [{}])[0].get("text", "").strip()
    # else:
    #     raise Exception(f"DeepSeek API error: {response.text}")
    client = OpenAI(api_key="sk-60a0e4bd39f94846a5c710eaad56f8f5", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=True
    )
    return response.choices[0].message.content

def call_openai(prompt: str) -> str:
    """
    Calls OpenAI API (GPT-4) to generate text based on a prompt.
    """
    url = "https://api.openai.com/v1/completions"
    payload = {"model": "gpt-4", "prompt": prompt, "max_tokens": 200}
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        raise Exception(f"OpenAI API error: {response.text}")