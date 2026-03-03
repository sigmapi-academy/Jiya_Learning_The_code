def listInput():
    x = input("Enter elements of the list in [1, 2, 3, 'hello']: ")
    li = eval(x)
    return li

def sameSet(a:list, b:list):
    if isinstance(a, list) and isinstance(b, list):
        for e in b:
            if e not in a:
                return False  # b is not a subset
        return True # b is a subset
    else:
        return f'{a} or {b} may not be a list' 
    
li1 = listInput()
li2 = listInput()

isSubSet = sameSet(li1, li2)
if isinstance(isSubSet, bool):
    if isSubSet:
        print('list b is the subset')
    else:
        print('list b is not a subset')
else:
    print(isSubSet)
    
    
