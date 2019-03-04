class Calculator ():
    def __init__(self):
        self.all_result_history = {}
        self.temp_result = []
    def add (self, x, y):
        return x + y
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
