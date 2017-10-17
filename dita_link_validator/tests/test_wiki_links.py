"""
Tests for markdown wiki type link discovery.
"""

from dita_link_validator.link_checker import is_wiki_link
from dita_link_validator.tests.conftest import TEST_FILE_1


def test_is_wiki_link():
    link1 = 'sample markdown1'
    link2 = 'sample md broken'

    assert is_wiki_link(TEST_FILE_1, link1)
    assert is_wiki_link(TEST_FILE_1, link2)
