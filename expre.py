class Calculator:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        return eval(self.expression)

exp = Calculator("5 + 3 * 2 / 4")
print("Result:", exp.solve())
