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


def get_files(root_dir):
    """
    Collects markdown files from a directory.
    """
    max_links_list = []
    max_files_checked = 0
    max_links_checked = 0
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if '.md' in name:
                max_files_checked += 1
                file_path = os.path.join(root, name)
                # print "Retrieving files in %s:" % (file_path)
                max_links_list += get_md_links(file_path)

    for link_tuple in max_links_list:
        (link, file_name) = link_tuple
        (tag, message) = check_link(link)
        print(console_message(tag, message, link,
                              with_tag=False, with_color=False))
        max_links_checked += 1
        if tag == 'error':
            print(console_message(tag, message, link))
    print("Files checked: %s" % (max_files_checked))
    print("Links checked: %s" % (max_links_checked))
    return

get_files(TARGET_FOLDER2)
