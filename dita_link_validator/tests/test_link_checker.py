"""
Tests for general link checking.
"""

import pytest

from dita_link_validator import link_checker


VALID_TAGS = ('error', 'ok')
VALID_MSG_KEYS = ('status_code_error', 'check_link_message',
                  'invalid_url_error', 'connection_error', 'invalid_protocol')


def test_check_link_success():
    """
    Test link checking with existing link.
    Expect to receive: ('ok', 'check_link_message')
    """
    (tag, message_key) = link_checker.check_link('http://google.com')
    expected_tag = 'ok'
    expected_message_key = 'check_link_message'
    assert tag in VALID_TAGS
    assert tag == expected_tag
    assert message_key in VALID_MSG_KEYS
    assert message_key == expected_message_key


def test_check_link_error_1():
    """
    Test link checking with not existing link.
    Expects to receive: ('error', 'connection_error')
    """
    (tag, message_key) = link_checker.check_link('http://no_such_link')
    expected_tag = 'error'
    expected_message_key = 'connection_error'
    assert tag in VALID_TAGS
    assert tag == expected_tag
    assert message_key in VALID_MSG_KEYS
    assert message_key == expected_message_key


def test_check_link_error_2():
    """
    Test link checking with malformed link.
    Expects to receive: ('error', 'invalid_url_error')
    """
    (tag, message_key) = link_checker.check_link('vv')
    expected_tag = 'error'
    expected_message_key = 'invalid_protocol'
    assert tag in VALID_TAGS
    assert tag == expected_tag
    assert message_key in VALID_MSG_KEYS
    assert message_key == expected_message_key


def test_check_link_error_3():
    """
    Test link checking with deleted website (i.e. 404 status code).
    Expects to receive: ('error', 'status_code_error')
    """
    (tag, message_key) = link_checker.check_link(
        'http://sparkl.com/docs/web')
    expected_tag = 'error'
    expected_message_key = 'status_code_error'
    assert tag in VALID_TAGS
    assert tag == expected_tag
    assert message_key in VALID_MSG_KEYS
    assert message_key == expected_message_key
