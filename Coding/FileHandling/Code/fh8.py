
fileName = input('Enter File Name: ')

with open("./FileHandling/Files/"+fileName, "r") as fileObject:
    line = fileObject.readline()
    while line:
        print(line, end='')
        line = fileObject.readline()