from dataclasses import dataclass
from Token import TokenType
from Node import *

class Parser():
    def __init__(self, token):
        self.token = token
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.token)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        raise Exception("Invalid syntax");

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expr()

        if self.current_token != None:
            self.raise_error()

        return result

    def expr(self):

        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.MINUS, TokenType.PLUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())        
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result, self.term())

        return result

    def term(self):

        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.DIVIDE, TokenType.MULTIPLY):
            if self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())
            elif self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())

        return result

    def factor(self):

        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif self.current_token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif self.current_token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
   
        self.raise_error()


