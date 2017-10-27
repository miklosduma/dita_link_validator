"""
Main module supporting command-line options.
"""

from __future__ import print_function
import argparse

from check_links_dita import links_map_checker
from check_links_markdown import check_links_in_dir


def call_main():
    """
    Passes command-line arguments to the call_main function.
    """
    desc = 'Command-line link validator tool.'
    dita_help = ('Specify a ditamap as input to '
                 'check first-level topicrefs with external links in them.')
    markdown_help = ('Specify a folder as input to '
                     'check all markdown files inside for broken links.')

    # Create parser instance
    parser = argparse.ArgumentParser(description=desc)

    # Add verbose True or False based on whether -v flag is specified
    parser.add_argument('-dt', '--dita', help=dita_help, dest='DITAMAP')

    # Add phases in case one or more are specified
    parser.add_argument('-md', '--markdown', help=markdown_help, dest='FOLDER')

    # Get command-line arguments
    args = parser.parse_args()

    # Depending on command options call either function
    if args.DITAMAP:
        return links_map_checker(args.DITAMAP)
    if args.FOLDER:
        return check_links_in_dir(args.FOLDER)

    # Or print help message if neither option was specified
    return parser.print_help()

# Call from command line. Args are gathered from terminal input
if __name__ == "__main__":
    call_main()
