# # empty list
# my_list = []

# # List of integers
# num = [1,2,3,4,5,6,7,8,9]

# # List of strings
# names = ['Jiya', 'Aadya', 'Krita', 'Shrestha']

# # Mixed list
# mixed_list = [10, "Python", 3.14, True]

# # nested list
# nested_list = [[10, 15], [11, 12], [20,40]]

# print(my_list)
# print(num)
# print(names)
# print(mixed_list)
# print(nested_list)
# print(nested_list[0][0])
# print("First name:",names[0])
# print("Last name:",names[-1])
# print("Names at index 1-2:", names[1:3])
# print('Even:', num[1::2])
# # print('Odd:', num[0::2])
# print('Odd:', num[::2])
# print('Reverse num[]:',num[-1::-1])

# fruits = ['Apple', 'Mango', 'Orange', 'Banana', 'Grapes', 'Strawberry']

# # print(fruits)
# # fruits[3] = 'Watermelon'
# # print(fruits)

# for fruit in fruits:
#     print(fruit)

# matrix = [[10, 12, 14], [16, 18, 20], [22, 24, 26]]
# for row in matrix:
#     print(row)
# matrix = [[10, 12, 14], [16, 18, 20], [22, 24, 26]]
# for row in matrix:
#     for ele in row:
#         print(f'\t{ele}',end = '')
#     print() # to change the line


# squares = [x**2 for x in range(1,11)]
# print(squares)

# even_nums = [x for x in range(1, 21) if x % 2 == 0]
# print(even_nums)

# import random as R

# rand_num = R.sample(range(1, 100), 10)
# print("Sorting in Ascending order:")
# print("Before sorting: ",rand_num)

# rand_num.sort()

# print("After sorting:",rand_num)

# # Soring in Descending order
# rand_num = R.sample(range(1, 100), 10)
# print("Sorting in Decending order:")
# print("Before sorting: ",rand_num)

# rand_num.sort(reverse=True)

# print("After sorting:",rand_num)

# rand_num = R.sample(range(1, 100), 10)

# import random as R

# rand_num = [R.randint(1,100) for _ in range(11)]
# li = sorted(rand_num)
# print(rand_num)
# print(li)
# print()
# dli = sorted(rand_num, reverse= True)
# print(rand_num)
# print(dli)

import random as R

rand_num = [R.randint(1,10) for _ in range(30)]
print(rand_num)
print(len(rand_num))
print(rand_num.count(2))
print(rand_num.index(3))

copy_rand_num = rand_num.copy()
print(copy_rand_num)
copy_rand_num[0] = 80

print(rand_num)
print(copy_rand_num)
