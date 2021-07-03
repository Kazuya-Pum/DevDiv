from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
    from .Python3Lexer import Python3Lexer
    from .Python3Listener import Python3Listener
else:
    from Python3Parser import Python3Parser
    from Python3Lexer import Python3Lexer
    from Python3Listener import Python3Listener


class WordListener(Python3Listener):
    def __init__(self):
        self.words = []

    def enterArglist(self, ctx:Python3Parser.ArglistContext):
        self.words.extend([child.getText() for child in ctx.getChildren()])


def get_words(filepath):
    parser = Python3Parser(CommonTokenStream(Python3Lexer(FileStream(filepath, encoding="utf-8"))))
    walker = ParseTreeWalker()
    listener = WordListener()
    walker.walk(listener, parser.file_input())

    return listener.words
