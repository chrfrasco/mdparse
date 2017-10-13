class TextToken:

    def __init__(self, *, value):
        self.value = value


class HeadingToken:

    def __init__(self, *, level, children):
        if not 1 <= level <= 6:
            raise ValueError('heading level must be between 1 and 6')

        self.level = level
        self.children = children


class GenericToken:
    _available_tokens = ['p', 'u', 's', 'i', 'b']

    def __init__(self, *, children, token_type):
        if token_type not in self._available_tokens:
            raise ValueError('generic token type must be one of %s' % ', '.join(self._available_tokens))

        self.token_type = token_type
        self.children = children
