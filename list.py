# enhanced_todo_list.py
# Console-based Realtime To-Do List with Priority and Due Date

tasks = []  # List to store tasks as dictionaries

def display_tasks():
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. [{status}] {task['name']} | Priority: {task['priority']} | Due: {task['due_date']}")

def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    if priority not in ['High', 'Medium', 'Low']:
        priority = "Medium"
    due_date = input("Enter due date (e.g., 2026-01-15): ")
    task = {
        'name': name,
        'priority': priority,
        'due_date': due_date,
        'done': False
    }
    tasks.append(task)
    print(f"Task added: {name}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    display_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task deleted: {removed_task['name']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_done():
    if not tasks:
        print("No tasks to mark as done.")
        return
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            print(f"Task marked as done: {tasks[task_num - 1]['name']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    print("=== Welcome to the Enhanced To-Do List ===")

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark task as done")
        print("5. Exit")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()