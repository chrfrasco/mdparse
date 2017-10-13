import unittest

from mdparse.tokens import *


class TestTokens(unittest.TestCase):

    def test_heading_range_exception(self):
        self.assertRaises(ValueError, HeadingToken, children=[], level=0)
        self.assertRaises(ValueError, HeadingToken, children=[], level=7)

    def test_invalid_generic_token_type(self):
        self.assertRaises(ValueError, GenericToken, children=[], token_type='bad')


if __name__ == '__main__':
    unittest.main()
