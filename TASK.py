tasks = []

def add_task(task):

    tasks.append(task)

    print(f"Task '{task}' added to the To-Do list.")


def view_tasks():

    if not tasks:

        print("Your To-Do list is empty.")

    else:

        print("To-Do List:")

        for index, task in enumerate(tasks, start=1):

            print(f"{index}. {task}")


def complete_task(task_index):

    if 1 <= task_index <= len(tasks):

        completed_task = tasks.pop(task_index - 1)

        print(f"Task '{completed_task}' marked as completed.")

    else:

        print("Invalid task index. Please enter a valid task number.")

 
user_name = input("Enter your name: ")  
print(f"Welcome, {user_name}!")

 
while True:

    print("\nOptions:")

    print("1. Add a task")

    print("2. View tasks")

    print("3. Complete a task")

    print("4. Quit")

   

    choice = input("Enter your choice (1/2/3/4): ")

   

    if choice == "1":

        task = input("Enter the task: ")

        add_task(task)

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        task_index = int(input("Enter the task number to mark as completed: "))

        complete_task(task_index)

    elif choice == "4":

        print(f"Goodbye, {user_name}!")

        break

    else:

        print("Invalid choice. Please choose a valid option.")