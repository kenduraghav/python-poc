# student = {
#     "name": "Alice",
#     "age": 22,
#     "course": "Computer Science"
# }

# # Access and print a value
# print(student["name"])

# # Modify a value
# student["age"] = 23

# # Add a new key-value pair
# student["grade"] = "A"

# # Print entire dictionary
# print(student)


book = {
    "title":"The Great Gatsby",
    "author":"F. Scott Fitzgerald",
    "year":1925,
}

print(book);

print(book["title"])

for key in book:
    print(key,":", book[key])

print(book.items())

book['genre'] = 'Fiction'
print(book)
print(book.keys())
print(book.values())

print(book.get('title'))
print(book.get('publisher', 'Not Found'))
del book['genre']
print(book.get('genre', 'Not Found'))

#what else we can learn with dictionaries go one by one for dictionaries in python
