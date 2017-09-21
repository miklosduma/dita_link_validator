"""
Test cases for collecting and checking links
in case of structured ditamap.
"""

from unittest import TestCase
from dita_link_validator.check_links_dita import links_map_checker


class TestMapChecker(TestCase):
    """
    Class for ditamap check tests.
    """

    test_files_dir = 'dita_link_validator/tests/test_files'

    def test_check_map(self):
        """
        Testing with test ditamap.
        Expects: ('error', 'error_count_message', error_links)
        error_links must include all links in expected_error_links list.
        """
        check_file = '%s/test_links.ditamap' % (TestMapChecker.test_files_dir)

        expected_tag = 'error'
        expected_message_key = 'error_count_message'
        expected_error_links = [
            'http://no-such-link',
            'test_missing_http_schema',
            'htp://test_invalid_protocol']

        (tag,
         message_key,
         error_links) = links_map_checker(check_file)
        self.assertTrue(isinstance(error_links, list))
        self.assertItemsEqual(expected_tag, tag)
        self.assertItemsEqual(expected_message_key, message_key)
        self.assertItemsEqual(expected_error_links, error_links)

    def test_check_map_not_exist(self):
        """
        Testing with non-existent file.
        Must return no such file error.
        """
        check_file = 'no_such_file'
        result = links_map_checker(check_file)
        expected = ('error', 'no_such_file_error', 'no_such_file')
        self.assertItemsEqual(result, expected)

    def test_check_map_not_xml(self):
        """
        Testing with file that is not xml.
        Must return not xml error.
        """
        check_file = 'dita_link_validator/messages.py'
        result = links_map_checker(check_file)
        expected = ('error', 'not_xml_error',
                    'dita_link_validator/messages.py')
        self.assertItemsEqual(result, expected)

    def test_map_with_no_link(self):
        """
        Testing with map that has no external links.
        Must return no links warning.
        """
        check_file = '%s/test_map_no_links.ditamap' % (
            TestMapChecker.test_files_dir)
        result = links_map_checker(check_file)
        expected = ('warning', 'no_links_warn',
                    check_file)
        self.assertItemsEqual(result, expected)
