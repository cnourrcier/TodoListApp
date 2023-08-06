
#The initial list variable to store tasks.
tasks = []


#Prompt user for the task title and add it to the 'tasks' list
def add_task():
    title = input("\nAdd a task: ")
    task = {"Title": title, "Completed": False}
    tasks.append(task)
    print("\nTask added successfully!\n")


#Displays all the tasks along with their completion status.
def view_tasks():
    if not tasks:
        print("\nThere are no tasks in the list\n")

    print("\nTasks: ")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task['Completed'] else "Not Done"
        print(f"{index}. {task['Title']} - {status}")


#Marks a task as completed based on user input.
def mark_completed():
    while True:
        try:
            if not tasks:
                print("\nThere are no tasks in the list\n")
                return
            view_tasks()
            prompt = int(input("\nChoose a task number to mark as completed. Otherwise, to return to main menu, press '0': "))
            if 1 <= prompt <= len(tasks):
                tasks[prompt - 1]["Completed"] = True
                return
            elif prompt == 0:
                return
            else:
                print("\nInvalid input. Please try again")
        except ValueError:
            print("\nInvalid input. Please enter a valid task number") 

    


#Displays the menu of options and handles user choices.
#The program continues running until the user chooses to exit.
def main():
    running = True
    while running == True:
        print("\nOptions: ")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        option = input("\nType a number to choose an option from the menu: ")

        if option == '1':
            add_task()
        elif option == '2':
            view_tasks()
        elif option == '3':
            mark_completed()
        elif option == '4':
            print("Goodbye!")
            running = False
            break
        else:
            print("\nInvalid choice. Please try again")


#ensure the main code block is executed only when the script is run directly,
#and not when it is imported as a module into another script.
if __name__ == "__main__":
    main() 