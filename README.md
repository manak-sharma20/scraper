# GeM Bid Scraper

A Playwright-based procurement scraping pipeline for extracting bid data from the GeM portal.

## Features

- Dynamic web scraping using Playwright
- Pagination handling
- Robust extraction from inconsistent layouts
- Department normalization
- Bid document link extraction
- CSV export
- Procurement insights generation

## Tech Stack

- Python
- Playwright
- Pandas

## Project Structure

gemedge-scraper/
│
├── scraper/
│   ├── listing.py
│   ├── detail.py
│   ├── utils.py
│   └── __init__.py
│
├── data/
│   ├── bids.csv
│   └── .gitkeep
│
├── insights.py
├── main.py
├── requirements.txt
└── README.md

## Setup

pip install -r requirements.txt
playwright install

## Run Scraper

python main.py

## Generate Insights

python insights.py

## Output

- data/bids.csv

## Limitations

Some bid detail endpoints triggered direct PDF downloads instead of HTML-rendered pages. Due to this, deeper evaluation-layer extraction such as bidder comparison tables and L1 vendor extraction could not be consistently automated across all bid formats.

## Future Improvements

- PDF parsing for bid documents
- Automated bidder comparison extraction
- Vendor ranking analysis
- Dashboard visualization