class Calculator:
    def __init__(self):
        self.history = []
        #self.result = None
        self.memory = None

    def save(self,result,x,y,op):
        self.history.append(str(x)+op+str(y)+"="+str(result))
        self.result = result

    def swap_memory(self, y):
       if y is not None:
           return y
       if self.memory is None:
           raise Exception("memory is empty")
       y = self.memory
       self.clear_memory()
       return y

    def save_result(self, result, x, y, op):
        self.result = result
        self.history.append([x, y, op, result])
        return result

    def add(self, x, y):
        y = self.swap_memory(y)
        return self.save_result(x + y, x, y, "+")

    def sub(self, x, y):
        y = self.swap_memory(y)
        return self.save_result(x + y, x, y, "-")

    def mul(self, x, y):
        y = self.swap_memory(y)
        return self.save_result(x + y, x, y, "*")

    def div(self, x, y):
        if y != 0:
            y = self.swap_memory(y)
            return self.save_result(x + y, x, y, "/")
        else:
            return "cannot be divided by zero"

    def clear_history(self):
        self.history = []

    def memory_save(self):
        self.memory = self.result

    def clear_memory(self):
        self.memory = None


from math import sqrt as sq

class Advanced_calculator(Calculator):
    def sqrt (self, x):
        return sq(x)
    def root (self, x, y):
        return round((x ** (1/y)),3)
    def pow (self, x, y):
        return (x ** y)
