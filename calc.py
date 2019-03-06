class Calculator:
    def __init__(self):
        self.all_result_history = {}
        self.auto_temp_result = .0
        self.temp_result = .0

    def add(self, x, y):
        if y is not None:
            result = x + y
            self.all_result_history[str(x) + " + " + str(y) + " = "] = result
            self.auto_temp_result = result
            return result
        else:
            if self.temp_result != 0:
                result = self.temp_result + x
                return result
                self.temp_result = .0
            else:
                return "failing"

    def sub(self, x, y):
        if y is not None:
            result = x - y
            self.all_result_history[str(x) + " - " - str(y) + " = "] = result
            self.auto_temp_result = result
            return result
        else:
            if self.temp_result != 0:
                result = self.temp_result - x
                return result
                self.temp_result = .0
            else:
                return "failing"

    def mul(self, x, y):
        if y is not None:
            result = x * y
            self.all_result_history[str(x) + " * " + str(y) + " = "] = result
            self.auto_temp_result = result
            return result
        else:
            if self.temp_result != 0:
                result = self.temp_result * x
                return result
                self.temp_result = .0
            else:
                return "failing"

    def div(self, x, y):
        if y is not None and y != 0:
            result = x / y
            self.all_result_history[str(x) + " / " + str(y) + " = "] = result
            self.auto_temp_result = result
            return result
        elif y is None:
            if self.temp_result != 0:
                result = self.temp_result / x
                return result
                self.temp_result = .0
            else:
                return "failing"
        else:
            return "failing"

    def clear_all_result_history(self):
        self.all_result_history = {}

    def last_result_in_temp(self):
        self.temp_result = self.auto_temp_result

    def clear_temp_result(self):
        self.temp_result = .0
