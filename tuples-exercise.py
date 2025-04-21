students = (101, "John", 85.5)
# Accessing elements

id, name, score = students
print(f"ID: {id}, Name: {name}, Score: {score}")

print("-" * 20)

students = [
    (101, "John", 85.5),
    (102, "Jane", 92.0),
    (103, "Dave", 78.5),
    (104, "Alice", 95.0),
]

# Accessing elements
for student in students:
    id, name, score = student
    print(f"ID: {id}, Name: {name}, Score: {score}")

print("-" * 20)
print(" Nested tuples")
def nested_tuples():
    return(
        (
            101, "John",
            ("English", "Math", "Science")
        ),
        (
            102, "Jane",
            ("History", "Math", "Art")
        ),
        (
            103, "Dave",
            ("English", "History")
        ),
        (
            104, "Alice",
            ("Math", "Science", "Art")
        )
    )

nested_tuples = nested_tuples()

for students in nested_tuples:
    id, name, subjects = students
    print(f"ID: {id}, Name:{name}")
    print(f"Subjects: {', '.join(subjects)}")
    print("-" * 20)
          