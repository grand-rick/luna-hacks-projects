#!/usr/bin/env python3
import unittest
from shorten import UrlShortener
"""
Test suties for the module
"""

class TestUrlShortener(unittest.TestCase):
    """
    Test cases for this module
    """

    @classmethod
    def setUp(self):
        """
        Setup resources to be used 
        """
        self.obj = UrlShortener()

    @classmethod
    def tearDown(self):
        """
        Free resources after running the tests
        """
        del self.obj

    def test_documentation(self):
        """
        Test documentation for the module
        classes and methods
        """
        self.assertIsNotNone(self.__class__.__doc__)
        self.assertIsNotNone(UrlShortener.__doc__)

    def test_shortening(self):
        """
        Test to assertain that the url is actually shortened
        """
        # urls = self.obj.generate_short_url()
        # self.assertNotEqual(urls["url"], second["short_url"])
        pass


if __name__ == "__main__":
    TestUrlShortener().main()