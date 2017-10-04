"""
Configuration for markdown tests.
"""

import pytest

TEST_FILES_DIR = 'dita_link_validator/tests/test_files'
TEST_FILE_1 = '%s/markdown/sample_markdown1.md' % (TEST_FILES_DIR)
TEST_FILE_2 = '%s/markdown/sample_md_relative.md' % (TEST_FILES_DIR)
TEST_FILE_3 = '%s/markdown/sample_md_broken.md' % (TEST_FILES_DIR)


IMAGE_LINKS_1 = [
    'https://gitter.im/sparkl/support?utm_source=badge'
    '&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge']
INTERNAL_LINKS_1 = ['#bulk-importing-all-example-configurations']

EXPECTED_LINKS_TITLE_1 = ['https://www.python.org/downloads/']

EXPECTED_SIMPLE_LINKS_1 = ['http://docs.sparkl.com/',
                           'https://git-scm.com/downloads',
                           'https://github.com/sparkl/cli/releases',
                           'https://python-xy.github.io',
                           'https://saas.sparkl.com',
                           'https://saas.sparkl.com']
EXPECTED_REFERENCE_LINKS_1 = ['http://docs.sparkl.com/#TopicRoot/'
                              'Editor/the_editor_c.html',
                              'https://github.com/sparkl/examples'
                              '/tree/master/Library']

EXPECTED_WIKI_PAGE_REFS = ['sample markdown1', 'sample md broken']


@pytest.fixture(scope="module")
def setup_method():
    """
    Opens and reads test file for tests.
    After sending content, closes file.
    """
    open_file = open(TEST_FILE_1, 'r')
    content = open_file.read()
    yield content
    open_file.close()
