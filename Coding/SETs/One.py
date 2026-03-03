# fruits = {'apple', 'banana', 'cherry', 'apple'}
# print(fruits)

# numbers = set([1,2,3,2,1])
# print(numbers)

# empty_set = set()
# print(type(empty_set))

# colors = {"red", "green", "blue"}

# for color in colors:
#     print(color)

# animals = {"cat", "dog"}
# animals.add("horse") # Add single element.
# animals.update(["cow", "goat"]) # Add multiple elements.
# print(animals)

# animals.remove("cat")  # Remove items. Error if not found.

# # animals.remove("frog") # Error: 
# animals.discard("frog")   # Remove item. No error if not found.
# print(animals)

# A = {1,2,3,4}
# B = {3,4,5,6}
# print('Union:', A | B)
# print("Intersection: ", A & B)
# print("Difference(A - B):", A - B)
# print("Symmetric Difference:", A^B)

# fruits = {'apple', 'banana', 'mango', 'grapes'}
# print('apple' in fruits)  #True
# print("grapes" not in fruits) #False
# print("cherry" not in fruits) #True

fs = frozenset([1, 2, 3])
print(fs)
print(type(fs))

fs.add(4)
