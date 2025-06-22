import requests
from bs4 import BeautifulSoup

def run(urls):
    print("[Agent] ScraperAgent running...")

    htmls = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            htmls.append(str(soup))
        except Exception as e:
            print(f"[ERROR] ScraperAgent failed for {url}: {e}")

    print(f"[Agent] ScraperAgent scraped {len(htmls)} pages")
    return htmls
