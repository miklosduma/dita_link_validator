"""
Test cases for invoking main commands.
"""

import pytest
from dita_link_validator.call_command import call_main


def test_call_no_args():
    """
    Main fun called with no arguments.
    Must return no_args_error message
    """
    args = []
    result = call_main(args)
    tag = result[0]
    message = result[1]
    expected_tag = 'error'
    expected_message = 'no_args_error'
    assert tag == expected_tag
    assert message == expected_message


def test_call_one_arg_only():
    """
    Main fun called with one argument only.
    Must return no_args_error message
    """
    args = ['dita']
    result = call_main(args)
    tag = result[0]
    message = result[1]
    expected_tag = 'error'
    expected_message = 'no_args_error'
    assert tag == expected_tag
    assert message == expected_message
