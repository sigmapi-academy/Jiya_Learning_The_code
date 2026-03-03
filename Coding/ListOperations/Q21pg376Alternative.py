
n = int(input("Enter the number of rows and columns: "))
magicSqr = [[] for _ in range(n)]
# allocate memory for 2-d list
for i in range(n):
    magicSqr[i] = [0]*n

magicSum = n * (n**2+1)//2    
rowsum = [0] * n
colsum = [0] * n
for i in range(n):
    for j in range(n):
        magicSqr[i][j] = int(input('Enter value: '))
        rowsum[i] += magicSqr[i][j]
        
# column sum and diagonal sum
leftDiagonal = 0
rightDiagonal = 0
for i in range(n):
    for j in range(n):
        colsum[i] += magicSqr[j][i]
        
    leftDiagonal += magicSqr[i][i]
    rightDiagonal += magicSqr[i][n-1-i]

isMagicSquare = True
if leftDiagonal != magicSum or rightDiagonal != magicSum:
    isMagicSquare = False  
else:
    for i in range(n):
        if rowsum[i] != magicSum or colsum[i] != magicSum:
            isMagicSquare = False
            break   

print(magicSqr)
if isMagicSquare:
    print('It is a magic square')
else:
    print('It is not a magic square')