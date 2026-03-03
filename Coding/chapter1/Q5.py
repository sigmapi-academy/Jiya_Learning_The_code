# 	5. Write a program to input to unequal positive numbers and 
#  check whether they are perfect square numbers or not. If the user 
#  enters any negative number, then the program display the message 
#  "square root of negative number cannot be determined".
# 	 Sample input: 81, 100
# 	 Sample output: They are perfect square numbers.
	
# 	 Sample input: 225, 99
# 	 Sample output: 225 is a perfect square number.
#    99 is not a perfect square number.

import math

N = int(input('Enter first number: '))
M = int(input('Enter second number: '))

if N < 0 or M < 0:
    print('Square root of negative number cannot be determined')
else:
    SQ1 = int(math.sqrt(N))
    SQ2 = int(math.sqrt(M))

    if SQ1 ** 2 == N and SQ2 ** 2 == M:
        print(f"{N}, {M} is a perfect square number")
    elif SQ1 ** 2 == N and SQ2 ** 2 != M:
        print(f"{N} is a perfect square number")
        print(f"{M} is not a perfect square number")
    elif SQ1 ** 2 != N and SQ2 ** 2 == M:
        print(f"{N} is not a perfect square number")
        print(f"{M} is a perfect square number")
    else:
        print(f"{N} and {M} both are not perfect square")


rupee = '\u20b9'
print(rupee,'100')

    