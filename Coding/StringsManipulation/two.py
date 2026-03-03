str1 = input('Enter any sentence: ')

vowels = "AEIOUaeiou"

# for char in str1:
#     if char not in vowels:
#         print(char, end="")

i = 0
length = len(str1)
while i < length:
    char = str1[i]
    if char not in vowels:
        print(char, end="")
    i += 1

        