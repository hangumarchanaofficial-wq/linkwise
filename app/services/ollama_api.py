import requests
import json

def get_llm_summary(text_content):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "gemma3:4b",
        "prompt": f"Please provide a concise and professional summary of the following content:\n\n{text_content}",
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No summary generated.")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {str(e)}"
        