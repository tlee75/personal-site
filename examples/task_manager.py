# This program will behave as a to do list which keeps track of tasks
# The tasks may be added and removed using command line prompts
# Each task must have a unique name and an integer based priority

import json
from pathlib import Path

# Set the path to the task file globally
file_path = Path('tasks.txt')

# This function is called by other functions in order to open the task list from file
def OpenTasks():

    task_dict = dict()
    if file_path.is_file():

        with open(file_path, mode="r+") as tasks:
            try:
                task_dict = json.load(tasks)
            except:
                print("Found empty task file, initializing...")
                tasks.write(json.dumps({}))
    return task_dict

# Used to display the current task list retrieved from file, as well as the possible commands
def Display():
    tasks = OpenTasks()
    print("------------------")
    print("Tasks:\n")
    for k,v in tasks.items():
        print(f"{k}: {v['body']} - Priority {v['priority']}")
    if len(tasks) == 0:
        print("\nYou have no tasks!\n")
    print("\nCommands:\n")
    print("new - Insert new task:")
    print("delete - Remove a task")
    print("quit - Exit the program")

# Walks the user through inputting a new task
def NewTask():
    # Read the existing tasks from file, if any, and store them in a dictionary
    tasks = OpenTasks()

    # Obtain the name of a task, must be unique
    while True:
        task_name = input("Name of Task: ")
        if task_name in tasks or not task_name:
            print("WARN: You must use a unique task name")
            continue
        else:
            break

    # Obtain task description, cannot be left blank
    while True:
        task_body = input("Task Description: ")
        if not task_body:
            print("WARN: You must enter a task description")
            continue
        else:
            break

    # Obtain task priority, must be an integer
    while True:

        try:
            task_priority = int(input("Task Priority: "))
        except:
            print("WARN: You must enter an integer based priority number")
            continue
        else:
            break

    # Create the new task entry
    tasks[task_name] = {'priority':task_priority, 'body': task_body}

    # Write the updated task dictionary to file
    with open(file_path, mode="w") as task_file:
        try:
            task_file.write(json.dumps(tasks))
        except:
            print("ERROR: Error occurred while attempting to write the file")

# Walks the user through deleting an existing task
def DeleteTask():
    # Read the existing tasks from file, if any, and store them in a dictionary
    tasks = OpenTasks()
    print("Deleting task...")

    # Fetch the name of the task to delete, must exist
    while True:
        task_name = input("Name of Task: ")
        if task_name not in tasks:
            print("WARN: You must enter a valid task name")
            continue
        else:
            break
    try:
        del tasks[task_name]
    except:
        print("ERROR: Error while trying to delete task")

    # Write modified task list back to file
    with open(file_path, mode="w") as task_file:
        try:
            task_file.write(json.dumps(tasks))
        except:
            print("ERROR: Error occurred while attempting to write the file")

# main program loop which prompts for commands
def main():
    running = True
    while running:
        Display()
        command = input("\nEnter Command: ")
        if command == 'quit':
            print("Bye!")
            running = False
        elif command == 'new':
            NewTask()
        elif command == 'delete':
            DeleteTask()
        else:
            print("------------------")
            print("ERROR: Invalid command, please try again")


if __name__ == "__main__":
    main()
