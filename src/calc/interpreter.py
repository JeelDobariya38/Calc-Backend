class Interpreter:
    def __init__(self, parsetree):
        self.parsetree = parsetree

    def interpret(self):
        return self.parsetree.execute()
