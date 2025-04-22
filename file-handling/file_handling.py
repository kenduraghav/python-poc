import os

cwd = os.getcwd()
filePath = os.path.join(cwd, 'sample.txt')
print(cwd)

def write_file(file_path,content):
    # Open the file in write mode and write content to it
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        message = f"Error Writing to file: {e}"
        log_error(message)
        return message


def read_file(filepath): 
    # Open the file in read mode and read content from it
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        message = "read_file(): File not found"
        log_error(message)
        return message
    except Exception as e:
        message = f"Error read_file(): {e}"
        log_error(message)
        return message


def append_file(file_path, content):
    # Open the file in append mode and append content to it
    try:
        with open(file_path,'a') as file:
            file.write(f"\n{content}")
    except Exception as e:
        message = f"Error appending to file: {e}"
        log_error(message)
        return message


def read_file_by_line(filepath):
    # Open the file in read mode and read content from it line by line
    try:
        with open(filepath, 'r') as file:
            line = file.readline()
            while line:
                print(line)
                line = file.readline()
    except FileNotFoundError:
        message = "read_file_by_line(): File not found"
        log_error(message)
        return message
    except Exception as e:
        message = f"Error read_file_by_line: {e}"
        log_error(message)
        return message


def read_file_by_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # .strip() removes newline characters
    except FileNotFoundError:
        message = "read_file_by_lines(): File not found"
        log_error(message)
        return message
    except Exception as e:
        message = f"Error read_file_by_lines: {e}"
        log_error(message)
        return message



def log_error(message):
    with open("failed_logs.txt", "a") as log_file:
        log_file.write(message + "\n")


def get_user_input():
    return input(
            "\n"
            ############## File Handling Menu ##############\n"
            "Do you want to write or read a file?\n"
            "1 - write\n"
            "2 - read\n"
            "3 - append\n"
            "4 - read by line\n"
            "5 - read by lines\n"
            "0 - exit\n"
            "Enter your option: "
    ).strip().lower()


def run(filePath, option):
    while option != '0':
        if option == '1':
            content = input("Enter the content to write to the file: ")
            write_file(filePath, content)
            print(f"Content written to {filePath}")
        elif option == '2':
            content = read_file(filePath)
            print(f"Content of {filePath}:\n{content}")
        elif option == '3':
            content = input("Enter the content to append to the file:")
            append_file(filePath,content)
            print(f"Content appended to {filePath}")
        elif option == '4':
            content = read_file_by_line(filePath)
            print("Done!")
        elif option == '5':
            content = read_file_by_lines(filePath)
            print("Done!")
        else:
            print("Invalid option. Please try again.")
        option = get_user_input()


if __name__ == "__main__":
    #print the input aligned to the left
    #write a while loop until user exits (enter 5)
    run(filePath, get_user_input())

