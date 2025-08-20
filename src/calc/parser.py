from .customerr import InvalidSyntaxError
from .tokens import TokenType
from .nodes import Node, NumberNode, AddNode, SubNode, MulNode, DivNode, OutNode


def isnumbernode(node):
    res = str(node.execute())
    for char in res:
        if char not in "1234567890.-":
            return False
    return True


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def get_binary_args(self, parsetree):
        left = None
        right = None

        # Left Arg
        try:
            left = parsetree.args.pop()
            if not isnumbernode(left):
                raise InvalidSyntaxError("Invalid Left Args Type!!!")
        except IndexError as _:  # noqa: F841
            left = NumberNode(data=float(0))

        # Right Arg
        try:
            right = next(self.tokens)
        except StopIteration as _:  # noqa: F841
            raise InvalidSyntaxError("Not Sufficient Args!!!")

        if right.type != TokenType.NUMBER:
            if right.type == TokenType.MINUS:
                try:
                    right = next(self.tokens)
                    if right.type == TokenType.NUMBER:
                        neg_num = 0 - float(right.data)
                        right = NumberNode(data=neg_num)
                    else:
                        raise InvalidSyntaxError("Not Sufficient Args!!!")
                except StopIteration as _:  # noqa: F841
                    raise InvalidSyntaxError("Not Sufficient Args!!!")
            elif right.type == TokenType.LPRAM:
                right = self.parse().args[0]
            else:
                raise InvalidSyntaxError("Invalid Right Args Type!!!")
        else:
            right = NumberNode(data=float(right.data))

        return [left, right]

    def parse(self):
        parsetree = Node()
        for token in self.tokens:
            if token.type == TokenType.NUMBER:
                node = NumberNode(data=float(token.data))
                parsetree.args.append(node)
            elif token.type == TokenType.PLUS:
                args = self.get_binary_args(parsetree)
                node = AddNode(args)
                parsetree.args.append(node)
            elif token.type == TokenType.MINUS:
                args = self.get_binary_args(parsetree)
                node = SubNode(args)
                parsetree.args.append(node)
            elif token.type == TokenType.MULTIPLE:
                args = self.get_binary_args(parsetree)
                node = MulNode(args)
                parsetree.args.append(node)
            elif token.type == TokenType.DIVIDE:
                args = self.get_binary_args(parsetree)
                node = DivNode(args)
                parsetree.args.append(node)
            elif token.type == TokenType.OUTPUT:
                outparsetree = self.parse()
                node = OutNode(outparsetree.args)
                parsetree.args.append(node)
            elif token.type == TokenType.LPRAM:
                tree = self.parse().args[0]
                parsetree.args.append(tree)
            elif token.type == TokenType.RPRAM:
                return parsetree
        return parsetree
