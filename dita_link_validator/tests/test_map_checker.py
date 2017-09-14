from unittest import TestCase

from dita_link_validator import link_checker


class TestMapChecker(TestCase):

        # Testing with test ditamap. Should return all links in
        # expected_error_links list
    def test_check_map(self):
        check_file = 'dita_link_validator/tests/test_files/test_links.ditamap'
        expected_error_links = [
            'http://no-such-link', 'test_missing_http_schema', 'htp://test_invalid_protocol']
        (tag, message_key, error_links) = link_checker.links_map_checker(check_file)
        self.assertTrue(isinstance(error_links, list))
        self.assertItemsEqual(expected_error_links, error_links)

    # Testing with non-existent file. Should return no such file error
    def test_check_map_not_exist(self):
        check_file = 'no_such_file'
        result = link_checker.links_map_checker(check_file)
        expected = ('error', 'no_such_file_error', 'no_such_file')
        self.assertItemsEqual(result, expected)

    # Testing with file that is not xml. Should return not xml error
    def test_check_map_not_xml(self):
        check_file = 'dita_link_validator/messages.py'
        result = link_checker.links_map_checker(check_file)
        expected = ('error', 'not_xml_error',
                    'dita_link_validator/messages.py')
        self.assertItemsEqual(result, expected)

    # Testing with map that has no external links
    def test_map_with_no_link(self):
        check_file = 'dita_link_validator/tests/test_files/test_map_no_links.ditamap'
        result = link_checker.links_map_checker(check_file)
        expected = ('warning', 'no_links_warn',
                    'dita_link_validator/tests/test_files/test_map_no_links.ditamap')
        self.assertItemsEqual(result, expected)
