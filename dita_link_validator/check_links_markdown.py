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


def get_reference_links(md_content):
    """
    Collects reference type links.
    E.g.: 
        [link text][link reference]
        [link reference]: actual link
    """
    links = []

    # Match [*][*] pattern and collect content
    # inside second pair of square brackets
    link_reference_candidates = re.findall(
        r'(?<=\]\[)[^][]+(?=\])', md_content)

    # Use collected reference candidate to check if
    # a links is assigned to it
    # E.g. [reference]: link
    for reference in link_reference_candidates:
        regex = r'(?<=\[%s\]: )[^ \n]+' % (reference)
        link = re.findall(regex, md_content)

        # If anything matched, add link value to links list
        if link != []:
            link_value = link[0]
            links.append(link_value)

    return links


def get_md_simple_links(md_content):
    """
    Collects simple markdown links.
    E.g.: [text](link) 
    """

    # (?>!\!) -> exclude images
    # \[[^[]+\] -> matches anything in square brackets []
    # \([^#][^(]+\) -> matches anything in brackets (), except:
    # anchor links that start with hashtag (#)

    simple_links = re.findall(r'(?<!\!)\[[^[]+\]\([^#][^( ]+\)',  md_content)
    simple_links_list = []
    for link in simple_links:
        actual_link = re.findall(r'(?<=\()[^(]+(?=\))', link)[0]
        simple_links_list.append(actual_link)

    return simple_links_list


def get_md_links_with_title(md_content):
    """
    Collects simple markdown links with title.
    E.g.: [text](link) or [text](link Title) 
    """

    # (?>!\!) -> exclude images
    # \[[^[]+\] -> matches anything in square brackets []
    # \([^#][^(]+\) -> matches anything in brackets (), except:
    # anchor links that start with hashtag (#)
    title_links = re.findall(
        r'(?<!\!)\[[^[]+\]\([^#][^(]+"[^"]+"\)',  md_content)
    title_links_list = []
    for link in title_links:
        actual_link = re.findall(r'(?<=\()[^( ]+(?=\s)', link)[0]
        title_links_list.append(actual_link)

    return title_links_list


def get_md_links(md_file):
    """
    Collects all links from a markdown file.
    """
    open_file = open(md_file, 'r')
    content = open_file.read()
    links_list = []
    simple_links = get_md_simple_links(content)
    title_links = get_md_links_with_title(content)
    ref_links = get_reference_links(content)
    links_list += simple_links
    links_list += title_links
    links_list += ref_links

    return links_list


def get_md_files(root_dir):
    """
    Collects markdown files from a directory.
    """
    paths_to_files = []
    for root, _, files in os.walk(root_dir):
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
    number_of_files = len(md_files)
    total_links = 0
    error_links = []

    for md_file in md_files:

        print(console_message(
            'info',
            'check_message',
            md_file,
            with_tag=False))
        links_to_check = get_md_links(md_file)

        number_of_links = len(links_to_check)
        total_links += number_of_links

        for link in links_to_check:
            (tag, message) = check_link(link)

            if tag == 'error':
                print(console_message(tag, message, link))
                error_links.append(link + ' in ' + md_file)

            if tag == 'ok':
                print(console_message(tag, message, link,
                                      with_tag=False, with_color=False))
        print('Number of links checked: %s' % (number_of_links))

    number_of_broken_links = len(error_links)

    print('Number of files collected: %s' % (number_of_files))
    print('Total number of links checked: %s' % (total_links))

    if number_of_broken_links > 0:
        print(console_message('error', 'error_count_message',
                              "\n".join(error_links), with_tag=False))
        return ('error', 'error_count_message', error_links)

    print(console_message('ok', 'all_good_message', root_dir))
    return ('ok', 'all_good_message', root_dir)


# check_links_in_dir(TARGET_FOLDER2)
