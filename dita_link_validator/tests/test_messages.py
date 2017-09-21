"""
Test cases for messages.
"""

from unittest import TestCase

from dita_link_validator import messages


class TestMessage(TestCase):
    """
    Class for message tests.
    """

    def test_message_1(self):
        """
        Checking success message for running the script
        on a correct file (no colors)
        """

        result = messages.console_message(
            'ok',
            'check_message',
            'file_name',
            with_color=False)
        expected = 'SUCCESS!!!!! Checking links in file: file_name'
        self.assertEqual(result, expected)

    def test_message_2(self):
        """
        Checking status code error message (no colors, no tags).
        """

        result = messages.console_message('error',
                                          'status_code_error',
                                          'link_name',
                                          with_color=False,
                                          with_tag=False)
        expected = 'Browser sent back error status code. Check link: link_name'
        self.assertEqual(result, expected)
