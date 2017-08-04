from unittest import TestCase

from dita_link_validator import link_checker


valid_tags = ('error', 'ok')
valid_message_keys = ('status_code_error', 'check_link_message',
	                      'invalid_url_error', 'connection_error')

class TestLinkChecker(TestCase):

    def test_check_link_success(self):
        (tag,message_key) = link_checker.check_link('http://google.com')
        expected_tag = 'ok' 
        expected_message_key = 'check_link_message'
        self.assertTrue(tag in valid_tags and message_key in valid_message_keys)
        self.assertEqual(tag,expected_tag)
        self.assertEqual(message_key,expected_message_key)

    def test_check_link_error_1(self):
        (tag,message_key) = link_checker.check_link('http://no_such_link')
        expected_tag = 'error'
        expected_message_key = 'connection_error'
        self.assertTrue(tag in valid_tags and message_key in valid_message_keys)
        self.assertEqual(tag,expected_tag)
        self.assertEqual(message_key,expected_message_key)

    def test_check_link_error_2(self):
        (tag,message_key) = link_checker.check_link('vv')
        expected_tag = 'error'
        expected_message_key = 'invalid_url_error'
        self.assertTrue(tag in valid_tags and message_key in valid_message_keys)
        self.assertEqual(tag,expected_tag)
        self.assertEqual(message_key,expected_message_key)

    def test_check_link_error_3(self):
        (tag,message_key) = link_checker.check_link('http://sparkl.com/docs/web')
        expected_tag = 'error'
        expected_message_key = 'status_code_error'
        self.assertTrue(tag in valid_tags and message_key in valid_message_keys)
        self.assertEqual(tag,expected_tag)
        self.assertEqual(message_key,expected_message_key)
