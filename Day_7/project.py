# Project: "To-Do List Manager"

print("TO-do List Manager\n")
print("Choose the option: ")
print("1. Add a Task")
print("2. Remove a Task")
print("3. View Tasks")
print("4. Complete a Task")

tasks = []
completed_tasks = []

user_choice = input("Choose a function (add, remove, view, complete): ")

if user_choice == 'add':
    user_input = input("Enter new task: ")
    tasks.append(user_input)
    print("Task added:", tasks)

elif user_choice == 'view':
    print("Your tasks:", tasks)

elif user_choice == 'remove':
    user_input = input("Enter task to remove: ")
    if user_input in tasks:
        tasks.remove(user_input)
        print("Task removed:", tasks)
    else:
        print("Task not found.")

elif user_choice == 'complete':
    user_input = input("Enter task to mark as complete: ")
    if user_input in tasks:
        tasks.remove(user_input)
        completed_tasks.append(user_input)
        print("Task completed:", completed_tasks)
    else:
        print("Task not found.")

else:
    print("Invalid choice.")






