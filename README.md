# GeM Bid Scraper

A Playwright-based procurement scraping pipeline for extracting bid data from the GeM (Government e-Marketplace) portal.

## Features

- Dynamic web scraping using Playwright
- Pagination handling
- Robust extraction from inconsistent layouts
- Department normalization
- Bid document link extraction
- CSV export
- Procurement insights generation
- PDF download workflow
- Vendor extraction attempt from bid documents

---

## Tech Stack

- Python
- Playwright
- Pandas
- Requests
- pdfplumber

---

## Project Structure

```text
gemedge-scraper/
│
├── scraper/
│   ├── listing.py
│   ├── detail.py
│   ├── evaluation.py
│   └── __init__.py
│
├── data/
│   ├── bids.csv
│   └── .gitkeep
│
├── insights.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Pipeline Workflow

1. Scrape bid listings using Playwright
2. Extract structured bid metadata
3. Handle pagination dynamically
4. Export bid dataset to CSV
5. Download bid documents (PDFs)
6. Attempt vendor/evaluation extraction from PDFs
7. Generate procurement insights

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

## Run Scraper

```bash
python main.py
```

This will:

- Scrape bid listings
- Export structured data to CSV
- Download a sample bid PDF
- Attempt vendor extraction from the PDF

---

## Generate Insights

```bash
python insights.py
```

Example insights generated:

- Total bids scraped
- Top departments
- Top item categories
- High quantity procurements

---

## Output

Generated dataset:

```text
data/bids.csv
```

Example fields:

- bid_no
- ra_no
- items
- quantity
- department
- start_date
- end_date
- detail_link

---

## Limitations

Some bid detail endpoints triggered direct PDF downloads instead of structured HTML-rendered pages. Due to this, deeper evaluation-layer extraction such as bidder comparison tables and L1 vendor extraction could not be reliably automated across all bid formats.

Additionally, some bid documents were image-based/scanned PDFs, limiting reliable text extraction without OCR integration.

---

## Future Improvements

- OCR integration for scanned PDFs
- Automated bidder comparison extraction
- Vendor ranking analysis
- Dashboard visualization
- Scheduled scraping pipeline
- Database integration

---

## Author

Kumar Manak