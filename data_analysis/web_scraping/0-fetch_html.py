#!/usr/bin/env python3
"""
Module providing a helper to fetch the raw HTML of a web page
using the requests library.
"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """
    Fetch a web page and return its HTML content as text.

    Args:
        url (str): the URL of the page to retrieve.
        headers (dict, optional): HTTP headers to send with the request,
            e.g. {"User-Agent": "..."}. Defaults to None.
        timeout (int or float, optional): number of seconds to wait
            before aborting the request. Defaults to 10.

    Returns:
        str: the full HTML of the response.

    Raises:
        requests.exceptions.HTTPError: if the HTTP status code is >= 400.
        requests.exceptions.RequestException: on connection errors
            or timeouts.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text