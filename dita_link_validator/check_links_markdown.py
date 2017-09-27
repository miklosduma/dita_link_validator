import re
import glob
import os
import requests
import sys

from termcolor import colored

target_file = 'README.md'
target_folder = '../../examples'
target_folder2 = '../../sparkl_cli.wiki'

messages = {
    'check_message': 'Checking links in file:',
    'check_link_message': 'Link checked:',
    'all_good_message': 'No broken links found in ditamap:',
    'no_links_warn': 'Links ditamap not well-formed or no external links to check in file:',
    'no_ditamap_warn': 'Based on filename, file is not a ditamap:',
    'not_xml_error': 'File is not a well-formed xml file: ',
    'status_code_error': 'Browser sent back error status code. Check link:',
    'invalid_url_error': 'Link is not well-formed. Check link in your browser:',
    'connection_error': 'Failed to connect to link:',
    'no_such_file_error': 'Could not find file:',
    'error_count_message': 'Links to be checked:',
    'file_not_spec_error': 'Specify a ditamap file for the command. For example: python links_map_checker.py foo.ditamap'
}

# List of message tags and colors used in console_message fun. Tags and
# colors are all optional
message_types = {
    'ok': {
        'color': 'green',
        'tag': 'SUCCESS!!!!!'
    },
    'error': {
        'color': 'red',
        'tag': 'ERROR!!!!!'
    },
    'warning': {
        'color': 'yellow',
        'tag': 'WARNING!!!!!'
    },
    'info': {
        'color': 'blue',
        'tag': 'INFO:'
    }
}


def console_message(type, key, arg, with_color=True, with_tag=True):
    """
    Constructs message based on:
      * type (i.e. 'info' or 'error')
      * message key (i.e. 'check_message' or 'invalid_url_error')
      * arg (a variable, such as a link or file name)
    """
    message = ' '.join((messages[key], arg))

    # If with_tag is set to true (default), tag corresponding to type is used
    # as prefix to the message
    if with_tag:
        tag = message_types[type]['tag']
        message = ' '.join((tag, message))

    # If with_color is set to true (default), color corresponding to type is
    # used to format the message
    if with_color:
        color = message_types[type]['color']
        return colored(message, color)

    return message


def is_protocol_correct(link):
    """
    Correct protocols are https and http. Function returns False if start of link does not match either.
    """
    return link.startswith('http', 0, 4) or link.startswith('https', 0, 5)


def check_link(link):
    """
    Pings link and sends back response tuple (tag,message_key) for console_message fun
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


def get_md_links(md_file):
    file = open(md_file, 'r')
    content = file.read()
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

# get_md_links(target_file)


def get_files(root_dir):
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
        (link, file) = link_tuple
        # print "Checking %s" % (link)
        (tag, message) = check_link(link)
        max_links_checked += 1
        if tag == 'error':
            print "Error, failed to open %s in %s." % (link, file)
    print "Files checked: %s" % (max_files_checked)
    print "Links checked: %s" % (max_links_checked)
    return

get_files(target_folder2)
