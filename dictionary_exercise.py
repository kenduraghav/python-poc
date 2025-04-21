students_score = {
    "John": 85,
    "Jane": 92, 
    "Dave": 78,
    "Alice": 95,
}


students = {
    "Alice": {"age": 22, "subjects": ["Math", "Science"]},
    "Bob": {"age": 21, "subjects": ["English", "History"]}
}

# 1. Add a subject for Alice
students["Alice"]["subjects"].append("Art")

# 2. Print the student name, age, and subjects
for student, details in students.items():
    print(f"Name: {student}, Age: {details['age']}, Subjects: {', '.join(details['subjects'])}")


del students["Alice"]["subjects"]
students["Bob"]["subjects"].remove("History")

print(students)
# for student, score in students_score.items():
#     print(f"{student}: {score}")

# print(students_score.get("Bob", "Bob's score not available"))


if __name__ == "__main__":
    # Example usage
    print("Student scores:")
    for student, score in students_score.items():
        print(f"{student}: {score}")

    # Check if a student's score is available
    student_name = "Bob"
    score = students_score.get(student_name, f"{student_name}'s score not available")
    print(score)