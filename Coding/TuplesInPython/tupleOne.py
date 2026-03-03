
# my_tuple = ('apple', 'banana', 'grape', 'orange')
# print(my_tuple)
# print("First element:", my_tuple[0])
# print("Last element: ",my_tuple[-1])


# info = ('Apple', 25, 25.5, True)
# print("Mixed data type in tuple:",info)

# singleElement = (5)
# print(type(singleElement))

# singleElement = (5,)
# print(type(singleElement))

# my_tuple = ('apple', 'banana', 'grape', 'orange')

# my_tuple[1] = 'mango'

# print(my_tuple)


# my_tuple = ('apple', 'banana', 'grape', 'orange')

# for fruit in my_tuple:
#     print(fruit)

# a = (1, 2)
# b = (3, 4)
# print(a)
# print(b)
# c = a + b  #(1, 2, 3, 4) Concatenation of tuples
# print(c)
# d = a * 2  #(1, 2, 1, 2) Repeatition of a tuple
# print(d)

# print(len(a), len(b), len(c), len(d))



# person = ('Shiv', 42, 'USA')
# name, age, country = person
# print(name)
# print(age)
# print(country)

a = (1, 2)
b = (3, 4)
print(a)
print(b)
c = a + b  #(1, 2, 3, 4) Concatenation of tuples
print(c)
d = a * 2  #(1, 2, 1, 2) Repeatition of a tuple
print(d)

idx =  d.index(2)
print('First index:', idx)
nextIdx = d.index(2, idx+1)
print('Next index:',nextIdx)
# nextIdx = d.index(2, nextIdx + 1)
# print('Next index:',nextIdx)
c = d.count(2)
print(f'{2} has occured {c} times')




