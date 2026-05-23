import pandas as pd

from scraper.listing import scrape_listings


data = scrape_listings(20)

df = pd.DataFrame(data)

print(df.head())

df.to_csv("data/bids.csv", index=False)

print("\nSaved to data/bids.csv")