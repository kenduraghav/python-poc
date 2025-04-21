def string_challenge():
    message = "  Welcome to Python Programming  "
    
    print("Original:", message)
    print("Stripped:", message.strip())
    print("Uppercase:", message.upper())
    print("Lowercase:", message.lower())
    print("Replace 'Python' with 'Coding':", message.replace("Python", "Coding"))
    print("Slice 'Welcome':", message.strip()[0:7])
    
string_challenge()


def transform_sentence(message):

    messages = message.split()
    total = len(messages)
    for i in range(total):
        messages[i] = messages[i].upper()
    
    return " ".join(messages)


transformed_msg = transform_sentence("Hello World! This is a test message.")
print(transformed_msg)


def transform_sentence_lc(message):
    return " ".join([word.upper() for word in message.split()]) 

transformed_msg_lc = transform_sentence_lc("Python is easy and fun.")
print(transformed_msg_lc)


def title_case_converter(message):
    return message.title()

title_cased_msg = title_case_converter("hELLo wORLD from PyTHON")
print(title_cased_msg)


def format_string(name, age):
    """
    Formats a string using f-string syntax.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        str: A formatted string greeting the person with their name and age.
    """
    return f"Hello, {name}! You are {age} years old."

print(format_string("Alice", 30))


def format_string_with_placeholders(name, age):
    return "Hello, {}! You are {} years old.".format(name, age)

print(format_string_with_placeholders("Bob", 25))

