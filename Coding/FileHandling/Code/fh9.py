
fileName = input('Enter file name: ')
fileObject = open('./FileHandling/Files/' + fileName, "r+")
# print()
# while True:
#     line = input('Enter any sentence: ')
#     fileObject.write(line)
#     fileObject.write('\n')
#     choice = input('Do you wish to enter more data? (y/n): ')
#     if choice in ('n','N'):
#         break
    
print("The byte position of the file object is", fileObject.tell())
fileObject.seek(10) #places file object at beginning of the file
print("The byte position of the file object after seek() is", fileObject.tell())
print()
print("READING DATA FROM THE FILE")
content = fileObject.read()
print(content)
print("The byte position of the file object is", fileObject.tell())
fileObject.seek(30) #places file object at beginning of the file
print("The byte position of the file object after seek() is", fileObject.tell())
content = fileObject.read()
print(content)

fileObject.close()
