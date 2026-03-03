"""
    Simple calulator which solves simple arithmetic  problems like
    addition(+), subtraction(-), multiplication(*), division(quotient(//), remainder(%), actual division(/)),
    exponention(**)
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def remainder(a, b):
    return a % b

def quotient(a, b):
    return a // b

def multiply(a, b):
    return a * b

def power(a, b):
    return a**b


# main code

while True:
    n1 = float(input('Enter first number: '))
    op = input('Enter operator symbol (+, -, *, /, //, **) : ') 
    n2 = float(input('Enter second number: '))
    correctOp = True
    match(op):
        case "+":
            res = add(n1, n2)
        case "-":
            res = subtract(n1, n2)
        case '*':
            res = multiply(n1, n2)
        case '%':
            res = remainder(n1, n2)
        case "//":
            res = quotient(n1, n2)
        case "/":
            res = divide(n1,n2)
        case "**":
            res = power(n1, n2)
        case _: 
            correctOp = False
            print('Wrong operator selected')
    if correctOp:
        print(f'Result = {res}')
    
    e = input("press 'x' or 'X' to exit from the calculator: ")
    if e in ('x', 'X'):
        break # terminates the loop
    