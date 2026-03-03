
def add(*numbers):
    total = sum(numbers)
    print("Sum:", total)
    
def mul(*numbers):
    p = 1
    for m in numbers:
        p = p * m
    return p
    
add(45, 23)
add(45, 23, 65)
add(67, 21, 19, 29)

p1 = mul(12, 4)
print("Multiplication:", p1)
p2 = mul(2, 3, 4)
print("Multiplication:", p2)
p3 = mul(3, 4, 5, 6)
print("Multiplication:", p3)
