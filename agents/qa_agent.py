def run(df):
    print("[Agent] QAAgent running...")

    # Example: remove duplicates
    df = df.drop_duplicates(subset=["headline"])

    print(f"[Agent] QAAgent final DataFrame has {len(df)} rows")
    return df
