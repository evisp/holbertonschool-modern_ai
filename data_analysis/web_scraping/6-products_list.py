#!/usr/bin/env python3
"""
Module providing a Selenium scraper that collects the products
listed on a static webscraper.io e-commerce category page.
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


def scrape_products(url):
    """
    Scrape every product card on a static product category page.

    Args:
        url (str): the category page, e.g.
            "https://webscraper.io/test-sites/e-commerce/static/"
            "computers/laptops".

    Returns:
        list: a list of product dicts, each with keys
            "title" (str): the title attribute of the product link,
            "price" (str): the text of the h4.price element,
            "description" (str): the text of the p.description element,
            "rating" (int): the data-rating value under .ratings.
    """
    driver = _build_driver()
    try:
        driver.get(url)
        time.sleep(1)

        products = []
        for card in driver.find_elements(By.CSS_SELECTOR, "div.thumbnail"):
            link = card.find_element(By.CSS_SELECTOR, "a.title")
            price = card.find_element(By.CSS_SELECTOR, "h4.price")
            description = card.find_element(By.CSS_SELECTOR,
                                            "p.description")
            rating = card.find_element(By.CSS_SELECTOR,
                                       ".ratings p[data-rating]")
            products.append({
                "title": link.get_attribute("title"),
                "price": price.text.strip(),
                "description": description.text.strip(),
                "rating": int(rating.get_attribute("data-rating"))
            })
        return products
    finally:
        driver.quit()


scrape_products_list = scrape_products