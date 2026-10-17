#!/usr/bin/env python3
"""
Module providing a Selenium scraper that collects the details
of a single product page on the webscraper.io e-commerce test site.
"""
import time
from selenium import webdriver

By = webdriver.common.by.By


def _build_driver():
    """
    Create a headless Chrome driver with a 1920x1080 window.

    Returns:
        selenium.webdriver.Chrome: the configured driver instance.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def scrape_product_detail(url, delay=2.0):
    """
    Open a product detail page and extract its main fields.

    Args:
        url (str): the product detail page, e.g.
            "https://webscraper.io/test-sites/e-commerce/static/product/32".
        delay (float): seconds to wait after loading the page.

    Returns:
        dict: a dict with keys
            "title" (str): text of the second h4 inside .caption,
            "price" (str): text of the first h4.price,
            "description" (str): text of p.description,
            "rating" (int): number of star icons inside .ratings.
    """
    driver = _build_driver()
    try:
        driver.get(url)
        time.sleep(delay)

        headings = driver.find_elements(By.CSS_SELECTOR, ".caption h4")
        price = driver.find_element(By.CSS_SELECTOR, "h4.price")
        description = driver.find_element(By.CSS_SELECTOR, "p.description")
        stars = driver.find_elements(By.CSS_SELECTOR,
                                     ".ratings .ws-icon-star")

        return {
            "title": headings[1].text.strip(),
            "price": price.text.strip(),
            "description": description.text.strip(),
            "rating": len(stars)
        }
    finally:
        driver.quit()
