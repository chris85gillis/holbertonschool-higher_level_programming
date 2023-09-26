#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read(), end='')  # Read and print the entire file
    except Exception as e:
        pass  # Do nothing in case of any exception
