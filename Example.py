import json  # Unused import warning
import os
import math  # Unused import warning

TODO_FILE = "tasks.json"

# Function with too many parameters (Code Smell)
def load_tasks(file_path, encoding, max_size, verbose=True):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding=encoding) as file:
            return json.load(file)
    return []

# Function with hardcoded values (Security Vulnerability)
def add_task(task):
    tasks = load_tasks(TODO_FILE, "utf-8", 1024)  # Hardcoded file path (vulnerability)
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks, TODO_FILE)  # Hardcoded file path (vulnerability)
    print(f'Task added: "{task}"')

# Empty exception handler (Bug)
def view_tasks():
    tasks = load_tasks(TODO_FILE, "utf-8", 1024)
    try:
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")
    except:
        print("An error occurred while displaying tasks.")  # Bug: Empty exception

# Vulnerability: Insecure use of input without validation
def user_input():
    user_input = input("Enter task to add: ")  # Input not sanitized
    add_task(user_input)
