import csv

filename = input('Enter file name with .csv extention: ')

with open('./FileHandling/Files/'+filename) as fileObject:
    reader = csv.reader(fileObject)
    for row in reader:
        print (row)