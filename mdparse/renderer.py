from .tokens import *

def render_html_from_tokens(tokens):
    return "\n".join(render_html_from_token(token) for token in tokens)


def render_html_from_token(token):
    if token.type == TEXT_TOKEN:
        return render_text_token(token)
    elif token.type == HEADING_TOKEN:
        return render_heading_token(token)
    else:
        return render_generic_token(token)


def render_text_token(token):
    return token.value


def render_heading_token(token):
    inner_html = render_html_from_tokens(token.children)
    return '<h{level}>{inner_html}</h{level}>'.format(level=token.level, inner_html=inner_html)


def render_generic_token(token):
    inner_html = render_html_from_tokens(token.children)
    return '<{token_type}>{inner_html}</{token_type}>'.format(token_type=token.token_type, inner_html=inner_html)
