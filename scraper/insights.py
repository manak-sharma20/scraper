import pandas as pd


df = pd.read_csv("data/bids.csv")

print("\nTOTAL BIDS:")
print(len(df))

print("\nTOP DEPARTMENTS:")
print(df["department"].value_counts().head())

print("\nTOP ITEM TYPES:")
print(df["items"].value_counts().head())

print("\nTOP QUANTITY BIDS:")
print(
    df.sort_values(
        by="quantity",
        ascending=False
    ).head()
)