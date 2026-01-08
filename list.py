tasks = []  

def display_tasks():
    if not tasks:
        print("No tasks in your list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task added: {task}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    display_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task deleted: {removed_task}")
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
            tasks[task_num - 1] += " ✅"
            print(f"Task marked as done: {tasks[task_num - 1]}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    print("=== Welcome to the Realtime To-Do List ===")

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