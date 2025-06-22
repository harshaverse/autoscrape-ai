def run(theme):
    print("[Agent] DiscoveryAgent running...")

    urls = [
        "https://venturebeat.com/category/ai/",
        "https://techcrunch.com/tag/artificial-intelligence/",
        "https://www.analyticsvidhya.com/blog/category/artificial-intelligence/",
    ]

    print(f"[Agent] DiscoveryAgent found {len(urls)} URLs")
    return urls
