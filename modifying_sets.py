colors = {"red", "green", "blue"}
print(colors)

colors.add("white")
print(f"set.add: {colors}")

colors.update({"yellow", "black"})
print(f"set.update: {colors}")


colors.discard("pink")

print(f"set.discard: {colors}")

#colors.remove("pink")  # This will raise a KeyError if "pink" is not found

print("---" * 20)

students = {"Alice", "Bob", "Charlie"}
students.add("Diana")
students.update(["Eve", "Frank"])
students.discard("Zara")  # Should not raise an error
students.remove("Charlie")
removed = students.pop()
print(f"Removed Element from Set: {removed}")
print(f"Final Students: {students}")
students.clear();
print(students)
