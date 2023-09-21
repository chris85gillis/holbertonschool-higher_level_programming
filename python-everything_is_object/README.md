Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is an object...
	- It is something a variable can refer to. 
	a = [1, 2, 3]
		- In the above example a is the variable that is refering to the object [1, 2, 3]

What is the difference between a class and an object or instance...
	- A class serves as a blueprint or template for creating objects. 
		- It defines the structure and behavior of object of a particular type. For example: if you have
		a class called "Car", it would define what properties (make, model, color) and methods (start,stop,
		accelerate) a car object can have and what they do.
	- An object is an instance of a class, meaning it is a specific realization or occurrence of the class's blueprint.
		-Objects have their own set of property values, which can differ from one isntance to anther. 

What is the difference between immutable object and mutable object...
	- Immutable and mutable objects are two different concepts in programming that describe whether an object's state (data)
	can be changed after it is created. The key difference between them lies in whether the object's data can be modified once
	it's been assigned a value. 
		- Immutable objects cannot be changed after it is created. 
			- Examples: numbers (integers, floats), strings, and tuples
		- Mutable objects is an object whose state can be modified after it is created. 
			- Examples: dictionaries, sets, and custom objects

What is a reference
	- It is a value that refers to or identifies a specific memory location or objects in a computer's memeory.
	- They are used to access and manipulate data stored in memory. 

What is an assignment
	- It is a operation that involves storing a value or data in a variable or data structure. It assigns a specific value
	or result of an expression to a variable, allowing you to store and manipulate data within a program. 
		- They are used to give names (variables) to data so that it can be used and manipulated later in the program.

What is an alias
	- Refers to an alternative name or identifier that can be used to refernce a variable, function, or other program.
		x = 10
		y = x  # y is now an alias for the value stored in x

How to know if two variables are identical
	- To check if two variables have the same value, you can use the equality operator ('==')
		x = 10
		y = 10

		if x == y:
    		print("x and y have the same value.")

How to know if two variables are linked to the same object
	- You can use the identity operator ('is')
		a = [1, 2, 3]
		b = a  # Both variables reference the same list object

		if a is b:
    		print("a and b reference the same object.")


How to display the variable identifier (which is the memory address in the CPython implementation)
	- You can display the memory address (identifier) of a variable using the 'id()' function. 
	The 'id()' function returns the unique identifier (memory address) of an object.
		x = 42
		print(id(x))

		-In the above example 'id(x)' will return the memory address of the integer object '42', 
		and 'print()' will display that address. 

What are the built-in mutable types
	Lists:
		These are ordered collections of items that can be of mixed data types. You can change the elements of a list
		after it's created using methods like 'append()', 'insert()', 'remove()', and assignment to specific indices.
			my_list = [1, 2, 3]
			my_list.append(4)   # Adds an element to the end
			my_list[0] = 0      # Modifies an element
	Dictionaries:
		These are unordered collections of key-value pairs. You can add, modify, or remove key-balue pairs in a dictionary.
			my_dict = {"name": "Alice", "age": 30}
			my_dict["age"] = 31  # Modifies a value
			my_dict["city"] = "New York"  # Adds a new key-value pair
	Sets:
		Are unordered collection of unique elements. You can add and remove elements from a set. 
			my_set = {1, 2, 3}
			my_set.add(4)    # Adds an element
			my_set.remove(2) # Removes an element
	Byte Arrays: 
		Are mutable sequences of bytes. You can modify individual bytes or the contents of a byte array.
			my_bytes = bytearray(b'Hello')
			my_bytes[1] = 111  # Modifies a byte
	Array Module Arrays:
		You can create arrays of various data types that are mutable this way. You can modify elements in an array 
		created using this module.
			import array
			my_array = array.array('i', [1, 2, 3])
			my_array[0] = 0    # Modifies an element

What are the built-in immutable types
	Integers:
		These values are immutable. Once you creat an integer object, you cannot change its value.
			x = 5
			# Attempting to change the value of x will result in creating a new integer object.
	Floats:
		Floating-point numbers are also immutable, like integers.
			pi = 3.14159
			# You cannot change the value of pi; you would create a new float object instead.
	Strings: 
		Are sequences of characters and are ummutable. You can create new strings by modifying or concatenating exisiting ones,
		but the original strings remain unchanged. 
			text = "Hello, world!"
			new_text = text + " Goodbye!"  # Creates a new string
	Tuples:
		Are ordered collections of elements that can be mixed data types. 
			my_tuple = (1, 2, 3)
			# You cannot modify the elements of my_tuple; you'd have to create a new tuple.
	Namedtuples:
		Are a type of tuple with named fields.
			from collections import namedtuple
			Point = namedtuple("Point", ["x", "y"])
			p = Point(1, 2)
			# You cannot change the values of x or y in p.
	Frozen Sets:
		These are immutable sets, and their elements cannot be changed or added after creation.
			my_frozen_set = frozenset({1, 2, 3})
			# You cannot modify the contents of my_frozen_set.
	Bytes:
		Bytes objects in Python are immutable squences of bytes.
			my_bytes = b"Hello"
			# You cannot change the content of my_bytes.
	Complet Numbers:
		These are also ummutable.
			z = 3 + 4j
			# The real and imaginary parts of z cannot be changed directly.

How does Python pass variables to functions
	- Variables are passed to functions using a mechanism know as "pass-by-object-reference." This 
	means that when you pass a variable to a function, you are passing a refernce to the object that the variable points to, rather than
	a copy of the object itself. This is consistnet for both mutable and immutable objects, but the way changes affect the original 
	depends on whether the object is mutable or not.
		IMMUTABLE OBJETS:
			def modify_immutable(x):
    			x = x + 1  # Create a new integer object and reassign x to it
    			return x

			y = 5
			modified_y = modify_immutable(y)
			# y remains 5; modified_y is 6
		MUTABLE OBJETS:
			def modify_mutable(my_list):
    			my_list.append(4)  # Modify the original list

			my_nums = [1, 2, 3]
			modify_mutable(my_nums)
			# my_nums is now [1, 2, 3, 4]


Requirements

Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc

.txt Answer Files
Only one line
No Shebang on the first line (i.e. “#!/usr/bin/python3”)
All your files should end with a new line