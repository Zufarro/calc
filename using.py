from calc import Calculator


my_calc = Calculator()

print(my_calc.add(5,4))
print(my_calc.add(4,6))
print(my_calc.all_result_history)
print(my_calc.auto_temp_result)
my_calc.last_result_in_temp()
print (my_calc.temp_result)
print(my_calc.add(4,None))

print(my_calc.mul(5,4))
print(my_calc.div(7,6))
print(my_calc.sub(10,6))

print(my_calc.div(7,0))


print(my_calc.all_result_history)
my_calc.clear_all_result_history()
print(my_calc.all_result_history)

my_calc.last_result_in_temp()
print (my_calc.temp_result, " add")
my_calc.clear_temp_result()
print (my_calc.temp_result, " clear")
