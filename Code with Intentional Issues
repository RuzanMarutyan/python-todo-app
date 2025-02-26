import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)  # Missing error handling here, should handle potential errors
    return []  # Code Smell: Could be improved by logging or handling an empty file more explicitly

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Missing error handling for file write operation (IOError)

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f'Task added: "{task}"')  # Code Smell: No check for duplicate tasks

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if len(tasks) == 0:  # Code Smell: Could be optimized to just check for empty list directly
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def complete_task(task_number):
    """Complete a task."""
    tasks = load_tasks()
    if task_number > len(tasks) or task_number < 1:  # Bug: This check is inverted, should be <= not >
        print("Invalid task number.")
        return
    tasks[task_number - 1]["completed"] = True
    save_tasks(tasks)
    print(f'Task {task_number} marked as completed.')

def remove_task(task_number):
    """Remove a task from the list."""
    tasks = load_tasks()
    if task_number <= 0 or task_number >= len(tasks):  # Bug: This check is incorrect, should be < len(tasks)
        print("Invalid task number.")
        return
    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f'Removed task: "{removed_task["task"]}"')

def main():
    """Main function to interact with the to-do list."""
    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                task_num = int(input("Enter task number to mark complete: "))  # Bug: No validation for non-integer input
                complete_task(task_num)
            except ValueError:  # Code Smell: User input not sanitized, error handling is minimal
                print("Invalid input, please enter a number.")
        elif choice == "4":
            view_tasks()
            try:
                task_num = int(input("Enter task number to remove: "))  # Bug: No validation for non-integer input
                remove_task(task_num)
            except ValueError:  # Code Smell: User input not sanitized, error handling is minimal
                print("Invalid input, please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
