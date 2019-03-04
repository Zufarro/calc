class Calculator ():
    def __init__(self):
        self.all_result_history = {}
        self.temp_result = .0
    def add (self, x, y):
        if y is not None:
            result = x + y
            self.all_result_history[str(x) + " + " + str(y) + " = "] = result
            self.temp_result = result
            return result
        else:
            if self.temp_result != 0:
                return "pass"
            else:
                return "failing"

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
