print("Tic Tac Toe:")
grid = [[' ' for _ in range(3)] for _ in range(3)]
print("Player 1 is 'X' and Player 2 is 'O'")
player=1
turns=0
symbol='X'
def Grid():
   for row in grid:
       print('|'.join(row))
       print('-' * 5)
def win():
   if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0] != ' ': 
       if grid[0][0]=='X':
           return 1
       else:
           return 2
   elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0] != ' ':
       if grid[1][0]=='X':
           return 1
       else:
           return 2
   elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0] != ' ':  
       if grid[2][0]=='X':
           return 1
       else:
           return 2
   elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0] != ' ': 
       if grid[0][0]=='X':
           return 1
       else:
           return 2
   elif grid[0][2]==grid[1][1]==grid[2][0] and grid[0][2] != ' ':  
       if grid[0][2]=='X':
           return 1
       else:
           return 2
   elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0] != ' ': 
       if grid[0][0]=='X':
           return 1
       else:
           return 2
   elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1] != ' ':  
       if grid[0][1]=='X':
           return 1
       else:
           return 2
   elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2] != ' ':  
       if grid[0][2]=='X':
           return 1
       else:
           return 2
   else:
       return -1
while turns<9:
   Grid()
   print("Player ",player,"'s turn ")
   print("Enter the position:")
   row=int(input("Row:"))
   col=int(input("Column:"))
   if row < 0 or row > 2 or col < 0 or col > 2:  
       print("Invalid input. Please enter values between 0 and 2.")
       continue
   if grid[row][col]==' ':
       grid[row][col]=symbol
   else:
       print("Please choose another position")
       continue  
   winner = win()
   if winner != -1:
       Grid()
       print("Player",winner,"wins!")
       break
   turns+=1
   if symbol=='X':
       player=2
       symbol='O'
   else:
       player=1
       symbol='X'
if turns==9 and winner==-1:
   Grid()
   print("It's a draw")