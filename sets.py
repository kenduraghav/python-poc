course_A = {"Alice", "Bob", "Charlie", "David"}
course_B = {"Charlie", "Eve", "Frank", "Alice"}



# Find students who are enrolled in both courses
all_students = course_A.union(course_B)

print(f"Student list combined in both courses: {all_students}")


#student enrolled in both courses
students_in_both = course_A.intersection(course_B)
print(f"Students enrolled in both courses: {students_in_both}")

#print students who are only in course A
print(f"Students only in course A: {course_A - course_B }")

print(f"Students only in course B: {course_B - course_A }")

course_B.add("Grace")

course_A.remove("Bob")


print(f"Updated course A: {course_A }")
print(f"Updated course B: {course_B }")    