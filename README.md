# TodoListApp
A simple command-line based Todo List application written in Python.

Description

This Python script allows users to manage a list of tasks, including adding new tasks, viewing existing tasks, and marking tasks as completed. 

Updates 8/5/23

- modified 'add_task' function to save tasks to the "tasks.txt" file after adding them to the 'tasks' list.

- created new function 'load_tasks' to read the tasks from the "tasks.txt" file and populate the 'tasks' list.

- modified code to store and update task completion status in "tasks.txt" file.

Updates 8/6/23

- modified file writing and reading to json format for more structure and efficiency. 

- updated method of loading tasks from "tasks.txt" for better efficiency. 

- added an additional error handling message in load_tasks() function to address potentially corrupted files.

- added additional validation feature in add_task() function to handle empty user input.
