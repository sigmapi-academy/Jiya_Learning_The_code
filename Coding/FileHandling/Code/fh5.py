
fileName = input('Enter File Name: ')

with open("./FileHandling/Files/"+fileName, "r") as fileObject:
    while True:
        line10 = fileObject.read(10)
        if line10 != '':
            print(line10)
        else:
            break