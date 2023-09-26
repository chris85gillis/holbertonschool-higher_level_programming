
# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General

## How to open a file

In Python, you can open a file using the `open()` function. Here's how you can do it:

```python
# Syntax: open(filename, mode, encoding)
# - filename: The name of the file you want to open.
# - mode: The mode in which you want to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
# - encoding (optional): The character encoding to use when reading or writing the file (e.g., 'utf-8' for UTF-8).

# Example 1: Opening a file for reading
file_name = "example.txt"
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Example 2: Opening a file for writing (creates the file if it doesn't exist, truncates it if it does)
output_file_name = "output.txt"
try:
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write("Hello, world!\n")
        file.write("This is a new line.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In the above examples:
- `open()` is used to open the file, specifying the file name, mode, and encoding (if needed).
- A `with` statement is used to ensure that the file is properly closed after reading or writing. This is good practice because it automatically handles exceptions and cleanup.
- In Example 1, the file is opened for reading (`'r'` mode), and its content is read using the `read()` method.
- In Example 2, the file is opened for writing (`'w'` mode), and text is written to it using the `write()` method. If the file doesn't exist, it will be created, and if it does exist, its content will be truncated (erased).


## How to write text in a file



How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure
How to access command line parameters in a Python script
