#!/usr/bin/env python3
"""
Module providing a scraper that logs in to quotes.toscrape.com
and collects the quotes visible after authentication.
"""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """
    Log in with a CSRF-protected form and scrape the quotes page.

    Args:
        login_url (str): the login page,
            e.g. "https://quotes.toscrape.com/login".
        user (str): the username to submit.
        pwd (str): the password to submit.

    Returns:
        list: a list of quote dicts, each with keys
            "text" (str), "author" (str) and "tags" (list of str).

    Raises:
        requests.exceptions.HTTPError: on any HTTP status >= 400.
        TypeError: if the login page has no csrf_token input.
    """
    quotes_url = requests.compat.urljoin(login_url, "/")

    with requests.Session() as session:
        response = session.get(login_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        token = soup.find("input", attrs={"name": "csrf_token"})["value"]

        payload = {
            "csrf_token": token,
            "username": user,
            "password": pwd
        }
        response = session.post(login_url, data=payload, timeout=10)
        response.raise_for_status()

        response = session.get(quotes_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

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
