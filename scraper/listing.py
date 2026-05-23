from playwright.sync_api import sync_playwright

BASE_URL = "https://bidplus.gem.gov.in/all-bids"


def extract_value(text, key):
    try:
        start = text.index(key) + len(key)
        remaining = text[start:].strip()
        return remaining.split("\n")[0].strip()
    except:
        return ""


def extract_department(text):
    try:
        start = text.index("Department Name And Address:")
        remaining = text[start:].split("Start Date:")[0]
        lines = remaining.split("\n")

        cleaned = []

        for line in lines:
            line = line.strip()

            if (
                line
                and "Department Name And Address:" not in line
            ):
                cleaned.append(line)

        return " | ".join(cleaned)

    except:
        return ""


def scrape_listings(limit=20):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(BASE_URL, wait_until="networkidle")

        page.wait_for_timeout(8000)

        current_page = 1

        while len(results) < limit:
            print(f"Scraping Page {current_page}")

            cards = page.locator(".card")

            count = cards.count()

            for i in range(count):
                try:
                    card = cards.nth(i)

                    text = card.inner_text()

                    bid_no = extract_value(text, "Bid No.:")
                    ra_no = extract_value(text, "RA NO:")

                    item = {
                        "bid_no": bid_no,
                        "ra_no": ra_no,
                        "items": extract_value(text, "Items:"),
                        "quantity": extract_value(
                            text,
                            "Quantity:"
                        ),
                        "department": extract_department(text),
                        "start_date": extract_value(
                            text,
                            "Start Date:"
                        ),
                        "end_date": extract_value(
                            text,
                            "End Date:"
                        ),
                        "detail_link": ""
                    }

                    links = card.locator("a")

                    for j in range(links.count()):
                        href = links.nth(j).get_attribute(
                            "href"
                        )

                        link_text = (
                            links
                            .nth(j)
                            .inner_text()
                            .strip()
                        )

                        if (
                            "GEM/" in link_text
                            and "/B/" in link_text
                        ):
                            bid_no = link_text

                        if (
                            "GEM/" in link_text
                            and "/R/" in link_text
                        ):
                            ra_no = link_text

                        if (
                            href
                            and "showbidDocument" in href
                        ):
                            item["detail_link"] = (
                                "https://bidplus.gem.gov.in/"
                                + href.lstrip("/")
                            )

                    item["bid_no"] = bid_no
                    item["ra_no"] = ra_no

                    results.append(item)

                    if len(results) >= limit:
                        break

                except Exception as e:
                    print("Card Error:", e)

            next_button = page.locator("text=Next")

            if next_button.count() == 0:
                break

            next_button.click()

            page.wait_for_timeout(5000)

            current_page += 1

        browser.close()

    return results