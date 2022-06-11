from Node import *
from Value import Number

class Interpreter():
    def visit(self, node):
        node_name = f'visit_{type(node).__name__}'
        method = getattr(self, node_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_MinusNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)

    def visit_PlusNode(self, node):
        return Number(node.node.value)
    
    def visit_MinusNode(self, node):
        return Number(node.node.value * (-1))