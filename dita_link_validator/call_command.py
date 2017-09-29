from __future__ import print_function
import sys

from messages import console_message
from check_links_dita import links_map_checker
from check_links_markdown import check_links_in_dir


def call_main(args):
    """
    Main function to call either dita or markdown
    link checker funs.
    """

    # First positional arguments
    valid_options = ['dita', 'markdown']

    # Check if command is called with two arguments
    try:
        command_option = args[1]
        command_target = args[2]

    # Do nothing if not.
    except IndexError:
        print(console_message('error', 'no_args_error', ''))
        return ('error', 'no_args_error', '')

    # First positional argument must be dita or markdown
    if command_option not in valid_options:
        print(console_message('error', 'invalid_arg_error', command_option))
        return ('error', 'invalid_arg_error', command_option)

    # For dita call checker fun on second argument
    # Second arg must be a ditamap. This is handled in links_map_checker
    if command_option == 'dita':
        return links_map_checker(command_target)

    # For markdown call checker fun on second argument
    # Second arg must be a directory. This is handled in check_links_in_dir
    if command_option == 'markdown':
        return check_links_in_dir(command_target)

# Call from command line. Args are gathered from terminal input
if __name__ == "__main__":
    call_main(sys.argv)
