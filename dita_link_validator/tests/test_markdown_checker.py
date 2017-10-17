"""
Test cases for markdown file collection.
"""

import pytest
from dita_link_validator.check_links_markdown import check_links_in_dir
from conftest import (TEST_FILES_DIR,
                      TEST_FILE_1,
                      TEST_FILE_2,
                      TEST_FILE_3,
                      EXPECTED_ERROR_WIKI_REFS,
                      EXPECTED_ERROR_LINKS)


def test_no_files_in_dir():
    """
    Run function on dir with no md files in it.
    Must receive warning with no markdown files message.
    """
    no_md_dir = '%s/dita' % (TEST_FILES_DIR)
    (tag, message_key, argument) = check_links_in_dir(no_md_dir)
    expected_tag = 'warn'
    expected_message_key = 'no_markdown_files'

    assert tag == expected_tag
    assert message_key == expected_message_key
    assert argument == no_md_dir


def test_not_dir():
    """
    Run function on file instead of dir.
    Must receive error with not directory error message.
    """
    (tag, message_key, argument) = check_links_in_dir(TEST_FILE_1)
    expected_tag = 'error'
    expected_message_key = 'not_directory'

    assert tag == expected_tag
    assert message_key == expected_message_key
    assert argument == TEST_FILE_1


def test_md_full():
    """
    Call markdown link collection and checking.
    Expects to find broken links.
    """
    statistics = check_links_in_dir(TEST_FILES_DIR)
    total_error_refs = statistics['total_error_refs']
    total_error_links = statistics['total_error_links']
    expected_keys = [TEST_FILE_1, TEST_FILE_2, TEST_FILE_3,
                     'total_error_refs', 'total_error_links']
    errors_in_test_file_1 = statistics[TEST_FILE_1]['error_refs']
    errors_in_test_file_3 = statistics[TEST_FILE_3]['error_links']
    #errors_in_test_file_3 = statistics[TEST_FILE_3]['error_links']

    #error_links = statistics['error_links']
    #error_refs = statistics['error_refs']

    assert total_error_refs == 1
    assert total_error_links == 1
    assert all(key in expected_keys for key in statistics.keys())
    assert errors_in_test_file_1 == EXPECTED_ERROR_WIKI_REFS
    assert errors_in_test_file_3 == EXPECTED_ERROR_LINKS

    """
    assert tag == 'error'
    assert message_key == 'error_count_message'
    assert any('sample_file_non.md' in link for link in error_links)
    """
