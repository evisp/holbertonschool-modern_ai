#!/usr/bin/env python3
"""
Module providing a scraper that collects quotes from the JSON API
of quotes.toscrape.com, page by page.
"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """
    Fetch every page of the quotes API and collect all quotes.

    Starts at /api/quotes?page=1 and keeps requesting the next page
    while the payload reports "has_next" as true.

    Args:
        base_url (str): the root URL of the site,
            e.g. "https://quotes.toscrape.com".

    Returns:
        list: a list of quote dicts, each with keys
            "text" (str), "author" (str) and "tags" (list of str).
    """
    root = base_url.rstrip("/")
    quotes = []
    page = 1

    while True:
        endpoint = "{}/api/quotes?page={}".format(root, page)
        payload = json.loads(fetch_html(endpoint))

        for item in payload.get("quotes", []):
            author = item.get("author", "")
            if isinstance(author, dict):
                author = author.get("name", "")
            quotes.append({
                "text": item.get("text", ""),
                "author": author,
                "tags": item.get("tags", [])
            })

        if not payload.get("has_next") or not payload.get("quotes"):
            break
        page += 1

    return quotes
