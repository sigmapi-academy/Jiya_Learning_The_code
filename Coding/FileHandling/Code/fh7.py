fileName = input('Enter File Name: ')

with open("./FileHandling/Files/"+fileName, "a+") as fileObject:
    while True:
        data = input('Enter data to save in the text file: ')
        fileObject.write(data+'\n')
        ans = input("DO you wish to enter more data?(y/n): ")
        if ans in ('n', 'N'):
            break
