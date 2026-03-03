import csv

fileName = input("Enter file name with .csv extention: ")

with open('./FileHandling/Files/' + fileName, 'a', newline='') as fo:
    fieldNames = ['Name', 'Age', 'City', 'Email', 'MobileNumber']
    writer = csv.DictWriter(fo, fieldNames)
    
    while True:
        name = input('Enter your name: ')
        age = input('Enter your age: ')
        city = input('Enter your city: ')
        email = input('Enter email: ')
        mobileNum = input('Enter mobile nummber: ')
        
        data = {'Name':name, 'Age':age, 'City':city, 'Email': email, 'MobileNumber': mobileNum}
        writer.writerow(data)
        ch = input("Press 'y' to enter another record, other wise press 'n': ")
        if ch.lower() == 'n':
            print('Insertions are done.')
            break
        
    