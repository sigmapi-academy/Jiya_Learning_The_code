# Program to accept a record of an employee from the user and appends it in the binary file. 
# Thereafter, the records are read from the binary file and displayed on the screen using the
# same object. The user may enter as many records as they wish to. The program also displays 
# the size of binary files before starting with the reading process.

import pickle as P

print("working with binary files")
fileName = input('Enter file name: ')
recordNum = 1
print('Press 1 to write records in the file')
print('Press 2 to read all records from the file')
choice = int (input('Enter your choice (1, 2)? '))
match choice:
    case 1:
        print('Enter records of employees')
        print()
        with open('./FileHandling/Files/'+fileName,'ab' ) as fileObject:
            while True:
                print('Record number:', recordNum)
                empno = input('Enter employee number: ')
                ename = input('Enter employee name: ')
                ebasicSal = int(input('Enter basic salary: '))
                allowance = int(input('Enter allowances: '))
                totalSal = ebasicSal + allowance
                print('Total salary: ', totalSal)
                edata = [empno, ename, ebasicSal, allowance, totalSal]
                P.dump(edata, fileObject)
                recordNum += 1
                ans = input('Do you wish to enter more records (y/n)? ')
                if ans.lower() == 'n':
                    print('Record entry is OVER')
                    print()
                    break
            # Retrieving the size of the file.
            print('Size of the binary file (in bytes): ', fileObject.tell())
    case 2:
        # Reading the employees record from the file using load() module.
        print('Now reading the employee records from the file.')
        print()
        readrec = 1
        try:
            with open('./FileHandling/Files/'+fileName, 'rb') as fileObject:
                while True:
                    edata = P.load(fileObject)
                    print("Record Number: ", readrec)
                    print(edata)
                    readrec += 1
        except EOFError:
            print()
            print('End of file reached')
            print()
    case _:
        print('Wrong Option selected')