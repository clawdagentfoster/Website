from ddgs import DDGS

def search_duckduckgo(query, max_results=5):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        for r in results:
            print(f"Title: {r['title']}")
            print(f"Link: {r['href']}")
            print('---')

if __name__ == "__main__":
    search_duckduckgo("OpenClaw ACP configuration")
