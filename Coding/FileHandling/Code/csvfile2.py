import csv

fileName = input('Enter the file name with .csv extension: ')

with open('./FileHandling/Files/'+fileName, 'a', newline='') as fileObject:
    writer = csv.writer(fileObject)
    while True:
        name = input('Enter your name: ')
        age = input('Enter your age: ')
        city = input('Enter your city: ')
        email = input('Enter email: ')
        mobileNum = input('Enter mobile nummber: ')
        
        data = [name, age, city, email, mobileNum]
        writer.writerow(data)
        ch = input("Press 'y' to enter another record, other wise press 'n': ")
        if ch.lower() == 'n':
            print('Insertions are done.')
            break
        