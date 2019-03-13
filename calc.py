class Calculator:
    def __init__(self):
        self.history = []
        self.result = None
        self.memory = None

    def save(self,result,x,y,op):
        self.history.append(str(x)+op+str(y)+"="+str(result))
        self.result = result

    def add(self, x, y):
        if y is not None:
            result = x + y
            self.save(result,x,y,"+")
            return result
        else:
            if self.memory:
                result = self.memory + x
                self.memory = None
                return result
            else:
                return "failing"

    def sub(self, x, y):
        if y is not None:
            result = x - y
            self.save(result,x,y,"-")
            return result
        else:
            if self.memory:
                result = self.memory - x
                self.memory = None
                return result
            else:
                return "failing"

    def mul(self, x, y):
        if y is not None:
            result = x * y
            self.save(result,x,y,"*")
            return result
        else:
            if self.memory:
                result = self.memory * x
                self.memory = None
                return result
            else:
                return "failing"

    def div(self, x, y):
        if y is not None and y != 0:
            result = x / y
            self.save(result,x,y,"/")
            return result
        elif y is None:
            if self.memory:
                result = self.memory / x
                self.memory = None
                return result
            else:
                return "failing"
        else:
            return "failing"

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
