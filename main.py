import pandas as pd

from scraper.listing import scrape_listings


data = scrape_listings(50)

df = pd.DataFrame(data)

print(df.head())

df.to_csv("data/bids.csv", index=False)

print("\nSaved data to data/bids.csv")