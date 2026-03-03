v = int(input('Enter any positive integer: '))

t = int(input("How many times?"))

n = 1
while True:
    p = n * v
    print(n,'*',v,'=',p)
    if n == t:
        break #terminate the loop
    
    n += 1  # n = n + 1
    
