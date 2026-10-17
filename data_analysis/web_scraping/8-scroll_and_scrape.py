#!/usr/bin/env python3
"""
Module providing a Selenium scraper that scrolls a JS-rendered
infinite-scroll page and collects every unique product on it.
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


def _scroll_to_end(driver, scroll_pause):
    """
    Scroll to the bottom until the page height stops increasing.

    Args:
        driver (selenium.webdriver.Chrome): the active driver.
        scroll_pause (float): seconds to wait after each scroll.
    """
    last_height = driver.execute_script(
        "return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script(
            "return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Scroll an infinite-scroll page and scrape all unique products.

    Args:
        url (str): the infinite-scroll page, e.g.
            "https://webscraper.io/test-sites/e-commerce/scroll/"
            "computers/laptops".
        scroll_pause (float): seconds to wait after each scroll.

    Returns:
        list: a list of unique product dicts, each with keys
            "title" (str): the title attribute of a.title,
            "price" (str): the text of h4.price,
            "description" (str): the text of p.description,
            "rating" (int): the number of star icons under .ratings.
    """
    driver = _build_driver()
    try:
        driver.get(url)
        time.sleep(scroll_pause)
        _scroll_to_end(driver, scroll_pause)

        products = []
        seen = set()
        for card in driver.find_elements(By.CSS_SELECTOR, "div.thumbnail"):
            title = card.find_element(
                By.CSS_SELECTOR, "a.title").get_attribute("title")
            price = card.find_element(
                By.CSS_SELECTOR, "h4.price").text.strip()
            if (title, price) in seen:
                continue
            seen.add((title, price))

            description = card.find_element(
                By.CSS_SELECTOR, "p.description").text.strip()
            stars = card.find_elements(
                By.CSS_SELECTOR, ".ratings .ws-icon-star")
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": len(stars)
            })
        return products
    finally:
        driver.quit()
