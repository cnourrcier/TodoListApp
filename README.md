# Task Management Script

This script is a simple task management tool that allows you to add tasks, view tasks, mark tasks as completed, and exit the program. Tasks are stored in a JSON file called "tasks.txt".

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)

## Features

- Add new tasks with a title, priority, and due date.
- View the list of tasks along with their details.
- Mark tasks as completed.
- Save and load tasks from a JSON file.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Usage

1. Clone this repository or download the script directly.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   <pre>
   python script.py
   </pre>

## Functionality

### Add a Task

- Prompts you to input task details: title, priority, and due date (in YYYY-MM-DD format).
- Validates input and ensures the task title is not empty.
- Saves tasks to the "tasks.txt" file in JSON format.

### View Tasks

- Displays a list of all tasks along with their details.
- Shows the task's completion status, priority, title, and due date.

### Mark Task as Completed

- Lists all tasks with their details.
- Allows you to mark a task as completed by selecting its corresponding task number.
- Updates the completion status of the task in the list and the "tasks.txt" file.

### Exit

- Terminates the program.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
