
# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General

## How to open a file in read/write

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


## How to read the full content of a file

To read the full content of a file in Python, you can use the `open()` function with the `'r'` (read) mode. Here's how to do it:

```python
# Syntax: open(filename, mode, encoding)
# - filename: The name of the file you want to open for reading.
# - mode: 'r' for reading.
# - encoding (optional): The character encoding to use when reading the file (e.g., 'utf-8').

# Example: Reading the full content of a file
file_name = "example.txt"
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()  # Read the full content of the file
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example:

- We open the file "example.txt" in read mode (`'r'`).
- We use the `read()` method to read the full content of the file into the `content` variable.
- The `with` statement is used to ensure that the file is properly closed after reading. This is a recommended practice as it automatically handles exceptions and cleanup.

After running this code, the content of "example.txt" will be read and printed to the console.

Remember to handle exceptions, such as `FileNotFoundError`, which can occur if the specified file does not exist, as shown in the example.


## How to read a file line by line

You can read a file line by line in Python using a `for` loop. Here's how you can do it:

```python
# Syntax: open(filename, mode, encoding)
# - filename: The name of the file you want to open for reading.
# - mode: 'r' for reading.
# - encoding (optional): The character encoding to use when reading the file (e.g., 'utf-8').

# Example: Reading a file line by line
file_name = "example.txt"
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')  # Print each line without an extra newline
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example:

- We open the file "example.txt" in read mode (`'r'`).
- We use a `for` loop to iterate over the file object. This loop will read the file line by line, and the `line` variable will contain each line of text.
- We print each line using `print(line, end='')` to avoid adding an extra newline since each line from the file already contains a newline character.

This code will read and print the content of "example.txt" line by line. Make sure to handle exceptions like `FileNotFoundError` to account for cases where the specified file does not exist.


## How to move the cursor in a file

In Python, you can move the cursor (also known as the file pointer) within a file using the `seek()` method. The `seek()` method allows you to specify the new position for the cursor within the file. Here's how you can use it:

```python
# Syntax: file.seek(offset, whence)
# - offset: The new cursor position within the file.
# - whence (optional): The reference point from where the offset is measured. Default is 0 (absolute file positioning).
#   - 0: Start of the file (absolute file positioning)
#   - 1: Current position (relative file positioning)
#   - 2: End of the file (relative file positioning)

# Example: Moving the cursor within a file
file_name = "example.txt"
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # Read and print the first line
        first_line = file.readline()
        print("First Line:", first_line)

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Read and print the second line
        second_line = file.readline()
        print("Second Line (after moving the cursor):", second_line)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example:

- We open the file "example.txt" in read mode (`'r'`).
- We use the `readline()` method to read the first line of the file.
- Then, we use `seek(0)` to move the cursor back to the beginning of the file.
- Finally, we use `readline()` again to read the second line of the file after moving the cursor.

Keep in mind that the `seek()` method allows you to move the cursor to any position within the file, so you can use it to navigate to specific parts of the file as needed.


## How to make sure a file is closed after using it


What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure
How to access command line parameters in a Python script
