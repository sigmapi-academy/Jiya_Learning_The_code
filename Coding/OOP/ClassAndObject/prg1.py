class Student:
    # Class variable: class variable is shared by all the objects of class.
    # Same value for all objects.
    academy = "Sigmapi Academy" 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def show_details(self):
        print('Name:',self.name)
        print('Marks:', self.marks)

# main code

s1 = Student('Jiya', 100)

s2 = Student('Rishabh', 80)

s1.show_details() # Shows the details of S1 object.
print('Academy name:',Student.academy)
s2.show_details() # Shows the details of S2 object.
print('Academy name:',Student.academy)


