from __future__ import print_function

import xml.etree.ElementTree as ET
import requests
import sys

from messages import console_message


def check_link(link):
    """
    Pings link and sends back response tuple (tag,message_key) for console_message fun
    """

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


def links_map_checker(file):
    """
    Expects a ditamap that has one or more topicrefs with href attributes.
    Calls check_link function on all link values of hrefs
    """

    print(console_message('info', 'check_message', file, with_tag=False))

    # Warns if name of file does not end with .ditamap
    suffix = '.ditamap'
    if not file.endswith(suffix):
        print(console_message('warning', 'no_ditamap_warn', file))

    try:
        # Gets first level topicref children of ditamap
        xml_tree = ET.parse(file)
        root_map = xml_tree.getroot()
        topicrefs = root_map.findall('topicref')

        """
        Sample map:
        <map>
            ...
            <topicref
                href="http://docs.ansible.com/ansible/index.html"
                ...
            </topicref>
            ...OTHER TOPICREFS...
        </map>
        """

        # Checks only html links
        topicrefs_with_links = [
            x for x in topicrefs if x.attrib.get('format') == 'html']

        # If no external links in topicrefs, return from function
        if len(topicrefs_with_links) == 0:
            print(console_message('warning', 'no_links_warn', file))
            return ('warning', 'no_links_warn', file)

        # Get links from topicrefs and ping them through check_link fun
        # Collect broken links into error_links list
        error_links = []
        for topicref in topicrefs_with_links:
            link = topicref.attrib.get('href')
            (tag, message_key) = check_link(link)

            # If pinging a link returns an error, link is added to error_links
            # list
            if tag == 'error':
                error_links.append(link)
                print(console_message(tag, message_key, link))

            if tag == 'ok':
                print(console_message(tag, message_key, link,
                                      with_tag=False, with_color=False))

        # If error_links holds any links, prints all links in it as a
        # comma-separated string
        if len(error_links) > 0:
            print(console_message('error', 'error_count_message',
                                  ", ".join(error_links), with_tag=False))
            return ('error', 'error_count_message', error_links)

        print(console_message('ok', 'all_good_message', file))
        return ('ok', 'all_good_message', file)

    # Returns exception if command argument (first positional) targets a
    # non-existent file
    except IOError:
        print(console_message('error', 'no_such_file_error', file))
        return ('error', 'no_such_file_error', file)

    # Returns an exception if the file is not XML or well-formed
    except ET.ParseError:
        print(console_message('error', 'not_xml_error', file))
        return ('error', 'not_xml_error', file)

# Call from command-line as 'python link_checker.py [PATH_TO_DITAMAP]'
if __name__ == "__main__":
    # Only calls command if minimum one argument is specified (command itself
    # is an element in sys.argv list)
    if len(sys.argv) == 1:
        print(console_message('error', 'file_not_spec_error', ''))

    # Calls the links_map_checker fun with the first positional argument
    if len(sys.argv) > 1:
        links_map_checker(sys.argv[1])
