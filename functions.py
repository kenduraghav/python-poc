def greet(name  = "World"): #default argument
    print(f"Hello, {name}!")  

greet()
greet("Raghav")

def calculateAge(birthyear):
    current_year=2025
    return current_year - birthyear

print("Calculate your age:")
age= int(input("Enter your birth year: "))
print(f"You are {calculateAge(age)} years old.")


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
