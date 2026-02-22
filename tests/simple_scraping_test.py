import json
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from scraper.data_scraper import scrape_ad_details
from scraper.config import LINKS_FILE, SCRAPED_DATA_FILE


def run_extraction_test(target_count=3):
    if not os.path.exists(LINKS_FILE):
        print(f"Error: {LINKS_FILE} not found at {os.path.abspath(LINKS_FILE)}")
        return

    # load links
    with open(LINKS_FILE, "r", encoding="utf-8") as f:
        all_links = json.load(f)

    options = Options()
    # forces the window to start off-screen or at a tiny size
    options.add_argument("--window-position=-2000,0")

    # for headless mode
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.minimize_window()

    scraped_results = []

    print(f"Starting test: Looking for {target_count} OLX ads (ignoring Autovit)...")

    try:
        for link in all_links:
            # skip Autovit / todo: add autovit scraping
            if "autovit.ro" in link:
                continue

            print(f"[{len(scraped_results) + 1}/{target_count}] Scraping: {link}")
            ad_data = scrape_ad_details(driver, link)

            if ad_data:
                scraped_results.append(ad_data)
                print(f"   ✓ Scraped: {ad_data.get('title')[:50]}...")

            # stop when target reached
            if len(scraped_results) >= target_count:
                break

        os.makedirs(os.path.dirname(SCRAPED_DATA_FILE), exist_ok=True)

        with open(SCRAPED_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(scraped_results, f, indent=4, ensure_ascii=False)

        print(f"\nSuccess! Scraped {len(scraped_results)} ads to {SCRAPED_DATA_FILE}")

    except Exception as e:
        print(f"An error occurred during the test run: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_extraction_test(target_count=3)