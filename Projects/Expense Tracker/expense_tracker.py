print("-----------------------------------")
print("1.View Expense\n2.Calculate Total Expense\n3.Add a Expense\n4.Exit")

try:
    option = int(input("Please select anyone option: ")) 
except ValueError:
    print("The input must be an Integer: ")
    option = int(input("Please select anyone option: "))
while(option != 4):
    if(option == 1):
        with open("expense.txt", "r") as f:
            empty = True
            for line in f:
                empty = False
                print(line, end="")
            print("-----------------------------------")
            if empty:
                print("No data found")
                print("-----------------------------------")
    elif(option == 2):
        total = 0
        with open("expense.txt", "r") as f:
            for line in f:
                amount = int(line.split(":")[1])
                total += amount

        print("Total Expense:", total)
        print("-----------------------------------")
    elif(option == 3):
        with open("expense.txt", "a+") as f:
            typeof = input("Pls enter the type of expense: ")
            if(typeof.isdigit() or not typeof):
                print("Pls Enter a Valid Expense Type.")
                print("-----------------------------------")
            else:
                try:
                    amount = int(input('Please Enter the amount: '))
                    f.write(f"{typeof}: {amount}\n")
                    total += amount
                except ValueError:
                    print("Please Enter a Valid Amount")
                    print("-----------------------------------")
    elif(option == 4):
        exit

    else:
        print("Please Enter a Valid Option")
        print("-----------------------------------")
    print("1.View Expense\n2.Calculate Total Expense\n3.Add a Expense\n4.Exit")
    option = int(input("Please select anyone option: "))
