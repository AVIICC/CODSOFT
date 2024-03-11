# To do list

tasks = []      #created list type var for tasks 

def menu():      #defining function for menu having operation to be performed
    print("<-------------------------------------------->")
    print("To Do List manager..")
    print("<-------------------------------------------->")
    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. mark done")
    print("5. Quit")

def view_list():      #defining function to view listed tasks
    if len(tasks)<=0:
        print("\nYou have to lists tasks first.")
    else:
        for i in tasks:
            print(i)

def add_tasks():      #defining function to add tasks
    task = input("Enter your tasks : ")
    tasks.append(task)
    print("\nTask added successfully.")

def del_task():      #defining function to delete tasks
    view_list()
    task_del = int(input("Enter the no of task that you would like to delete \"no's starting from 0\": "))
    tasks.pop(task_del)
    print("\nTask deleted successfully.")

def mark_done():      #defining function to mark done tasks
    view_list()
    task_completed = int(input("Enter no of task that you completed to mark as done : ")) 
    tasks[task_completed] = ("Task marked as completed")
    print("Marked done.")

want_to_exit = False
while not want_to_exit:      #altering condition to perform loop untill false
    menu()
    choice = input("Please select any one option from above: ")

    if choice == "1":
        view_list()
    elif choice == "2":
        add_tasks()
    elif choice == "3":
        del_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        want_to_exit = True
        print("thanks for using To Do List.")
    else:
        print("Invalid input, Please enter from options.") 