"""

``` python
try:
    # Code that might cause an exception
    risky_code()
except SomeException:
    # Code that runs if exception happens
    handle_the_error()

```

"""



try:
    a = 1/0
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")


#multiple exceptions
try: 
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



#else and finally 
# The else block executes if no exceptions occur in the try block.
# The finally block executes regardless of whether an exception occurred or not.
# finally is good for cleanup like closing files or connections.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError: 
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError: 
    print("Error: Division by zero is not allowed.")
else:
    print("No exceptions occurred. Result is valid.")
finally:
    print("Execution completed.")



# Raising exceptions
# You can raise exceptions using the raise statement.
# This is useful for custom error handling or when you want to enforce certain conditions.
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive.")
    return number


try:
    num = int(input("Enter a number"))
    check_positive(num)
except ValueError as e:
    print(f"Error: {e}")


"""
try	    Code that might fail
except	What to do if it fails
else	What to do if no error
finally	Always do this (cleanup, etc.)
raise	Throw your own error
"""