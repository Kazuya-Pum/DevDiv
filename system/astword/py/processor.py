import ast
import inspect

class CollectVarname(ast.NodeTransformer):
    def __init__(self):
        self.words = []

    def visit_Name(self, node):
        self.words.append(node.id)


def collect_varname(node):
    visitor = CollectVarname()
    visitor.visit(node)
    return visitor.words


def get_words(filepath):
    with open(filepath, 'r') as rf:
        program = ast.parse(rf.read())
        return collect_varname(program)
