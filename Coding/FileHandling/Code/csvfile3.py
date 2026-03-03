import csv

fileName = input('Enter file name: ')
with open('./FileHandling/Files/'+fileName, 'r') as fo:
    reader = csv.DictReader(fo)
    
    for row in reader:
        print(row['Name'], row['City'], row['Age'], row['MobileNumber'], row['Email'])
        
        