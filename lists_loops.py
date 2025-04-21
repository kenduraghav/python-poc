# skills = ["Python", "Java", "C++", "JavaScript"]
# print(f"Skills List: {skills}")

# print(f"Using regular indexing [skills[2]]: {skills[2]}")

# print(f"Using Negative indexing [skills[-1]]: {skills[-1]}")


colors = ["red", "green", "blue", "yellow"]

# Print 1st and last item using both positive and negative indexing
# print(f" Available colors: {colors}")
# print(f"1st item using positive indexing: {colors[0]}")
# print(f"Last item using positive indexing: {colors[-1]}")


# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print("Even numbers:", evens)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)


def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

numbers = [12, 7, 4, 9, 20]

for i in range(len(numbers)):
    print(f"The given number {numbers[i]} is { check_even_odd(numbers[i])} ")

