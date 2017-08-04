from unittest import TestCase

from dita_link_validator import link_checker

check_file = 'dita_link_validator/tests/test_files/test_links.ditamap'

class TestMapChecker(TestCase):

    def test_check_map(self):
        result = link_checker.links_map_checker(check_file)
        self.assertTrue(isinstance(result,list))
        