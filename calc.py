class Calculator:
    def __init__(self):
        self.steps_memory = {}
        self.auto_memory = .0
        self.memory = .0

    def add(self, x, y):
        if y is not None:
            result = x + y
            self.steps_memory[str(x) + " + " + str(y) + " = "] = result
            self.auto_memory = result
            return result
        else:
            if self.memory != 0:
                result = self.memory + x
                return result
                self.memory = .0
            else:
                return "failing"

    def sub(self, x, y):
        if y is not None:
            result = x - y
            self.steps_memory[str(x) + " - " + str(y) + " = "] = result
            self.auto_memory = result
            return result
        else:
            if self.memory != 0:
                result = self.memory - x
                return result
                self.memory = .0
            else:
                return "failing"

    def mul(self, x, y):
        if y is not None:
            result = x * y
            self.steps_memory[str(x) + " * " + str(y) + " = "] = result
            self.auto_memory = result
            return result
        else:
            if self.memory != 0:
                result = self.memory * x
                return result
                self.memory = .0
            else:
                return "failing"

    def div(self, x, y):
        if y is not None and y != 0:
            result = x / y
            self.steps_memory[str(x) + " / " + str(y) + " = "] = result
            self.auto_memory = result
            return result
        elif y is None:
            if self.memory != 0:
                result = self.memory / x
                return result
                self.memory = .0
            else:
                return "failing"
        else:
            return "failing"

    def clear_steps_memory(self):
        self.steps_memory = {}

    def memory_save(self):
        self.memory = self.auto_memory

    def clear_memory(self):
        self.memory = .0


from math import sqrt as sq

class Advanced_calculator(Calculator):
    def sqrt (self, x):
        return sq(x)
    def root (self, x, y):
        return round((x ** (1/y)),3)
    def pow (self, x, y):
        return (x ** y)
