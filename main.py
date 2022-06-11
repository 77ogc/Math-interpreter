from Lexer import *
from Parser import *
from Interpreter import *

while True:
	text = input("Cal :  ")
	lexer = Lexer(text)
	tokens = lexer.generate_tokens()
	parser = Parser(tokens)
	tree = parser.parse()
	interpreter = Interpreter()
	value = interpreter.visit(tree)

	print( value )
 
