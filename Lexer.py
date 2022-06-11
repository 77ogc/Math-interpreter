from Token import *

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer():
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_number(self):
        number_str = self.current_char
        self.advance()
        dot_count = 0
        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    self.text = None
                    raise Exception(f"Syntax error.")
                    break
            
            number_str +=  self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0.'
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))
    
    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or  self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Unknow charactor '{self.current_char}'")
