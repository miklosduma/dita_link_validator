"""
Tests for markdown regex link finders.
"""

from dita_link_validator import check_links_markdown as clm
from dita_link_validator.tests.conftest import (TEST_FILE_1, TEST_FILES_DIR,
                                                EXPECTED_LINKS_TITLE_1,
                                                EXPECTED_SIMPLE_LINKS_1,
                                                EXPECTED_REFERENCE_LINKS_1)


def test_simple_links(setup_method):
    """
    Checking if fun manages to collect all simple links
    and only simple links from a markdown file
    [text](link)
    """
    simple_links = clm.get_simple_links(setup_method)
    simple_links.sort()
    assert simple_links == EXPECTED_SIMPLE_LINKS_1


def test_link_title(setup_method):
    """
    Checking if fun manages to collect all simple links with titles
    and only them from a markdown file
    [text](link "navtitle")
    """
    links_with_title = clm.get_links_with_title(setup_method)
    links_with_title.sort()
    assert links_with_title == EXPECTED_LINKS_TITLE_1


def test_link_reference(setup_method):
    """
    Checking if fun manages to collect reference-type
    links and only those
    [Book of Knowledge][1]
    [1]: http://book.knowledge.com
    """
    reference_links = clm.get_reference_links(setup_method)
    reference_links.sort()
    assert reference_links == EXPECTED_REFERENCE_LINKS_1


def test_get_all_links():
    """
    Checking if manages to get all links from file.
    """
    expected_all_links = EXPECTED_LINKS_TITLE_1 + \
        EXPECTED_SIMPLE_LINKS_1 + EXPECTED_REFERENCE_LINKS_1
    expected_all_links.sort()
    all_links = clm.get_all_links(TEST_FILE_1)
    all_links.sort()
    assert all_links == expected_all_links


def test_find_md_files():
    """
    Check if manages to collect all md files in dir.
    """
    md_files = clm.get_md_files(TEST_FILES_DIR)
    number_of_md_files = len(md_files)
    assert number_of_md_files == 3
