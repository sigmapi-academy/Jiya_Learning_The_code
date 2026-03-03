def calculate(n):
    square = n ** 2
    cube = n ** 3
    
    return square, cube

x = int(input('Enter any integer value to find its square and cube of it: '))
s, c = calculate(x)
print('Square:', s)
print('Cube:', c)
