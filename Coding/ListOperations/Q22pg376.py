

n = int(input("Enter the number of rows and columns: "))
if n % 2 == 0:
    print("Number of rows and columns should be odd")
else:
    mat = [[] for _ in range(n)]
    for i in range(n):
        mat[i] = [0] * n
    row = n - 1
    column = n // 2
    for k in range(1, n*n+1):
        mat[row][column]=k
        row += 1
        column += 1
        if row == n:
            row = 0
        if column == n:
            column = 0
        if mat[row][column] != 0:
            row -= 1
            column -= 1
            row -= 1
    print("Magic Square:")
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()