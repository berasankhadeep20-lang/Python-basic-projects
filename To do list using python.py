#To do list using python
import random
def typewriter_effect(text, delay=0.05):
    import sys
    import time
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def todo_list():
    tasks = []
    while True:
        typewriter_effect("\nTo-Do List Menu:")
        typewriter_effect("1. Add Task")
        typewriter_effect("2. View Tasks")
        typewriter_effect("3. Remove Task")
        typewriter_effect("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            typewriter_effect(f'Task "{task}" added.')
        elif choice == '2':
            typewriter_effect("Your Tasks:")
            for idx, task in enumerate(tasks, 1):
                typewriter_effect(f"{idx}. {task}")
        elif choice == '3':
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                typewriter_effect(f'Task "{removed_task}" removed.')
            else:
                typewriter_effect("Invalid task number.")
        elif choice == '4':
            typewriter_effect("Exiting To-Do List. Goodbye!")
            break
        else:
            typewriter_effect("Invalid choice. Please try again.")
todo_list()