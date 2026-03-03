# Write a program to input three angles of a 
# triangle and check whether its construction is 
# possible or not. If possible, then check and 
# display whether it is an acute angle triangle, 
# right angled or an obtuse angle triangle. 
# Otherwise, display a "triangle is not possible".

a = float(input('Enter first angle: '))
b = float(input('Enter second angle: '))
c = float(input('Enter third angle: '))

sum = a + b + c
if a == 0 or b == 0 or c == 0 or sum != 180:
    print('Triangle is not possible')
else:
    print('Triangle is possible')
    if a == 90 or b == 90 or c == 90 :
        print('Right Angled Triangle')
    elif a > 90 or b > 90 or c > 90 :
        print('Obtuse Angled Triangle')
    else:
        print('Acute Angled Triangle')
        