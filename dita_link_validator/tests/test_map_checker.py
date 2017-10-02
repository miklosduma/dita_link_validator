"""
Test cases for collecting and checking links
in case of structured ditamap.
"""

import pytest
from dita_link_validator.check_links_dita import links_map_checker
from dita_link_validator.tests.conftest import TEST_FILES_DIR


def test_check_map():
    """
    Testing with test ditamap.
    Expects: ('error', 'error_count_message', error_links)
    error_links must include all links in expected_error_links list.
    """
    check_file = '%s/dita/test_links.ditamap' % (TEST_FILES_DIR)

    expected_tag = 'error'
    expected_message_key = 'error_count_message'
    expected_error_links = [
        'http://no-such-link',
        'test_missing_http_schema',
        'htp://test_invalid_protocol']

    (tag,
     message_key,
     error_links) = links_map_checker(check_file)
    assert isinstance(error_links, list)
    assert tag == expected_tag
    assert message_key == expected_message_key
    assert error_links == expected_error_links


def test_check_map_not_exist():
    """
    Testing with non-existent file.
    Must return no such file error.
    """
    check_file = 'no_such_file'
    result = links_map_checker(check_file)
    expected = ('error', 'no_such_file_error', 'no_such_file')
    assert result == expected


def test_check_map_not_xml():
    """
    Testing with file that is not xml.
    Must return not xml error.
    """
    check_file = 'dita_link_validator/messages.py'
    result = links_map_checker(check_file)
    expected = ('error', 'not_xml_error',
                'dita_link_validator/messages.py')
    assert result == expected


def test_map_with_no_link():
    """
    Testing with map that has no external links.
    Must return no links warning.
    """
    check_file = '%s/dita/test_map_no_links.ditamap' % (
        TEST_FILES_DIR)
    result = links_map_checker(check_file)
    expected = ('warn', 'no_links_warn',
                check_file)
    assert result == expected
