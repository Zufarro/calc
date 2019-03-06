from calc import Calculator


my_calc = Calculator()

print(my_calc.add(5,4))
print(my_calc.add(4,6))
print(my_calc.steps_memory)
print(my_calc.auto_memory)
my_calc.memory_save()
print (my_calc.memory)
print(my_calc.add(4,None))

print(my_calc.mul(5,4))
print(my_calc.div(7,6))
print(my_calc.sub(10,6))

print(my_calc.div(7,0))


print(my_calc.steps_memory)
my_calc.clear_steps_memory()
print(my_calc.steps_memory)

my_calc.memory_save()
print (my_calc.memory, " add")
my_calc.clear_memory()
print (my_calc.memory, " clear")

print(my_calc.sub(10,15))
