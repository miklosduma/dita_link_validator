import pytest

from dita_link_validator import check_links_markdown as clm

test_files_dir = 'dita_link_validator/tests/test_files'
test_file = '%s/sample_markdown1.md' % (test_files_dir)


image_links = [
    'https://gitter.im/sparkl/support?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge']
internal_links = ['#bulk-importing-all-example-configurations']

expected_links_with_title = ['https://www.python.org/downloads/']

expected_simple_links = ['http://docs.sparkl.com/',
                         'http://docs.sparkl.com/#TopicRoot/Editor/the_editor_c.html',
                         'https://git-scm.com/downloads',
                         'https://github.com/sparkl/cli/releases',
                         'https://github.com/sparkl/examples/tree/master/Library',
                         'https://saas.sparkl.com',
                         'https://saas.sparkl.com']


open_file = open(test_file, 'r')
content = open_file.read()


def test_simple_links():
    """
    Checking if fun manages to collect all simple links
    and only simple links from a markdown file
    """
    simple_links = clm.get_simple_links(content)
    simple_links.sort()
    assert simple_links == expected_simple_links

def test_link_title():
    """
    Checking if fun manages to collect all simple links with titles
    and only them from a markdown file
    """
    links_with_title = clm.get_links_with_title(content)
    links_with_title.sort()
    assert links_with_title == expected_links_with_title
