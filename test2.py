# 1 Calculator.

what = input("What to do? (+, -): ")

a = input("Enter the first number: ")
b = input("Enter the second number: ")

if what == "+":
    c = a + b
    print("Result: " + c)
elif what == "-":
    c = a - b
    print("Result: " + c )
else:
    print("The wrong operation is selected!")
# 2 Calculator.

what = input("What to do? (+, -): ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c ))
else:
    print("The wrong operation is selected!")

# 3 Calculator

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Что сделать? (+, -, *, /): ")
result = 0

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b

print(f"Result: {result}")

# 4 Calculator

from colorama import init
from colorama import Fore, Back, Style

print(Fore.CYAN)

a = float(input("Enpyinstater the first number: "))
b = float(input("Enter the second number: "))

print(Fore.BLUE)

operation = input("Что сделать? (+, -, *, /): ")
result = 0

print(Fore.MAGENTA)

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b

print(f"Result: {result}")

#5 Calculator

import numexpr
from colorama import init
from colorama import Fore, Back, Style

print(Fore.CYAN)

expr = input("Enter a mathematical operation: ")
result = numexpr.evaluate(expr)

print(Fore.BLUE)

print(f"Result: {result}")

input()

















