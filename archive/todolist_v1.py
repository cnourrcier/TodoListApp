
#define a list to store the tasks.
#each task will be represented as a dictionary with 'title' and 'completed' keys.
tasks = []

#function to add tasks to the list.
#prompt user for the task title and add it to the 'tasks' list
def add_task():
    title = input("\nEnter the task: ")
    task = {'title': title, 'completed': False}
    tasks.append(task)
    print("task added successfully!")


#function to display all the tasks in the 'tasks' list
def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTasks: ")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{index}.{task['title']} - {status}")


#function to mark a task as completed based on the user's input
def mark_completed():
    if not tasks:
        print("No tasks in the list")
        return
    view_tasks()
    while True:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed!")
                break
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input. Please enter a valid task number")          

#main function
#lists options for user to choose from and calls functions based on user choice.
def main():
    while True:
        print("\nOptions: ")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")


#ensure the main code block is executed only when the script is run directly,
#and not when it is imported as a module into another script. 
if __name__ == "__main__":
    main()
        

