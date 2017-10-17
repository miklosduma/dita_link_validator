"""
Functions to collect markdown files in a directory
and all links in them.
"""

from __future__ import print_function

import re
import os

from messages import console_message
from link_checker import check_link, is_rel_link, is_wiki_link


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
        link_value = re.findall(r'(?<=\]\()[^()]+(?=\))', link)[0]
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


def get_wiki_page_refs(md_file):
    """
    Collects page references from wiki.
    E.g.: [[Wiki page name]] or [[Link text|Wiki page name]]
    """
    wiki_page_refs_list = []

    with open(md_file, 'r') as open_md_file:
        md_content = open_md_file.read()
        # Find all wiki page ref links
        wiki_page_refs = re.findall(r'\[\[[a-zA-Z 0-9|]+\]\]', md_content)

        # Extract content, removing [[ and ]]
        for w_p_r in wiki_page_refs:
            w_p_r = re.findall(r'(?!\[)[^[]+(?<!\])', w_p_r)[0]

            # If page ref has link text, remove it
            # e.g. [[Link text|Wiki page name]]
            if '|' in w_p_r:
                w_p_r = w_p_r.split('|')[1]

            # Add page name ref to list
            wiki_page_refs_list.append(w_p_r)

        return wiki_page_refs_list


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
    # print(depth)
    return paths_to_files


def find_broken_links(md_file):
    """
    Finds the broken links in a file and returns
    the statistics
    """
    error_links = []
    links_to_check = get_all_links(md_file)
    number_of_links = len(links_to_check)
    print(console_message('info',
                          'no_of_links_file',
                          number_of_links,
                          with_tag=False,
                          with_color=False))

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
            error_links.append(link)

        if tag == 'warn':
            print(console_message(tag, message, link))

        if tag == 'ok':
            print(console_message(tag, message, link,
                                  with_tag=False, with_color=False))

    number_of_error_links = len(error_links)
    return error_links, number_of_links, number_of_error_links


def find_broken_wiki_refs(md_file):
    """
    Finds the broken wiki refs in a file and returns
    the statistics
    """
    error_refs = []
    wiki_refs = get_wiki_page_refs(md_file)
    number_of_wiki_refs = len(wiki_refs)

    for file_path in wiki_refs:

        if not is_wiki_link(md_file, file_path):
            print(console_message('error', 'no_such_file_error', file_path))
            error_refs.append(file_path)

        else:
            print(console_message('ok', 'check_rel_link_message', file_path))

    number_of_error_refs = len(error_refs)
    return error_refs, number_of_wiki_refs, number_of_error_refs


def get_statistics(md_file):
    """
    Get total number of links, wiki page refs
    and error links/references.
    """

    error_links, no_of_links, no_of_error_links = find_broken_links(
        md_file)
    error_refs, no_of_refs, no_of_error_refs = find_broken_wiki_refs(
        md_file)

    # Base statistics.
    file_statistics = {
        'total_links': no_of_links,
        'total_refs': no_of_refs
    }

    # Add error links list and number of error links if any
    if no_of_error_links > 0:
        file_statistics.update(
            {'error_links': error_links, 'error_links_no': no_of_error_links})

    # Add error wiki type ref list and number of them if there are any
    if no_of_error_refs > 0:
        file_statistics.update(
            {'error_refs': error_refs, 'error_refs_no': no_of_error_refs})

    return file_statistics


def print_statistics(statistics):
    """
    Print error links, number of links and so on.
    """

    # Get number of all error links and broken references
    total_error_links = statistics['total_error_links']
    total_error_refs = statistics['total_error_refs']

    # All other keys in statistics dict are path to markdown files
    file_names = [x for x in statistics.keys() if x !=
                  'total_error_links' and x != 'total_error_refs']

    # Print statistics message per markdown file
    for file_name in file_names:

        file_statistics = statistics[file_name]

        # If there are error links print them
        if 'error_links' in file_statistics:
            error_links = file_statistics['error_links']
            print(error_links)
            number_of_error_links = file_statistics.pop('error_links_no')
            print(number_of_error_links)

        # If there are error refs print them
        if 'error_refs' in file_statistics:
            error_refs = file_statistics['error_refs']
            print(error_refs)
            number_of_error_refs = file_statistics.pop('error_refs_no')
            print(number_of_error_refs)
    return


def check_links_in_dir(root_dir):
    """
    Checks all links in all markdown files
    in a directory.
    """

    # Return from fun if not called with valid path to a directory
    if not os.path.isdir(root_dir):
        print(console_message('error', 'not_directory', root_dir))
        return ('error', 'not_directory', root_dir)

    # Collect all markdown files from root dir
    md_files = get_md_files(root_dir)
    number_of_files = len(md_files)

    # Return from fun if there are no markdown files in directory
    if number_of_files == 0:
        print(console_message('warn', 'no_markdown_files', root_dir))
        return ('warn', 'no_markdown_files', root_dir)

    # Starting values for statistics
    statistics = {}
    total_error_refs = 0
    total_error_links = 0

    # Get statistics for files (i.e. number of links/broken links, etc)
    for md_file in md_files:
        file_statistics = get_statistics(md_file)

        # If there are broken links in file add their number to total
        if 'error_links_no' in file_statistics:
            total_error_links += file_statistics['error_links_no']

        # If there are broken wiki page references add their number to total
        if 'error_refs_no' in file_statistics:
            total_error_refs += file_statistics['error_refs_no']

        # Add file statistics to total statistics, file's name being the key
        statistics.update({md_file: file_statistics})

    # When done, update statistics with total number of broken links, etc
    statistics.update({'total_error_refs': total_error_refs,
                       'total_error_links': total_error_links})

    # If no broken links are found print all good message
    if total_error_refs == 0 and total_error_links == 0:
        print(console_message('ok', 'all_good_message', root_dir))
        return statistics

    # Otherwise print error statistics
    print_statistics(statistics)
    return statistics
