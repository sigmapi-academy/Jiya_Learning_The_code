
myObject = open("./FileHandling/Files/myfile.txt", "+w")

if not myObject.closed:
    myObject.close()
else:
    print('File is closed')
