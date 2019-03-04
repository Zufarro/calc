class Calculator ():
    def __init__(self):
        self.all_result_history = {}
        self.temp_result = .0
    def add (self, x, y):
        if y is not None:
            result = x + y
            self.all_result_history[str(x) + " + " + str(y) + " = "] = result
            return result
        else:
            return "pass"

    def sub (self, x, y):
        return x - y

    def mul (self, x, y):
        return x * y

    def div (self, x, y):
        return x /y

    def clear_result (self):
        pass

    def moving_result_in_temp(self):
        pass

    def clear_temp_result(self):
        pass

my_calc = Calculator()
print(my_calc.add(5,4))
print(my_calc.add(4,6))
print (my_calc.all_result_history)
