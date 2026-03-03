
fileName = input('Enter file name: ')
lineList = []
with open("./FileHandling/Files/"+fileName, "+a") as fileObject:
    while True:
        line = input('Type a line or press "x" or "X" to exit: ')
        if line.lower() == 'x':
            break
        lineList.append(line+"\n")
    fileObject.writelines(lineList)
    
        
