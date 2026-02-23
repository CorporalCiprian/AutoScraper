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
.venv\Scripts\activate
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

Crawls search results and saves unique ad URLs to `data/links.json` and outputs the scraped links in `data/scraped_raw_data.json`:

```bash
python -m main
```

### Selectors
Update the `OLX` and `AUTOVIT` dictionaries if websites classes change.

## Output

- `data/links.json` → Collected advertisement URLs  
- `data/scraped_raw_data.json` → Structured scraped vehicle data  
