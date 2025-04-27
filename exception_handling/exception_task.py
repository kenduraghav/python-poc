def  check_file_exists(file_path):
    """
    Check if a file exists at the given path.
    """
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        print("Error: file not found.")
        return False
    



if __name__ == "__main__":
    file_path = input("Enter the file path:")
    
    if check_file_exists(file_path):
        print("File exists.")
    else:
        print("File does not exist.")


def tiny_exception_task():
    try:
        num1 = int(input("Enter first number:"))    
        num2 = int(input("Enter second number:"))
        result = num1 // num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Operation completed.")




if __name__ == "__main__":
    tiny_exception_task()

