from agents.tools import call_hf_llm

def run(htmls):
    print("[Agent] ExtractorAgent running...")

    extracted_data = []
    for html in htmls:
        prompt = f"Extract key AI news headlines from this HTML:\n\n{html[:2000]}"
        result = call_hf_llm(prompt)
        extracted_data.append(result)

    print(f"[Agent] ExtractorAgent extracted {len(extracted_data)} items")
    return extracted_data
