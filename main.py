import pandas as pd

from scraper.listing import scrape_listings
from scraper.detail import download_bid_pdf
from scraper.evaluation import extract_vendor_details


data = scrape_listings(20)

df = pd.DataFrame(data)
df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

df.to_csv("data/bids.csv", index=False)

print("\nCSV saved to data/bids.csv")

if len(data) > 0:

    url = data[0]["detail_link"]

    download_bid_pdf(url)

    vendor_data = extract_vendor_details(
        "data/sample.pdf"
    )

    print("\nVendor Extraction Attempt:")
    print(vendor_data)