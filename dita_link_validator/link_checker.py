"""
Funs in module check links to find broken ones.
"""

from __future__ import print_function
import requests


def is_protocol_correct(link):
    """
    Correct protocols are https and http.
    Function returns False if start of link does not match either.
    """
    return link.startswith('http', 0, 4) or link.startswith('https', 0, 5)


def check_link(link):
    """
    Pings link and sends back response tuple
    for console_message fun (tag,message_key)
    """

    # Check protocol first. If incorrect, do not go further
    if not is_protocol_correct(link):
        return ('error', 'invalid_url_error')

    # Uses HEAD request to get status code
    try:
        status = requests.head(link).status_code

        # If HEAD method not supported, retry with GET
        if status == 405:
            status = requests.get(link).status_code

        # Status codes of 400 or higher are error codes.
        if status >= 400:
            return ('error', 'status_code_error')

        return ('ok', 'check_link_message')

    # Possible error scenarios for the http request:
    except requests.exceptions.MissingSchema:
        return ('error', 'invalid_url_error')

    except requests.exceptions.InvalidURL:
        return ('error', 'invalid_url_error')

    except requests.exceptions.ConnectionError:
        return ('error', 'connection_error')
