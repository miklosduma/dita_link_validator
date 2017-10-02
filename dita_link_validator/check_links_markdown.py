"""
Functions to collect markdown files in a directory
and all links in them.
"""

from __future__ import print_function

import re
import os

from messages import console_message
from link_checker import check_link, is_rel_link


def get_reference_links(md_content):
    """
    Collects reference type links.
    E.g.:
        [Book of Knowledge][1]
        [1]: http://book.knowledge.com
    """
    links = []

    # Match [*][*] pattern and collect content
    # inside second pair of square brackets
    link_reference_candidates = re.findall(
        r'(?<=\]\[)[^][]+(?=\])', md_content)

    # Use collected reference candidates to check if
    # a link is assigned to any of them
    # E.g. [reference]: link
    for reference in link_reference_candidates:
        regex = r'(?<=\[%s\]: )[^ \n\r]+' % (reference)
        link = re.findall(regex, md_content)

        # If anything matched, add link value to links list
        if link != []:
            link_value = link[0]
            links.append(link_value)

    return links


def get_simple_links(md_content):
    """
    Collects simple markdown links.
    E.g.: [text](link)
    """
    simple_links_list = []
    # (?>!\!) -> exclude images
    # \[[^[]+\] -> matches anything in square brackets
    # \([^#][^(]+\) -> matches anything in brackets, except
    # anchor links that start with hashtag (#)
    simple_links = re.findall(r'(?<!\!)\[[^[]+\]\([^#][^( ]+\)', md_content)

    # Collect link value from matched links
    for link in simple_links:
        link_value = re.findall(r'(?<=\]\()[^(]+(?=\))', link)[0]
        simple_links_list.append(link_value)

    return simple_links_list


def get_links_with_title(md_content):
    """
    Collects simple markdown links with title.
    E.g.: [click here](http://haha.com "This is title")
    """
    title_links_list = []
    # (?>!\!) -> exclude images
    # \[[^[]+\] -> matches anything in square brackets []
    # \([^#][^(]+\) -> matches anything in brackets (), except
    # anchor links that start with hashtag (#)
    title_links = re.findall(
        r'(?<!\!)\[[^[]+\]\([^#][^(]+"[^"]+"\)', md_content)

    # Collect link values from links
    for link in title_links:
        link_value = re.findall(r'(?<=\()[^( ]+(?=\s)', link)[0]
        title_links_list.append(link_value)

    return title_links_list


def get_all_links(md_file):
    """
    Collects all links from a markdown file.
    """

    # Read content of markdown file
    with open(md_file, 'r') as open_md_file:
        content = open_md_file.read()

    # Get all types of links and concatenate results
    return get_simple_links(content) + \
        get_links_with_title(content) + \
        get_reference_links(content)


def get_md_files(root_dir):
    """
    Collects markdown files from a directory.
    """
    paths_to_files = []

    # Traverse root directory going down in search for md files
    for root, _, files in os.walk(root_dir):

        for name in files:

            # If a file is markdown, add path to it to list
            if '.md' in name:
                file_path = os.path.join(root, name)
                paths_to_files.append(file_path)

    return paths_to_files


def check_links_in_dir(root_dir):
    """
    Checks all links in all markdown files
    in a directory.
    """

    if not os.path.isdir(root_dir):
        print(console_message('error', 'not_directory', root_dir))
        return ('error', 'not_directory', root_dir)

    # Collect markdown files
    md_files = get_md_files(root_dir)
    number_of_files = len(md_files)

    # Start state for link statistics
    total_links = 0
    error_links = []

    if number_of_files == 0:
        print(console_message('warn', 'no_markdown_files', root_dir))
        return ('warn', 'no_markdown_files', root_dir)

    # Check links in all collected files
    for md_file in md_files:

        # Tell which file is being checked
        print(console_message(
            'info',
            'check_message',
            md_file,
            with_tag=False))

        # Collect links from file
        links_to_check = get_all_links(md_file)

        # Get number of links in file and add to total
        number_of_links = len(links_to_check)
        total_links += number_of_links

        # Links checked in file.
        print(console_message('info',
                              'no_of_links_file',
                              number_of_links,
                              with_tag=False,
                              with_color=False))

        # Check all links in file
        for link in links_to_check:
            (tag, message) = check_link(link)

            # If http/https is missing, link might be relative link
            # If link is a valid file path, check is successful
            if message == 'invalid_protocol' and is_rel_link(md_file, link):
                tag = 'ok'
                message = 'check_rel_link_message'

            # If cannot open link, send error message and add link to list
            if tag == 'error':
                print(console_message(tag, message, link))
                error_links.append(link + ' in ' + md_file)

            if tag == 'warn':
                print(console_message(tag, message, link))

            if tag == 'ok':
                print(console_message(tag, message, link,
                                      with_tag=False, with_color=False))

    # Total number of files and links checked.
    print(console_message('info',
                          'no_of_files',
                          number_of_files,
                          with_tag=False))
    print(console_message('info',
                          'no_of_links_total',
                          total_links,
                          with_tag=False))

    # If any broken link is found, print list of error links
    number_of_broken_links = len(error_links)
    if number_of_broken_links > 0:
        print(console_message('error', 'error_count_message',
                              "\n".join(error_links), with_tag=False))
        return ('error', 'error_count_message', error_links)

    # Otherwise print all fine
    print(console_message('ok', 'all_good_message', root_dir))
    return ('ok', 'all_good_message', root_dir)
