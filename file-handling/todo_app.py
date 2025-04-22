import os
import json

cwd = os.getcwd()
filePath = os.path.join(cwd,"todo.txt")

def load_task_id():
    try:
        with open ("ids.txt", "r") as file:
            task_id = int(file.read().strip())
            return task_id 
    except FileNotFoundError:
        print("ID file not found. Starting with ID 1.")
    except ValueError:
        print("Invalid ID in file. Starting with ID 1.")
    except Exception as e:
        print(f"Error loading task ID: {e}")    
    return 1

task_id = load_task_id()

def update_task_id(task_id):
    try:
        with open("ids.txt", "w") as file:
            file.write(str(task_id))
            print("Task ID updated successfully.")
    except Exception as e:
        print(f"Error updating task ID: {e}")


def load_tasks():
    try:
        if os.path.exists(filePath):
            with open(filePath,"r") as file:
                tasks = json.load(file)
                return tasks
    except FileNotFoundError:
        print("No tasks found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty task list.")
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return []   


def save_tasks(tasks):
    try:
        with open(filePath, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error saving tasks: {e}")


def add_task(tasks):
    task = input("Enter a new task: ")
    try:
        task_id = load_task_id()
        global filePath
        task_details = {
            "id": task_id,
            "task": task,
            "done": False
        }
        tasks.append(task_details)
        save_tasks(tasks)
        update_task_id(task_id + 1)
        print(f"Task '{task}' added to the list.")
    except Exception as e:
        print(f"Error adding task: {e}")


def view_tasks(tasks):
    try:
        if tasks:
            print("To-Do List:")
            for task in tasks:
                print(f"ID: {task['id']}, Task: {task['task']}, Done: {task['done']}")
        else:
            print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")
    except Exception as e:
        print(f"Error viewing tasks: {e}")


def mark_task_done(tasks):
    id = int(input("Enter the ID of the task to mark as done: "))
    try:
        for task in tasks:
            if task["id"] == id:
                task["done"] = True
                save_tasks(tasks)  
                print(f"Task ID {id} marked as done.")
                break   
        else:
            print(f"Task ID {id} not found.")
    except ValueError:
        print("Invalid ID. Please enter a valid task ID.")  
    except Exception as e:
        print(f"Error marking task as done: {e}")

def clear_tasks(tasks):
    try:
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    except Exception as e:
        print(f"Error clearing tasks: {e}")

def get_user_option():
    # Display the menu and get user option
    print("############ To-Do List Menu ############")
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Mark Task as Done")
    print("4 - Clear All Tasks")
    print("0 - Exit")
    option = input("Select an option: ")
    return option


def run():
    tasks = load_tasks()
    while True:
        option = get_user_option()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            mark_task_done(tasks)
        elif option =="4":
            clear_tasks(tasks)
        elif option == "0":
            print("Exiting the To-Do List App.")
            break
        else:
            print("Invalid option. Please try again.")
        print("\n")  # Add a newline for better readability between iterations

if __name__ == "__main__":
    run()