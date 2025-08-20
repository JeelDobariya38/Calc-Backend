def apply_dmass(expression):
    return expression


def add_whitespaces(expression):
    ind = -1
    final_expression = ""
    num_acc = ""

    for val in expression:
        ind += 1
        if val in "01234456789.":
            num_acc += val
        else:
            final_expression += " " + num_acc + " " + val
            num_acc = ""

    return final_expression + " " + num_acc


class Filter:
    def __init__(self, expression):
        self.expression = expression

    def apply(self):
        expression = self.expression
        expression = apply_dmass(expression)
        expression = add_whitespaces(expression)
        return expression
