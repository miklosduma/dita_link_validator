"""
Functions to collect markdown files in a directory
and all links in them.
"""

from __future__ import print_function

import re
import os

from messages import console_message
from link_checker import check_link

TARGET_FOLDER = '../../examples'
TARGET_FOLDER2 = '../../sparkl_cli.wiki'


def get_md_links(md_file):
    """
    Collects links from a markdown file.
    """
    open_file = open(md_file, 'r')
    content = open_file.read()
    links = re.findall(r'https?://[^)\r\n\s\]\[]+', content)
    links_list = []
    """
    links = re.findall(r'(?<!\!)\[[^[]+\]\([^#][^(]+\)',  content)
    links_list = []
    for link in links:
        actual_link = re.findall(r'(?<=\()[^(]+(?=\))', link)[0]
        #actual_link = link.split(']')[1].replace('(', "").replace(')', "")
        links_list += [(actual_link, md_file)]
    """
    for link in links:
        links_list += [(link, md_file)]
    return links_list


def get_md_files(root_dir):
    """
    Collects markdown files from a directory.
    """
    paths_to_files = []
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if '.md' in name:
                file_path = os.path.join(root, name)
                paths_to_files.append(file_path)
    return paths_to_files


def check_links_in_dir(root_dir):
    """
    Checks all links in all markdown files
    in a directory.
    """
    md_files = get_md_files(root_dir)
    links_to_check = []
    error_links = []

    for md in md_files:
        links_to_check += get_md_links(md)

    for link_tuple in links_to_check:
        (link, file_name) = link_tuple
        (tag, message) = check_link(link)

        if tag == 'error':
            print(console_message(tag, message, link))
            error_links.append(link)

        if tag == 'ok':
            print(console_message(tag, message, link,
                                  with_tag=False, with_color=False))

    number_of_broken_links = len(error_links)
    if number_of_broken_links > 0:
        print(console_message('error', 'error_count_message',
                              ", ".join(error_links), with_tag=False))
        return ('error', 'error_count_message', error_links)

    print(console_message('ok', 'all_good_message', root_dir))
    return ('ok', 'all_good_message', root_dir)


check_links_in_dir(TARGET_FOLDER)
