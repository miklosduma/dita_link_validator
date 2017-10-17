"""
Contains all messages for package.
Also a function to format messages for terminal output.
"""

from termcolor import colored

# List of messages returned in terminal. Used in console_message fun
MESSAGES = {

    # Success messages
    'ok': {
        'color': 'green',
        'tag': 'SUCCESS!!!!!',
        'messages': {
            'check_link_message':
                'Link checked: ',
            'check_rel_link_message':
                'Relative link checked: ',
            'check_wiki_message':
                'Wiki page reference checked: ',
            'all_good_message':
                'No broken links found in: '
        }
    },

    # Error messages
    'error': {
        'color': 'red',
        'tag': 'ERROR!!!!!',
        'messages': {
            'not_directory':
                'Not a directory: ',
            'not_xml_error':
                'File is not a well-formed xml file: ',
            'status_code_error':
                'Browser sent back error status code. Check link: ',
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
                'Broken link(s) found:\n',
            'error_refs_count': 
                'Invalid wiki reference(s) found:\n',
            'file_not_spec_error':
                'Specify a ditamap file for the command.\n'
                'For example: python call_command.py dita foo.ditamap',
            'no_args_error':
                'Command takes two arguments.\n'
                'For example: [cmd] markdown path_to_folder',
            'invalid_arg_error':
                'First argument must be markdown or dita.\n'
                'Invalid argument: ',
            'wiki_error':
                'Reference to non-existent wiki page: '
        }
    },

    # Warnings
    'warn': {
        'color': 'yellow',
        'tag': 'WARNING!!!!!',
        'messages': {
            'no_links_warn':
                'Links ditamap not well-formed or no external links in file: ',
            'no_ditamap_warn':
                'Based on filename, file is not a ditamap: ',
            'no_markdown_files':
                'No markdown files in directory: '
        }
    },

    # Informative messages
    'info': {
        'color': 'blue',
        'tag': 'INFO:',
        'messages': {
            'check_message':
                'Checking links in file: ',
            'no_of_links_file':
                'Number of links checked: ',
            'no_of_refs_file':
                'Number of wiki page references checked: ',
            'no_of_links_total':
                'Total number of links checked: ',
            'no_of_files':
                'Number of files collected: ',
            'file_stats':
                'Link statistics in file: '
        }
    }
}


def console_message(msg_type, key, arg, with_color=True, with_tag=True):
    """
    Constructs message based on:
      * type (i.e. 'info' or 'error')
      * message key (i.e. 'check_message' or 'invalid_url_error')
      * arg (a variable, such as a link or file name)
    Collects message text from MESSAGES object

    MESSAGES = {
        msg_type: {
            'color': ,
            'tag': ,
            'messages': {
                key: 'This is the actual text'
            }
        }
    }
    """
    # Arg is a link, path or number. Make sure it is string
    arg = str(arg)

    # Get text of message from MESSAGES object
    message_text = MESSAGES[msg_type]['messages'][key]

    # Append message with argument
    message = ''.join((message_text, arg))

    # If with_tag is set to true (default), tag corresponding to type is used
    # as prefix to the message
    if with_tag:
        tag = MESSAGES[msg_type]['tag']
        message = ' '.join((tag, message))

    # If with_color is set to true (default), color corresponding to type is
    # used to format the message
    if with_color:
        color = MESSAGES[msg_type]['color']
        return colored(message, color)

    return message
