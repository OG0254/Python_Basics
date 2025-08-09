def task_manager():
    tasks = []

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append({"task": task, "completed": False})
            print(f"Task '{task}' added.")
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"{i + 1}. {task['task']} - {status}")
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["completed"] = True
                print(f"Task '{tasks[task_number]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                deleted_task = tasks.pop(task_number)
                print(f"Task '{deleted_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    task_manager()
