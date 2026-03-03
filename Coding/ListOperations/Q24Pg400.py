sequence = int(input("Enter the length of the sequence: "))
if sequence <= 0:
   print("Invalid input. Sequence length must be greater than 0.")
   exit()
li = []
max_value = 0
for i in range(sequence):
   value = input("Enter an element: ")
   if not value.isdigit():  
       print("Invalid elements provided. Please enter positive numbers.")
       exit()
   li.append(int(value))  
max_value = max(li)
if max_value == 0: 
   print("All elements are zero. Please enter positive numbers.")
   exit()
val_len = 40 / max_value  
for value in li:
   print("*" * int(value * val_len))  
 