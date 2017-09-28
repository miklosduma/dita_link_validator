import pytest

test_files_dir = 'dita_link_validator/tests/test_files'
test_file = '%s/sample_markdown1.md' % (test_files_dir)


image_links = [
    'https://gitter.im/sparkl/support?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge']
internal_links = ['#bulk-importing-all-example-configurations']

expected_links_with_title = ['https://www.python.org/downloads/']

expected_simple_links = ['http://docs.sparkl.com/',
                         'https://git-scm.com/downloads',
                         'https://github.com/sparkl/cli/releases',
                         'https://saas.sparkl.com',
                         'https://saas.sparkl.com']
expected_reference_links = ['http://docs.sparkl.com/#TopicRoot/Editor/the_editor_c.html',
                            'https://github.com/sparkl/examples/tree/master/Library']

@pytest.fixture(scope="module")
def setup_method():
	"""
	Opens and reads test file for tests.
	After sending content, closes file.
	"""
	open_file = open(test_file, 'r')
	content = open_file.read()
	yield content
	open_file.close()


