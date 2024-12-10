class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print("Addition:", calc.add(1,2))
print("Subtraction:", calc.subtract(5,2))
print("Multiplication:", calc.multiply(1,3))
print("Division:", calc.divide(9,3))
