# toDoApp.py

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("task added!")

def confirmDeletion(tasknumber): 
     index = tasknumber - 1
    task_to_delete = tasks[index]
    confirm = input(f"Are you sure you want to delete '{task_to_delete}'? (y/n): ").strip().lower()
    if confirm == "y":
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Deletion cancelled.")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    if len(tasks) == 0:
        print("No tasks to remove!")
        return
    
    if tasknumber < 1 or tasknumber > len(tasks):
        print(f"Invalid task number! Please enter a number between 1 and {len(tasks)}")
        return
    confirmDeletion(tasknumber)

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
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
            break
        else:
            print("wrong choice!!")
main()
