from calc import Calculator
from calc import Advanced_calculator

my_calc = Calculator()

print(my_calc.add(5,4))
print(my_calc.add(4,6))
print(my_calc.history)
print(my_calc.result)
my_calc.memory_save()
print (my_calc.memory)
print(my_calc.add(4,None))

print(my_calc.mul(5,4))
print(my_calc.div(7,6))
print(my_calc.sub(10,6))

print(my_calc.div(7,0))


print(my_calc.history)
my_calc.clear_history()
print(my_calc.history)

my_calc.memory_save()
print (my_calc.memory, " add")
my_calc.clear_memory()
print (my_calc.memory, " clear")

print(my_calc.sub(10,15))

my_calc2 = Advanced_calculator()
print(my_calc2.sqrt(100))
print(my_calc2.root(125,3))
print(my_calc2.pow(3,2))
