import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f'Task added: "{task}"')

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f'Task {task_number} marked as completed.')
    else:
        print("Invalid task number.")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Removed task: "{removed_task["task"]}"')
    else:
        print("Invalid task number.")

def main():
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
            task_num = int(input("Enter task number to mark complete: "))
            complete_task(task_num)
        elif choice == "4":
            view_tasks()
            task_num = int(input("Enter task number to remove: "))
            remove_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
