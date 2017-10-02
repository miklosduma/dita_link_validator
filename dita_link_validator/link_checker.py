"""
Funs in module check links to find broken ones.
"""

from __future__ import print_function
import os
import requests


def is_protocol_correct(link):
    """
    Correct protocols are https and http.
    Function returns False if start of link does not match either.
    """
    return link.startswith('http', 0, 4) or link.startswith('https', 0, 5)


def is_rel_link(md_file, link):
    """
    For markdown use. If protocol is missing, link might be relative link.
    Fun checks if link is a valid path to an existing file.
    """

    (path_to_file, file_name) = os.path.split(md_file)
    rel_path = os.path.join(path_to_file, link)

    return os.path.exists(rel_path)


def check_link(link):
    """
    Pings link and sends back response tuple
    for console_message fun (tag,message_key)
    """

    # Check protocol first. If incorrect, do not go further
    if not is_protocol_correct(link):
        return ('error', 'invalid_protocol')

    # Uses HEAD request to get status code
    try:
        status = requests.head(link).status_code

        # If HEAD method not supported, retry with GET
        if status == 405:
            status = requests.get(link).status_code

        # If you're not authenticated, send warning
        if status == 401:
            return ('warning', 'auth_warn')

        # Status codes of 400 or higher are error codes.
        if status >= 400:
            print(status)
            return ('error', 'status_code_error')

        return ('ok', 'check_link_message')

    # Possible error scenarios for the http request:
    except requests.exceptions.MissingSchema:
        return ('error', 'invalid_url_error')

    except requests.exceptions.InvalidURL:
        return ('error', 'invalid_url_error')

    except requests.exceptions.ConnectionError:
        return ('error', 'connection_error')
