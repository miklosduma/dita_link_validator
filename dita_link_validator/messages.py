"""
Contains all messages for package.
Also a function to format messages for terminal output.
"""

from termcolor import colored

# List of messages returned in terminal. Used in console_message fun
MESSAGES = {
    'check_message':
        'Checking links in file: ',
    'no_markdown_files':
        'No markdown files in directory: ',
    'not_directory':
        'Not a directory: ',
    'check_link_message':
        'Link checked: ',
    'all_good_message':
        'No broken links found in: ',
    'no_links_warn':
        'Links ditamap not well-formed or no external links in file: ',
    'no_ditamap_warn':
        'Based on filename, file is not a ditamap: ',
    'not_xml_error':
        'File is not a well-formed xml file: ',
    'status_code_error':
        'Browser sent back error status code. Check link: ',
    'auth_warn':
        'No permission to open link: ',
    'invalid_url_error':
        'Link is not well-formed. Check link in your browser: ',
    'invalid_protocol':
        'Link does not start with http/https protocol.\n'
        'Check link in your browser: ',
    'connection_error':
        'Failed to connect to link: ',
    'no_such_file_error':
        'Could not find file: ',
    'error_count_message':
        'Links to be checked:\n',
    'file_not_spec_error':
        'Specify a ditamap file for the command.\n'
        'For example: python call_command.py dita foo.ditamap',
    'no_args_error':
        'Command takes two arguments.\n'
        'For example: [cmd] markdown path_to_folder',
    'invalid_arg_error':
        'First argument must be markdown or dita.\n'
        'Invalid argument: '
}

# List of message tags and colors used in console_message fun. Tags and
# colors are all optional
MESSAGE_TYPES = {
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


def console_message(msg_type, key, arg, with_color=True, with_tag=True):
    """
    Constructs message based on:
      * type (i.e. 'info' or 'error')
      * message key (i.e. 'check_message' or 'invalid_url_error')
      * arg (a variable, such as a link or file name)
    """
    message = ''.join((MESSAGES[key], arg))

    # If with_tag is set to true (default), tag corresponding to type is used
    # as prefix to the message
    if with_tag:
        tag = MESSAGE_TYPES[msg_type]['tag']
        message = ' '.join((tag, message))

    # If with_color is set to true (default), color corresponding to type is
    # used to format the message
    if with_color:
        color = MESSAGE_TYPES[msg_type]['color']
        return colored(message, color)

    return message
