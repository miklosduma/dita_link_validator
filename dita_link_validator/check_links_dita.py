"""
Funs to collect links from a structured ditamap.
"""
from __future__ import print_function

import xml.etree.ElementTree as ET
import sys

from messages import console_message
from link_checker import check_link


def get_topicrefs_from_map(ditamap):
    """
    Collects topicref elements from ditamap.
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
    print(console_message('info', 'check_message', ditamap, with_tag=False))

    # Warns if name of file does not end with .ditamap
    suffix = '.ditamap'
    if not ditamap.endswith(suffix):
        print(console_message('warn', 'no_ditamap_warn', ditamap))

    try:
        # Gets first level topicref children of ditamap
        xml_tree = ET.parse(ditamap)
        root_map = xml_tree.getroot()
        topicrefs = root_map.findall('topicref')

        # Checks only html links
        topicrefs_with_links = [
            x for x in topicrefs if x.attrib.get('format') == 'html']
        return topicrefs_with_links

    # Returns exception if command argument (first positional) targets a
    # non-existent file
    except IOError as error:
        print(error)
        print(console_message('error', 'no_such_file_error', ditamap))
        return ('error', 'no_such_file_error', ditamap)

    # Returns an exception if the file is not XML or well-formed
    except ET.ParseError:
        print(console_message('error', 'not_xml_error', ditamap))
        return ('error', 'not_xml_error', ditamap)


def links_map_checker(ditamap):
    """
    Expects a ditamap that has one or more topicrefs with href attributes.
    Calls check_link function on all link values of hrefs
    """

    # Collect topicrefs with links from map
    topicrefs_with_links = get_topicrefs_from_map(ditamap)
    number_of_topicrefs = len(topicrefs_with_links)

    # If no external links in topicrefs, return from function
    if number_of_topicrefs == 0:
        print(console_message('warn', 'no_links_warn', ditamap))
        return ('warn', 'no_links_warn', ditamap)

    # get_topicrefs_from_map comes back with error if file is not xml or does
    # not exist
    if topicrefs_with_links[0] == 'error':
        return topicrefs_with_links

    # Get links from topicrefs and ping them through check_link fun
    # Collect broken links into error_links list
    error_links = []

    for topicref in topicrefs_with_links:

        link = topicref.attrib.get('href')
        (tag, message_key) = check_link(link)

        # If pinging a link returns an error, link is added to error_links
        if tag == 'error':
            error_links.append(link)
            print(console_message(tag, message_key, link))

        if tag == 'warn':
            print(console_message(tag, message_key, link))

        if tag == 'ok':
            print(console_message(tag, message_key, link,
                                  with_tag=False, with_color=False))

    # If error_links holds any links, prints all links in it as a
    # comma-separated string
    number_of_broken_links = len(error_links)
    if number_of_broken_links > 0:
        print(console_message('error', 'error_count_message',
                              "\n".join(error_links), with_tag=False))
        return ('error', 'error_count_message', error_links)

    print(console_message('ok', 'all_good_message', ditamap))
    return ('ok', 'all_good_message', ditamap)
