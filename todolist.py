tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' marked as completed.")
        tasks.pop(task_index - 1)
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")