
n = int(input('enter number of terms: '))

while n > 0:
    if n % 2 != 0:
        n -= 1
        continue
    
    print('n =', n)
    n -= 1