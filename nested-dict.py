def created_nested_dict(id, name ,age, subjects):

    return { 
        'id': id, 'name': name, 'age': age, 'subjects': subjects 
    }
    

students = {}
students["1"] = created_nested_dict("1", "Alice", 22, ["Math", "Science"])

students["2"] = created_nested_dict("2", "Bob", 23, ["English", "History"])
students["3"] = created_nested_dict("3", "Charlie", 24, ["Art", "Music"])
students["4"] = created_nested_dict("4", "David", 25, ["Physics", "Chemistry"])

# print(students)

# print(students["4"])

for student_id, student_info in students.items():
    print(f"Student ID: {student_id}")
    print(f"  Name: {student_info['name']}")
    print(f"  Age: {student_info['age']}")
    print(f"  Subjects: {', '.join(student_info['subjects'])}")
    print("-" * 30)

