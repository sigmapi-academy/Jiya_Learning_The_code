
fileName = input('Enter file name: ')
with open("./FileHandling/Files/"+fileName, "+a") as fileObject:
    while True:
        line = input('Type a line or press "x" or "X" to exit: ')
        if line.lower() == 'x':
            exit()
        print("Number of characters written in file:", fileObject.write(line+"\n"))
        
