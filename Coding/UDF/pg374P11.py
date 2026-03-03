def equals(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return a == b
    else:
        return f'{a} or {b} is not a list'
            

def listInput():
    x = input("Enter elements of the list in [1, 2, 3, 'hello']: ")
    li = eval(x)
    return li

li1 = listInput()
li2 = listInput()

if equals(li1, li2):
    print('Both lists having same elements.')
else:
    print('Both lists have different elements')



