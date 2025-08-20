class CalcException(Exception):
    def __init__(
        self, message: str = "Service is currently unavailable!!", name="CalcException"
    ):
        self.name = name
        self.message = message
        super().__init__(self.message, self.name)


class InvalidSyntaxError(CalcException):
    pass
