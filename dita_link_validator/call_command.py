from __future__ import print_function
import sys

from messages import console_message
from check_links_dita import links_map_checker
from check_links_markdown import check_links_in_dir


def call_main(args):

    valid_options = ['dita', 'markdown']

    try:
        command_option = args[1]
        command_target = args[2]

    except IndexError:
        print("ERRRROROROROR")
        return

    if command_option not in valid_options:
        print('Invalid command option')
        return

    if command_option == 'dita':
        return links_map_checker(command_target)

    if command_option == 'markdown':
        return check_links_in_dir(command_target)

if __name__ == "__main__":
    # Only calls command if minimum one argument is specified (command itself
    # is an element in sys.argv list)
    call_main(sys.argv)
