import json

#The initial list variable to store tasks.
tasks = []


#Prompt user for the task title and add it to the 'tasks' list
def add_task():
    title = input("\nAdd a task: ")
    while not title:
        print("\nTask title cannot be empty. Please try again.")
        title = input("\nAdd a task: ")
    priority = int(input("\nEnter task priority (1 - high, 2 - medium, 3 - low): "))
    while priority not in [1, 2, 3]:
        print("\nInvalid input. Please enter 1, 2, or 3.")
        priority = int(input("\nEnter task priority (1 - high, 2 - medium, 3 - low): "))
    task = {"title": title, "completed": False, "priority": priority}
    tasks.append(task)
    print("\nTask added successfully!\n")

    #save tasks to the "tasks.txt" file
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.extend(json.load(file))
            print("\nTasks loaded successfully!")
    except FileNotFoundError:
        print("\nNo previous tasks found.")
    except json.JSONDecodeError:
        print("\nError while loading tasks. The file may be corrupted.")


#Updates the "tasks.txt" file with the current tasks list
def update_file():
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)


#Displays all the tasks along with their completion status.
def view_tasks():
    if not tasks:
        print("\nThere are no tasks in the list.\n")

    print("\nTasks: ")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        if task["priority"] == 1:
            priority = 'High'
        elif task["priority"] == 2:
            priority == 'Medium'
        else:
            priority = 'Low'
        print(f"{index}. {priority} priority - {task['title']} - {status}")


#Marks a task as completed based on user input.
def mark_completed():
    if not tasks:
        print("\nThere are no tasks in the list.\n")
        return
    
    view_tasks()
    while True:
        try:
            task_number = int(input("\nChoose a task number to mark as completed. Otherwise, to return to main menu, press '0': "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed.")
                #update the "tasks.txt" file
                update_file()
                break
            elif task_number == 0:
                return
            else:
                print("\nInvalid input. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid task number.")
    

    


#Displays the menu of options and handles user choices.
#The program continues running until the user chooses to exit.
def main():
    load_tasks()

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
            print("\nInvalid choice. Please try again.")


#ensure the main code block is executed only when the script is run directly,
#and not when it is imported as a module into another script.
if __name__ == "__main__":
    main() 