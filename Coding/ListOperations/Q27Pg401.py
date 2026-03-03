theater = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]
while True:
    for i in theater:
        print(i)
    choice = input("Price or seat: ")
    if choice == "seat":
        print("Enter the row and column: ")
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        if theater[row][column] == 0:
            print("This seat is already reserved.")
        else:
            print("The price of the seat is", theater[row][column])
            theater[row][column] = 0
            for i in theater:
                print(i)
            print("Seat reserved successfully.")  
    elif choice == "price":
        price = int(input("Enter the price: "))
        l=0
        m=0
        seat=()
        for h in theater:
            l = 0
            for k in h:
                if k == price:
                    seat=(l,m)
                    print("Seat at row",m, "column ",l, "with price ",price, 
                          "has been reserved.")
                    theater[m][l] = 0 
                    for i in theater:
                        print(i)
                    break
                l+=1
            if k == price: #to break outer loop
                break
            m+=1
        if not seat: 
            print("No seats available with the price",price)
    else:
        print("Invalid input. Please enter 'price' or 'seat'.")
    cont=input("Enter yes or no to continue: ")
    if cont in ("no", 'No', 'NO','nO'):
        break