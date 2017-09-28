import pytest

from dita_link_validator import check_links_markdown as clm
from conftest import (test_file, expected_links_with_title,
                      expected_simple_links, expected_reference_links)


def test_simple_links(setup_method):
    """
    Checking if fun manages to collect all simple links
    and only simple links from a markdown file
    [text](link)
    """
    simple_links = clm.get_simple_links(setup_method)
    simple_links.sort()
    assert simple_links == expected_simple_links


def test_link_title(setup_method):
    """
    Checking if fun manages to collect all simple links with titles
    and only them from a markdown file
    [text](link "navtitle")
    """
    links_with_title = clm.get_links_with_title(setup_method)
    links_with_title.sort()
    assert links_with_title == expected_links_with_title


def test_link_reference(setup_method):
    """
    Checking if fun manages to collect reference-type
    links and only those
    [Book of Knowledge][1]
    [1]: http://book.knowledge.com
    """
    reference_links = clm.get_reference_links(setup_method)
    reference_links.sort()
    assert reference_links == expected_reference_links


def test_get_all_links():
    """
    Checking if manages to get all links from file.
    """
    expected_all_links = expected_links_with_title + \
        expected_simple_links + expected_reference_links
    expected_all_links.sort()
    all_links = clm.get_all_links(test_file)
    all_links.sort()
    assert all_links == expected_all_links
