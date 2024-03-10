# Comtact Book 
def menu():
    print('''\n<-------------------------------------------->
            Contacts Manager
<-------------------------------------------->
1. View contacts
\n2. Add Contacts
\n3. Update Contacts
\n4. Delete Contacts
\n5. Search Contacts List
\n6. Quit
<-------------------------------------------->''')
contact_names = []
contacts_phone = []

def view():
    if len(contact_names)>0:
        print("Name\tPhone")
        for name, phone in zip(contact_names, contacts_phone):
            print("{}\t{}".format(name, phone))
    else:
        print("\nSorry !, You have to add contacts first.")

def add():
    name = input("Enter name : ")
    phone = input("Enter phone : ")
    contact_names.append(name)
    contacts_phone.append(phone)
    print("\nContact Added successfully.")
    return phone,name

def update():
    view()
    choice_update = input("Which contact you want to update, Enter name : ")
    if choice_update in contact_names:
        name_index = contact_names.index(choice_update)
        new_name = input("Enter the updated name: ")
        new_phone = input("Enter the updated phone number: ")
        contact_names[name_index] = new_name
        contacts_phone[name_index] = new_phone
        print("\nContact updated successfully.")
    else:
        print("Not found!, please enter valid contact name.")

def delete():
    view()
    search_name = input("\nEnter name of contact you want to delete : ")
    if search_name in contact_names:
        name_index = contact_names.index(search_name)
        contact_names.pop(name_index)
        print("\nContact deleted successfully.")
    else:
        print("Not found!, please enter valid name.")

def search():
    search_name = input("Enter name of contact you want to search : ")
    if search_name in contact_names:
        name_index = contact_names.index(search_name)
        phone_index = contacts_phone[name_index]
        print("\n{}\t{}".format(search_name,phone_index ))
    else:
        print("Not found!, please enter valid name.")


want_to_exit = False
while not want_to_exit:
    menu()
    choice = input("Please select any one option from above: ")

    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    elif choice == "6":
        want_to_exit = True
        print("thanks.")
    else:
        print("Invalid input, Please enter from options.")

