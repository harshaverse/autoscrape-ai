import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

HF_TOKEN = "YOUR_HF_TOKEN_HERE" # your key here
HF_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

def call_hf_llm(prompt):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    json_data = {"inputs": prompt}

    try:
        resp = requests.post(HF_URL, headers=headers, json=json_data)
        resp.raise_for_status()
        result = resp.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            print(f"[WARNING] Unexpected HF result: {result}")
            return str(result)

    except Exception as e:
        print(f"[ERROR] HF call failed: {e}")
        return "Error: LLM failed"
