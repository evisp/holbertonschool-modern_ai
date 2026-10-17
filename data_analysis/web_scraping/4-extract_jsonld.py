#!/usr/bin/env python3
"""
Module providing a scraper that extracts quotes from the JSON-LD
blocks embedded in a web page.
"""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def _collect_objects(data):
    """
    Flatten a parsed JSON-LD value into a list of JSON-LD objects.

    Handles a single object, a list of objects, and objects that
    wrap their items in an "@graph" array.

    Args:
        data: the value returned by json.loads() for one script block.

    Returns:
        list: the dict objects found in the value.
    """
    if isinstance(data, list):
        objects = []
        for item in data:
            objects.extend(_collect_objects(item))
        return objects
    if isinstance(data, dict):
        if "@graph" in data:
            return _collect_objects(data["@graph"])
        return [data]
    return []


def _is_quote(obj):
    """
    Check whether a JSON-LD object has "@type" equal to "Quote".

    Args:
        obj (dict): a JSON-LD object.

    Returns:
        bool: True if the object's type is (or includes) "Quote".
    """
    obj_type = obj.get("@type")
    if isinstance(obj_type, list):
        return "Quote" in obj_type
    return obj_type == "Quote"


def _parse_tags(keywords):
    """
    Normalize JSON-LD keywords into a list of tag strings.

    Args:
        keywords: a list of strings, a comma-separated string, or None.

    Returns:
        list: the tags as a list of stripped, non-empty strings.
    """
    if keywords is None:
        return []
    if isinstance(keywords, str):
        keywords = keywords.split(",")
    return [str(tag).strip() for tag in keywords if str(tag).strip()]


def extract_jsonld(url):
    """
    Extract quotes from the JSON-LD script blocks of a page.

    Args:
        url (str): the Quotes List endpoint,
            e.g. "https://quotes.toscrape.com/".

    Returns:
        list: a list of quote dicts, each with keys
            "text" (str), "author" (str) and "tags" (list of str).
    """
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    quotes = []

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.get_text())
        except ValueError:
            continue

        for obj in _collect_objects(data):
            if not _is_quote(obj):
                continue
            author = obj.get("author", {})
            if isinstance(author, dict):
                author = author.get("name")
            quotes.append({
                "text": obj.get("text"),
                "author": author,
                "tags": _parse_tags(obj.get("keywords"))
            })

    return quotes
