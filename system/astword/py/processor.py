import ast

class CollectVarname(ast.NodeTransformer):
    def __init__(self):
        self.words = []

    def visit_Name(self, node):
        self.words.append(node.id)


def collect_varname(node):
    visitor = CollectVarname()
    visitor.visit(node)
    return visitor.words


def get_words(program):
    return collect_varname(ast.parse(program))
