to_do_list = []
while True:
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        task = input("Enter the task to add: ")
        to_do_list.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the to-do list.\n")
    elif choice == "2":
        if not to_do_list:
            print("Your to-do list is empty.\n")
        else:
            print("To-Do List:")
            for index, item in enumerate(to_do_list, start=1):
                status = "Completed" if item['completed'] else "Not Completed"
                print(f"{index}. {item['task']} - {status}")
            print()
    elif choice == "3":
        if not to_do_list:
            print("Your to-do list is empty. Unable to mark any task as completed.\n")
        else:
            view_tasks = True
            while view_tasks:
                print("To-Do List:")
                for index, item in enumerate(to_do_list, start=1):
                    status = "Completed" if item['completed'] else "Not Completed"
                    print(f"{index}. {item['task']} - {status}")
                task_number = int(input("Enter the task number to mark as completed (0 to cancel): "))
                if 0 < task_number <= len(to_do_list):
                    to_do_list[task_number - 1]['completed'] = True
                    print(f"Task '{to_do_list[task_number - 1]['task']}' marked as completed.\n")
                    view_tasks = False
                elif task_number == 0:
                    print("Operation canceled.\n")
                    view_tasks = False
                else:
                    print("Invalid task number. Please try again.\n")
    elif choice == "4":
        print("Exiting the to-do list program. Goodbye!")
        break  
    else:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
