from itertools import count
from tkinter import Y
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
