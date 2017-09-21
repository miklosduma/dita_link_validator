"""
Tests for general link checking.
"""

from unittest import TestCase

from dita_link_validator import link_checker


VALID_TAGS = ('error', 'ok')
VALID_MSG_KEYS = ('status_code_error', 'check_link_message',
                  'invalid_url_error', 'connection_error')


class TestLinkChecker(TestCase):
    """
    Class for link check tests.
    """

    def test_check_link_success(self):
        """
        Test link checking with existing link.
        Expect to receive: ('ok', 'check_link_message')
        """
        (tag, message_key) = link_checker.check_link('http://google.com')
        expected_tag = 'ok'
        expected_message_key = 'check_link_message'
        self.assertTrue(
            tag in VALID_TAGS and message_key in VALID_MSG_KEYS)
        self.assertEqual(tag, expected_tag)
        self.assertEqual(message_key, expected_message_key)

    def test_check_link_error_1(self):
        """
        Test link checking with not existing link.
        Expects to receive: ('error', 'connection_error')
        """
        (tag, message_key) = link_checker.check_link('http://no_such_link')
        expected_tag = 'error'
        expected_message_key = 'connection_error'
        self.assertTrue(
            tag in VALID_TAGS and message_key in VALID_MSG_KEYS)
        self.assertEqual(tag, expected_tag)
        self.assertEqual(message_key, expected_message_key)

    def test_check_link_error_2(self):
        """
        Test link checking with malformed link.
        Expects to receive: ('error', 'invalid_url_error')
        """
        (tag, message_key) = link_checker.check_link('vv')
        expected_tag = 'error'
        expected_message_key = 'invalid_url_error'
        self.assertTrue(
            tag in VALID_TAGS and message_key in VALID_MSG_KEYS)
        self.assertEqual(tag, expected_tag)
        self.assertEqual(message_key, expected_message_key)

    def test_check_link_error_3(self):
        """
        Test link checking with deleted website (i.e. 404 status code).
        Expects to receive: ('error', 'status_code_error')
        """
        (tag, message_key) = link_checker.check_link(
            'http://sparkl.com/docs/web')
        expected_tag = 'error'
        expected_message_key = 'status_code_error'
        self.assertTrue(
            tag in VALID_TAGS and message_key in VALID_MSG_KEYS)
        self.assertEqual(tag, expected_tag)
        self.assertEqual(message_key, expected_message_key)
