class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError as err:
            print(f'b is zero - {err}!')

        raise ZeroDivisionError

    def multiplication(self):
        return self.a * self.b










