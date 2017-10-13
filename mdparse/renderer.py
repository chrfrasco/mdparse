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

    def render_GenericToken(cls, token):
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
        return '<h{level}>{inner_html}</h{level}>'.format(level=token.level, inner_html=inner_html)

    @classmethod
    def render_GenericToken(cls, token):
        inner_html = cls.render_tokens(token.children)
        return '<{token_type}>{inner_html}</{token_type}>'.format(token_type=token.token_type, inner_html=inner_html)
