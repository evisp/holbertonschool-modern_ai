#!/usr/bin/env python3
"""
Module providing a basic static scraper for the first page
of quotes.toscrape.com using BeautifulSoup.
"""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Scrape the quotes listed on a single page of quotes.toscrape.com.

    Args:
        url (str): the Quotes List endpoint,
            e.g. "https://quotes.toscrape.com/".

    Returns:
        list: a list of dicts, one per quote block, each with:
            - "text" (str): the quote text
            - "author" (str): the quote's author
            - "tags" (list of str): the tags attached to the quote
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    quotes = []
    for block in soup.select("div.quote"):
        text = block.select_one("span.text")
        author = block.select_one("small.author")
        tags = [tag.get_text(strip=True) for tag in block.select("a.tag")]
        quotes.append({
            "text": text.get_text(strip=True) if text else "",
            "author": author.get_text(strip=True) if author else "",
            "tags": tags
        })
    return quotes
