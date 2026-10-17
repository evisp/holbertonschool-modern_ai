#!/usr/bin/env python3
"""
Module providing a paginated scraper for quotes.toscrape.com
that follows the "Next" links until no more pages remain.
"""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Scrape every page of quotes by following the "Next" links.

    Args:
        base_url (str): the first page URL,
            e.g. "https://quotes.toscrape.com/".

    Returns:
        list: the combined list of quote dicts from all pages, each with
            "text", "author" and "tags" keys (same format as scrape_basic).
    """
    all_quotes = []
    visited = set()
    url = base_url

    while url and url not in visited:
        visited.add(url)
        all_quotes.extend(scrape_basic(url))

        soup = BeautifulSoup(fetch_html(url), "html.parser")
        next_link = soup.select_one("li.next > a")
        if next_link is None or not next_link.get("href"):
            break

        url = parse.urljoin(url, next_link["href"])
        time.sleep(0.5)

    return all_quotes
