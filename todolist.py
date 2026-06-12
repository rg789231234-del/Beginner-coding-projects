todolist=[]
while True:
    selection=int(input("Welcome to the to-do list. To start, select a choice: 1=Add task, 2=Check list, 3=Remove/Tick off task, 4=Exit:"))
    
    if selection==1:
        taskin=input("Enter the name of your task: ")
        todolist.append(taskin)
        print(todolist)
    
    elif selection==2:
        print(todolist)
    
    elif selection==3:
        print(todolist)
        remove=input("Enter the EXACT name of the task you want to remove/tick off: ")
        if remove in todolist:
            todolist.remove(remove)
        else:
            print("Error")
    
    elif selection==4:
        print("Exiting")
        break
    
    else:
        print("Error")
        
    