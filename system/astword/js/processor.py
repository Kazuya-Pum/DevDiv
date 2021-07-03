import esprima
import os


class DeclaratorVisitor(esprima.NodeVisitor):
    def __init__(self):
        self.words = []

    # def visit_Identifier(self, node):
    #     print(node)
    #     self.generic_visit(node)

    # def visit_Property(self, node):
    #     if node.key.name == None:
    #         print(node)
    #     self.words.append(node.key.name)
    #     self.generic_visit(node)

    def visit_VariableDeclarator(self, node):
        if node.id.type == 'Identifier':
            self.words.append(node.id.name)
        elif node.id.type == 'ObjectPattern':
            for p in node.id.properties:
                self.words.append(p.key.name)
        self.generic_visit(node)

    def visit_FunctionDeclaration(self, node):
        self.words.append(node.id.name)
        self.generic_visit(node)

def get_words(filepath):
    words = []
    with open(filepath, 'r') as f:
        program = f.read()
        tree = esprima.parse(program)
        visitor = DeclaratorVisitor()
        visitor.visit(tree)
        return visitor.words