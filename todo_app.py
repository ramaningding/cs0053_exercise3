# toDoApp.py

tasks=[]

def addtask(task):
    """Add a new task to the tasks list and confirm addition."""
    tasks.append(task)
    print("task added!")

def showTasks():
    """Display all tasks in a numbered list or show a message if no tasks exist."""
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    """Remove a task by its number (1-based) with validation and confirmation."""
    if len(tasks) == 0:
        print("No tasks to remove!")
        return
    
    if tasknumber < 1 or tasknumber > len(tasks):
        print(f"Invalid task number! Please enter a number between 1 and {len(tasks)}")
        return
    
    # Convert to 0-based index for internal use
    index = tasknumber - 1
    removed_task = tasks.pop(index)
    print(f"Task '{removed_task}' removed!!")

def main():
    """Run the main menu loop for the todo application with user interaction."""
    while True:
        print("\n" + "="*30)
        print("      TODO LIST MANAGER")
        print("="*30)
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("-"*30)
        ch = input("Please enter your choice (1-4): ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            try:
                n = int(input("enter task no to remove: "))
                removetask(n)
            except ValueError:
                print("Invalid input! Please enter a valid number.")   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()
