from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaParser import JavaParser
    from .JavaLexer import JavaLexer
    from .JavaParserListener import JavaParserListener
else:
    from JavaParser import JavaParser
    from JavaLexer import JavaLexer
    from JavaParserListener import JavaParserListener


class WordListener(JavaParserListener):
    def __init__(self):
        self.words = []

    def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        self.words.append(ctx.getChild(0).getText())

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        self.words.append(ctx.getChild(1).getText())

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        self.words.append(ctx.getChild(1).getText())

    def enterFormalParameter(self, ctx:JavaParser.FormalParameterContext):
        self.words.append(ctx.getChild(1).getText())


def get_words(filepath):
    parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(filepath, encoding="utf-8"))))
    walker = ParseTreeWalker()
    listener = WordListener()
    walker.walk(listener, parser.compilationUnit())

    return listener.words
