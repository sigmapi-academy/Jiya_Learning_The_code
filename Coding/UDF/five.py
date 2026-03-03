def my_function():
    pass

def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

liName = []
liAge = []
liCity = []
while True:
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    city = input('Enter your city: ')
    liName.append(name)
    liAge.append(age)
    liCity.append(city)
    
    ch = input('More records press "y" or "Y" otherwise press "n" or "N"? ')
    if ch in ('n', 'N'):
        break
    
for i in range(len(liName)):    
    student_details(name=liName[i], age=liAge[i], city=liCity[i])
