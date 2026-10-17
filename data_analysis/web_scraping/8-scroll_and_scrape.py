#!/usr/bin/env python3
"""
Module providing a Selenium scraper that scrolls a JS-rendered
infinite-scroll page and collects every unique product on it.
"""
import time
from selenium import webdriver

By = webdriver.common.by.By
HEIGHT_JS = "return document.body.scrollHeight"
SCROLL_JS = "window.scrollTo(0, document.body.scrollHeight);"


def _build_driver():
    """
    Create a headless Chrome driver with a 1920x1080 window.

    Images are disabled and the page load strategy is "eager",
    so the driver does not wait for resources the scraper never uses.

    Returns:
        selenium.webdriver.Chrome: the configured driver instance.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2})
    options.page_load_strategy = "eager"
    return webdriver.Chrome(options=options)


def _wait_for_products(driver, timeout):
    """
    Wait until at least one product card is present on the page.

    Args:
        driver (selenium.webdriver.Chrome): the active driver.
        timeout (float): maximum number of seconds to wait.
    """
    end = time.time() + timeout
    while time.time() < end:
        if driver.find_elements(By.CSS_SELECTOR, "div.thumbnail"):
            return
        time.sleep(0.2)


def _wait_for_growth(driver, old_height, scroll_pause):
    """
    Wait up to scroll_pause seconds for the page height to increase.

    Returns as soon as the height grows, so each scroll only waits
    as long as the next batch actually takes to load.

    Args:
        driver (selenium.webdriver.Chrome): the active driver.
        old_height (int): the page height before the last scroll.
        scroll_pause (float): maximum number of seconds to wait.

    Returns:
        int: the current page height.
    """
    end = time.time() + scroll_pause
    height = old_height
    while time.time() < end:
        time.sleep(0.2)
        height = driver.execute_script(HEIGHT_JS)
        if height > old_height:
            break
    return height


def _scroll_to_end(driver, scroll_pause):
    """
    Scroll to the bottom until the page height stops increasing.

    Args:
        driver (selenium.webdriver.Chrome): the active driver.
        scroll_pause (float): seconds to wait for new content
            after each scroll before deciding the page has ended.
    """
    last_height = driver.execute_script(HEIGHT_JS)
    while True:
        driver.execute_script(SCROLL_JS)
        new_height = _wait_for_growth(driver, last_height, scroll_pause)
        if new_height <= last_height:
            break
        last_height = new_height


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Scroll an infinite-scroll page and scrape all unique products.

    Args:
        url (str): the infinite-scroll page, e.g.
            "https://webscraper.io/test-sites/e-commerce/scroll/"
            "computers/laptops".
        scroll_pause (float): seconds to wait for new content
            after each scroll.

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
        _wait_for_products(driver, 10)
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
