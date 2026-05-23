from playwright.sync_api import sync_playwright


def scrape_bid_detail(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(url, wait_until="networkidle")

        page.wait_for_timeout(10000)

        print("\nPAGE TITLE:")
        print(page.title())

        print("\nCURRENT URL:")
        print(page.url)

        print("\nVISIBLE TEXT:\n")

        body_text = page.locator("body").inner_text()

        print(body_text[:5000])

        input("Press Enter to close...")

        browser.close()