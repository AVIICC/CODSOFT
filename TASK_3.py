# imported random module as r to use random functions
import random as r
# listed all characters along with numbers and symbols
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', 
              '%', '&', '(', ')', '*', '+']

want_to_exit = False
while not want_to_exit:
    print("Welcome to the PyPassword Generator!")
    pass_length = int(input("What length of password would you like to generate ? :")) 

    password = ""
    for i in range(pass_length):
        password+=r.choice(characters)

    print("\nYour password is: " + password)
    choice = input("\nIf Want to generate again press \"yes\", if not press \"no\"? :").lower()
    if choice == "yes":
        want_to_exit = False
    else:
        want_to_exit = True
        print("have a good day !")

        


