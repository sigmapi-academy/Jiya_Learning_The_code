
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

roman = ''

N = int(input('Enter any value between 1-4000: '))
if N > 0 and N <= 3999:
    Dig = N//1000
    if Dig > 0:
        i = 0
        while i < Dig:
            roman += 'M'
            i += 1
    N = N % 1000 
    Dig = N//100
    if Dig > 0:
        if Dig < 4:
            i = 0
            while i < Dig:
                roman += 'C'
                i += 1
        elif Dig == 4:
            roman += 'CD'
        elif Dig == 5:
            roman += 'D'
        elif Dig >=6 and Dig < 9:
            i = 6
            roman += 'D'
            while i <= Dig:
                roman += 'C'
                i += 1
        else:
            roman += 'CM'
    N = N % 100
    dig = N//10
    if dig > 0 and dig < 4:
        i = 0
        while i < dig:
            roman += 'X'
            i += 1
    elif dig == 4:
        roman += 'XL'
    elif dig == 5:
        roman += 'L'
    elif dig > 5 and dig < 9:
        roman += 'L'
        i = 6
        while i <= dig:
            roman += 'X'
            i += 1
    elif dig == 9:
        roman += 'XC'
    
    N = N % 10
    if N>0 and N < 4:
        i = 0
        while i < N:
            roman += 'I'
            i += 1
    elif N == 4:
        roman += 'IV'
    elif N == 5:
        roman += 'V'
    elif N > 5 and N < 9:
        roman += 'V'
        i = 5
        while i < N:
            roman += 'I'
            i += 1
    elif N == 9:
        roman += 'IX'
    print('Roman:', roman)       
else:
    print('Invalid input.')       
        
