v = int(input('Enter any positive integer: '))

t = int(input("How many times?"))

n = 1
while n <= t:
    p = n * v
    print(n,'*',v,'=',p)
    n -= 1  # n = n + 1

