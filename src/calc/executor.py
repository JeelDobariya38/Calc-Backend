from .filter import Filter
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter


def calc_execute(code):
    code = Filter(code).apply()
    lexer = Lexer(code)
    tokens = lexer.tokonize()
    parser = Parser(tokens)
    parsetree = parser.parse()
    interpreter = Interpreter(parsetree)
    return interpreter.interpret()
