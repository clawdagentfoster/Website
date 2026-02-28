from playwright.sync_api import sync_playwright

def browse_example(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        print(f"Page title: {page.title()}")
        content = page.content()
        print(f"Page content length: {len(content)}")
        browser.close()

if __name__ == "__main__":
    browse_example("https://example.com")
