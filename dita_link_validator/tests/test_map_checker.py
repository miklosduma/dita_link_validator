from unittest import TestCase

from dita_link_validator import link_checker


class TestMapChecker(TestCase):

	# Testing with test ditamap. Should return all links in expected_error_links list
    def test_check_map(self):
        check_file = 'dita_link_validator/tests/test_files/test_links.ditamap'
        expected_error_links = ['http://no-such-link', 'missing_http_schema']
        (tag, message_key, error_links) = link_checker.links_map_checker(check_file)
        self.assertTrue(isinstance(expected_error_links, list))
        self.assertItemsEqual(expected_error_links,error_links)

    # Testing with non-existent file. Should return no such file error
    def test_check_map_not_exist(self):
        check_file = 'no_such_file'
        result = link_checker.links_map_checker(check_file)
        expected = ('error', 'no_such_file_error', 'no_such_file')
        self.assertItemsEqual(result,expected)

    # Testing with file that is not xml. Should return not xml error
    def test_check_map_not_xml(self):
        check_file = 'dita_link_validator/messages.py'
        result = link_checker.links_map_checker(check_file)
        expected = ('error', 'not_xml_error', 'dita_link_validator/messages.py')
        self.assertItemsEqual(result,expected)
