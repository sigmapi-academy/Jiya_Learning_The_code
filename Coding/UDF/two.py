def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# (10 + 25) - (30 - 40)
res = sub(add(10, 25), sub(30, 40))
print('result = ', res)