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

    def test_generic_empty(self):
        tokens = [GenericToken(children=[], token_type='p')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<p></p>')

    def test_generic_paragrpah(self):
        tokens = [GenericToken(children=[TextToken(value='Hello, world!')], token_type='p')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<p>Hello, world!</p>')

    def test_generic_italic(self):
        tokens = [GenericToken(children=[TextToken(value='Hello, world!')], token_type='i')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<i>Hello, world!</i>')

    def test_generic_strikethrough(self):
        tokens = [GenericToken(children=[TextToken(value='Hello, world!')], token_type='s')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<s>Hello, world!</s>')

    def test_generic_bold(self):
        tokens = [GenericToken(children=[TextToken(value='Hello, world!')], token_type='b')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<b>Hello, world!</b>')

    def test_generic_underline(self):
        tokens = [GenericToken(children=[TextToken(value='Hello, world!')], token_type='u')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<u>Hello, world!</u>')

    def test_generic_chain(self):
        tokens = [GenericToken(children=[GenericToken(children=[TextToken(value='Hello, world!')], token_type='b')], token_type='p')]
        html = HTMLRenderer.render_tokens(tokens)

        self.assertEqual(html, '<p><b>Hello, world!</b></p>')


if __name__ == '__main__':
    unittest.main()
