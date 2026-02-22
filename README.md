# AutoScraper

An automated web scraping tool for **OLX.ro** car listings.  
This project uses Selenium to navigate search pages, extract advertisement links, and scrape detailed vehicle information into structured JSON data.

## Installation

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows:**
```bash
.venv\Scripts\activate'
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Usage

### Extract Links

Crawls search results and saves unique ad URLs to `data/links.json`:

```bash
python -m scraper.get_links
```

### Extract Data

Visits the collected URLs to scrape titles, prices, and vehicle attributes:

```bash
python -m scraper.run_test
```

### Selectors
Update the `OLX` dictionary if website classes change.

## Output

- `data/links.json` → Collected advertisement URLs  
- `data/scraped_raw_data.json` → Structured scraped vehicle data  
