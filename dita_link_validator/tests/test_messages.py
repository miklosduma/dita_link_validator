"""
Test cases for messages.
"""

import pytest

from dita_link_validator import messages


def test_message_1():
    """
    Checking success message for running the script
    on a correct file (no colors)
    """

    result = messages.console_message('info',
                                      'check_message',
                                      'file_name',
                                      with_color=False)
    expected = 'INFO: Checking links in file: file_name'
    assert result == expected


def test_message_2():
    """
    Checking status code error message (no colors, no tags).
    """

    result = messages.console_message('error',
                                      'status_code_error',
                                      'link_name',
                                      with_color=False,
                                      with_tag=False)
    expected = 'Browser sent back error status code. Check link: link_name'
    assert result == expected
