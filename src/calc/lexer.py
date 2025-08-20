from .tokens import Token, TokenType


class Lexer:
    def __init__(self, code):
        self.code = iter(code)
        self.tokens = []
        self.isnum = False
        self.currtoken = ""

    def iswhitespace(self, letter):
        if letter in "\t \n":
            return True
        return False

    def gettoken(self):
        if self.currtoken == "+":
            return Token(TokenType.PLUS)

        if self.currtoken == "-":
            return Token(TokenType.MINUS)

        if self.currtoken in "*xX":
            return Token(TokenType.MULTIPLE)

        if self.currtoken == "/":
            return Token(TokenType.DIVIDE)

        if self.currtoken.lower() == "out":
            return Token(TokenType.OUTPUT)

    def tokonize(self):
        for letter in self.code:
            if self.iswhitespace(letter):
                if self.currtoken != "" and self.isnum:
                    token = Token(TokenType.NUMBER, self.currtoken)
                    self.tokens.append(token)
                    self.currtoken = ""
                    self.isnum = False
                continue

            if letter in "0123456789.":
                if self.currtoken == "":
                    self.isnum = True
            else:
                if self.isnum:
                    self.isnum = False

            self.currtoken += letter

            token = self.gettoken()
            if token:
                self.tokens.append(token)
                self.currtoken = ""
                continue

            if letter == "(":
                token = Token(TokenType.LPRAM)
                self.tokens.append(token)
                self.currtoken = self.currtoken[:-1]
                continue

            if letter == ")":
                token = Token(TokenType.RPRAM)
                self.currtoken = self.currtoken[:-1]
                self.isnum = True
                for char in self.currtoken:
                    if char not in "0123456789.":
                        self.isnum = False
                        break
                numtoken = Token(TokenType.NUMBER, self.currtoken)
                if numtoken.data != "":
                    self.tokens.append(numtoken)
                self.currtoken = ""
                self.isnum = False
                self.tokens.append(token)
                continue

        if self.currtoken != "":
            if self.isnum:
                token = Token(TokenType.NUMBER, self.currtoken)
                self.tokens.append(token)
            else:
                token = self.gettoken()
                if token:
                    self.tokens.append(token)
                    self.currtoken = ""
        return self.tokens
