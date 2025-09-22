# toDoApp.py

tasks = []


def add_task(task):
    """
    Add a new task to the tasks list and confirm addition.
    """
    tasks.append(task)
    print("task added!")


def confirm_deletion(task_number):
    """
    Prompt user for confirmation before deleting a task and handle the deletion.
    """
    index = task_number - 1
    task_to_delete = tasks[index]
    confirm = input(
        f"Are you sure you want to delete '{task_to_delete}'? (y/n): "
        ).strip().lower()
    if confirm == "y":
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Deletion cancelled.")


def show_tasks():
    """
    Display all tasks in a numbered list or show a message if no tasks exist.
    """
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])


def remove_task(task_number):
    """
    Remove a task by its number (1-based) with validation and confirmation.
    """
    if len(tasks) == 0:
        print("No tasks to remove!")
        return  
    elif task_number < 0 or task_number > len(tasks):
        print(
            "Invalid task number! Please enter a number between 1 and "
            f"{len(tasks)}"
            )
        return
    else:
        confirm_deletion(task_number)


def main():
    """
    Run the main menu loop for the to-do application with user interaction.
    """
    while True:
        print("\n" + "="*30)
        print("      TO-DO LIST MANAGER")
        print("="*30)
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("-"*30)
        ch = input("Please enter your choice (1-4): ")
        if ch == "1":
            t = input("enter task : ")
            add_task(t)
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            try:
                n = int(input("enter task no. to remove: "))
                remove_task(n)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif ch == "4":
            break
        else:
            print("wrong choice!!")


main()
