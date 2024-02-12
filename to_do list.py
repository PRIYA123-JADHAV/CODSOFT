tasks = {}

def add_task(task_description):
    task_id = len(tasks) + 1
    tasks[task_id] = {"description": task_description, "completed": False}
    print("Task added successfully!")

def update_task(task_id, new_description):
    if task_id in tasks:
        tasks[task_id]["description"] = new_description
        print(f"Task {task_id} updated successfully.")
    else:
        print("Task not found.")

def mark_task_complete(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print("Task not found.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task_id, task_info in tasks.items():
            status = "Completed" if task_info["completed"] else "Not Completed"
            print(f"{task_id}: {task_info['description']} - {status}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_complete(task_id)
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
