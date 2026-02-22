import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper.config import OLX, WAIT_TIME

def scrape_ad_details(driver, url):
    driver.get(url)
    time.sleep(WAIT_TIME)

    data = {"url": url}

    try:
        # title and price
        data['title'] = driver.find_element(By.CSS_SELECTOR, OLX['SELECTOR_TITLE']).text
        data['price'] = driver.find_element(By.CSS_SELECTOR, OLX['SELECTOR_PRICE']).text

        # tags
        raw_attributes = driver.find_elements(By.CSS_SELECTOR, OLX['SELECTOR_ATTRIBUTES'])
        attributes_dict = {}

        for attr in raw_attributes:
            text = attr.text
            if ":" in text:
                key, val = text.split(":", 1)
                attributes_dict[key.strip()] = val.strip()
            elif text.strip():
                # Handling labels without colons (e.g., "Private", "Business")
                attributes_dict[text.strip()] = "Yes"

        data['attributes'] = attributes_dict

        # description
        description_element = driver.find_element(By.CSS_SELECTOR, OLX['SELECTOR_DESCRIPTION'])
        data['raw_description'] = description_element.text

    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return None

    return data