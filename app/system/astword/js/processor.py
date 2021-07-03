from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaScriptParser import JavaScriptParser
    from .JavaScriptLexer import JavaScriptLexer
    from .JavaScriptParserListener import JavaScriptParserListener
else:
    from JavaScriptParser import JavaScriptParser
    from JavaScriptLexer import JavaScriptLexer
    from JavaScriptParserListener import JavaScriptParserListener


class WordListener(JavaScriptParserListener):
    def __init__(self):
        self.words = []

    def enterVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        self.words.append(ctx.getChild(0).getText())

    def enterArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        if ctx.getChildCount() > 2:
            self.words.extend(ctx.getChild(1).getText().split(','))

    def enterFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        if ctx.getChildCount() > 2:
            self.words.extend(ctx.getChild(1).getText().split(','))

    def enterFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        self.words.append(ctx.getChild(1).getText())
        


def get_words(filepath):
    parser = JavaScriptParser(CommonTokenStream(JavaScriptLexer(FileStream(filepath, encoding="utf-8"))))
    walker = ParseTreeWalker()
    listener = WordListener()
    walker.walk(listener, parser.program())

    return listener.words
