
fileName = input('Enter File Name: ')

with open("./FileHandling/Files/"+fileName, "r") as fileObject:
    fullFile = fileObject.read()
    vowels = 'AEIOUaeiou'
    count = 0
    for c in fullFile:
        if c in vowels:
            count+=1
    print(fullFile)
    print('\nNumber of vowels:', count)