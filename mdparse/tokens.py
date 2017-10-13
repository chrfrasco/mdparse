class TextToken:

    def __init__(self, *, value):
        self.value = value


class HeadingToken:

    def __init__(self, *, level, children):
        if not 1 <= level <= 6:
            raise ValueError('heading level must be between 1 and 6')

        self.level = level
        self.children = children
