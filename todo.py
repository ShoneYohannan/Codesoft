tasks = []

def addTask():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def listTasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def deleteTask():
    listTasks()
    try:
        idx = int(input("Enter task number to delete: "))
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def updateTask():
    listTasks()
    try:
        idx = int(input("Enter task number to update: "))
        if 0 <= idx < len(tasks):
            new_task = input("Enter new task content: ")
            tasks[idx] = new_task
            print(f"Task #{idx} updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Update a task")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            updateTask()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
