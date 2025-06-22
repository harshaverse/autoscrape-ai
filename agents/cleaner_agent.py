import pandas as pd

def run(extracted_data):
    print("[Agent] CleanerAgent running...")

    cleaned = []
    for item in extracted_data:
        # Simple split by newlines for demo
        lines = item.split("\n")
        for line in lines:
            if line.strip():
                cleaned.append({"headline": line.strip()})

    df = pd.DataFrame(cleaned)
    print(f"[Agent] CleanerAgent created DataFrame with {len(df)} rows")
    return df
