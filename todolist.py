import json

#The initial list variable to store tasks.
tasks = []


#Prompt user for the task title and add it to the 'tasks' list
def add_task():
    title = input("\nAdd a task: ")
    task = {"Title": title, "Completed": False}
    tasks.append(task)
    print("\nTask added successfully!\n")

    #save tasks to the "tasks.txt" file
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                task = {"Title": task_data["Title"],"Completed": task_data["Completed"]}
                tasks.append(task)
            print("\nTasks loaded successfully!")
    except (FileNotFoundError,json.JSONDecodeError):
        print("\nNo previous tasks found.")


#Updates the "tasks.txt" file with the current tasks list
def update_file():
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)

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
    if not tasks:
        print("\nThere are no tasks in the list\n")
        return
    
    view_tasks()
    while True:
        try:
            prompt = int(input("\nChoose a task number to mark as completed. Otherwise, to return to main menu, press '0': "))
            if 1 <= prompt <= len(tasks):
                tasks[prompt - 1]["Completed"] = True
                print("Task marked as completed")
                #update the "tasks.txt" file
                update_file()
                break
            elif prompt == 0:
                return
            else:
                print("\nInvalid input. Please try again")
        except ValueError:
            print("\nInvalid input. Please enter a valid task number")
    

    


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
            print("\nInvalid choice. Please try again")


#ensure the main code block is executed only when the script is run directly,
#and not when it is imported as a module into another script.
if __name__ == "__main__":
    main() 