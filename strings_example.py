multiline = """
This is a multiline string example 
with triple quotes
It can span multiple lines
and can include 'single' and "double" quotes without escaping.
"""


single_line = 'This is a single line string example with single quotes.'

msg = " Hello, World! "

print(len(msg))

print(msg)
print(msg.strip()) # Remove leading and trailing whitespace

print(msg.lower()) # Convert to lowercase
print(msg.upper()) # Convert to uppercase
print(msg.replace("World", "Python")) # Replace substring
print(msg.split(",")) 
print(msg.find("World")) # Find substring index
print(msg[1:6]) # Slice string from index 1 to 6
print("Hello" in msg) # Check if substring exists

print("Hello" + ',' + 'World') # Concatenate strings
print("Hello " * 3) # Repeat string 3 times

print("Hello {0} {1}".format("World", "Python")) # Format string with placeholders
first = "John" 
last = "Doe"
full = first + " " + last 
print(full)

age = 25
print(f"My name is {full} and I am {age} years old.") # f-string formatting

name ="alice bob"

name = name.upper()
print(name)

print(name.capitalize())  #
#name = input("Enter your name: ")
print(f"Hello, {name.capitalize()}!")
for i in range(5):
    print("I'M THE LEGEND THANOS!")
for i in range(5):
    print("I have played these games before!")


total = (50*7/2)-25+50

print(total)