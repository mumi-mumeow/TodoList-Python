Todo_List = []

while True :
    print("---------- To do List Menu ----------")
    print("1.Add Task\n" \
          "2.Delete Task\n" \
          "3.View All Tasks\n" \
          "4.Exit")
    menu = input("Select menu (1-4) : ")

    if menu == "1" :
        task = input("Enter your task : ")
        Todo_List.append(task)
        print("Task added successfully!")

    elif menu == "2" :
        if len(Todo_List) == 0 :
            print("Your to do list is empty")
        else :
            print("\nYour Task : ")
            for i in range(1, len(Todo_List)+1) :
                print(f"{i}.{Todo_List[i-1]}")
        
            index = int(input("\nEnter task number to delete : "))
        
            remove = Todo_List.pop(index-1)
            print(f"Deleted : {remove}")

    elif menu == "3" :
        if len(Todo_List) == 0 :
            print("Your to do list is empty")
        else :
            print("\nYour Task : ")
            for i in range(1, len(Todo_List)+1) :
                print(f"{i}.{Todo_List[i-1]}")

    elif menu == "4" :
        print("Have a nice day !")
        break

    else : 
        print("Invalid menu. Please select from 1 to 4 ")