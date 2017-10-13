import unittest

from mdparse.renderer import *


class TestHTMLRenderer(unittest.TestCase):

    def test_empty_tokens(self):
        tokens = []
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '')

    def test_text(self):
        tokens = [TextToken(value='Hello, world!')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, 'Hello, world!')

    def test_empty_heading(self):
        tokens = [HeadingToken(children=[], level=1)]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<h1></h1>')

    def test_heading(self):
        tokens = [HeadingToken(children=[TextToken(value='Hello, world!')], level=1)]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<h1>Hello, world!</h1>')


if __name__ == '__main__':
    unittest.main()
