# Stupid-calculator-v1
This is my first calculator v1

 #Дебільний калькулятор

todo = input("Що будемо робити? (+, -,/,*):")
a = float( input("Введи перше число: "))
b = float( input("Введи друге число: "))

if todo == '+':
      c = a + b
      print("Результат: " + str(c))
elif todo == '-':
      c = a - b
      print("Результат: " + str(c))
elif todo == '/':
      c = a / b
      print("Результат: " + str(c))
elif todo == '*':
      c = a * b
      print("Результат: " + str(c))
else:
   print("Вибрана не коректна операція")
