# Simple arithmatic calculator.
# defining function as menu showing operation to be performed
def menu():
    print("<-------------------------------------------->")
    print(             "Arithamtic Calculator")
    print("<-------------------------------------------->")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

# defining function to perform addition
def add(no_1,no_2):
   return no_1+no_2
    
# defining function to perform subtraction
def sub(no_1,no_2):
    return no_1-no_2

# defining function to perform multiplication
def pro(no_1,no_2):
    return no_1*no_2

# defining function to perform division
def div(no_1,no_2):
    return no_1/no_2

# to perform operation until user want to exit, while loop were used below
# to perform while loop condition specifies as bool false, amd altered it to True to go ahead
want_to_exit = False
while not want_to_exit:
    menu()
    choice = int(input("Enter the no of operation to be performed from the menu: "))
    if choice == 5:
        want_to_exit=True
        print("Have a good day!")
    else:
        a = float(input("Enter first no: ")) 
        b = float(input("Enter second no: "))  
        if choice == 1:         #comparing choice with different operations
            print(add(a,b))     #calling funtion based on choice
        elif choice == 2:
            print(sub(a,b))
        elif choice == 3:
            print(pro(a,b))
        else:
            print(div(a,b))

    

