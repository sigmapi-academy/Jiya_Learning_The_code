
N = int(input('Number of terms: '))

sum = 0
sign = 1

for i in range(1, N):
    t = (i * 2)*sign
    if t > 0:
        print(t,sep='', end='')
    else:
        print(t,'+', sep='', end='')
    sum = sum + t
    sign = sign * (-1)

# for the last term
sum = sum + N*2*sign
print(N*2,'=',sum) 
