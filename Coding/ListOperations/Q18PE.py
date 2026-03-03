import random as R
li2 = [i for i in range(1,11)]
li1 = li2
print(li2)
permutation = []

for j in range(10):
    for i in range(1, 11):
        randIndex = R.randint(0, len(li2)-1)
        value = li2.pop(randIndex)
        permutation.append(value)
    
    print(permutation)
    li2.extend(permutation)
    permutation.clear()
