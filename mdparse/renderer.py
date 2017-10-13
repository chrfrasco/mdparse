from .tokens import *

class Renderer:

    def render_tokens(cls, tokens):
        raise NotImplementedError

    def render_token(cls, token):
        raise NotImplementedError

    def render_TextToken(cls, token):
        raise NotImplementedError

    def render_HeadingToken(cls, token):
        raise NotImplementedError


class HTMLRenderer:

    @classmethod
    def render_tokens(cls, tokens):
        html_chunks = map(cls.render_token, tokens)
        return '\n'.join(html_chunks)

    @classmethod
    def render_token(cls, token):
        render_method = 'render_' + token.__class__.__name__
        render = getattr(cls, render_method)

        return render(token)

    @classmethod
    def render_TextToken(cls, token):
        return token.value

    @classmethod
    def render_HeadingToken(cls, token):
        inner_html = cls.render_tokens(token.children)
        h = f'h{token.level}'
        return f'<{h}>{inner_html}</{h}>'

