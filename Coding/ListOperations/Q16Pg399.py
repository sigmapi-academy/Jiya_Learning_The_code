import random as R

diceRoll = [R.randint(1, 6) for _ in range(1,21)]
print(diceRoll)

count = 0
startIndex = 0
endIndex = 0
longestRun = 1
for i in range(0, 20):
    #run loop
    count = 1
    for j in range(i+1, 20):
        if diceRoll[i] == diceRoll[j]:
            count += 1
        else:
            break
    if count > longestRun:
        startIndex = i
        longestRun = count
        endIndex = startIndex + count
        
for i in range(0, 20):
    if i == startIndex:
        print('(',diceRoll[i], end = ' ')
    elif i == endIndex:
        print(')', end = ' ')
    else:
        print(diceRoll[i], end = ' ')