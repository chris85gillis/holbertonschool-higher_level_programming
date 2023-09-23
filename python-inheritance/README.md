Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:


General

What is a superclass, baseclass or parentclass

	In Python, a superclass, base class, or parent class is a class that serves as the blueprint for one or more derived classes (also known as subclasses or child classes). A superclass defines common attributes and behaviors that are shared by its subclasses, allowing you to create a hierarchy of classes with specialized functionality. 

	Here's a simple example to illustrate the concept:

	```python
	class Animal:
    	def __init__(self, name):
        	self.name = name

    	def speak(self):
        	pass

	class Dog(Animal):
    	def speak(self):
        	return f"{self.name} says Woof!"

	class Cat(Animal):
    	def speak(self):
        	return f"{self.name} says Meow!"

	dog = Dog("Buddy")
	cat = Cat("Whiskers")

	print(dog.speak())  # Output: Buddy says Woof!
	print(cat.speak())  # Output: Whiskers says Meow!
	```

	In this example, `Animal` is the superclass or base class, and `Dog` and `Cat` are subclasses or child classes. The `Animal` class defines a common attribute (`name`) and a method (`speak`) that all animals share. Both `Dog` and `Cat` inherit these attributes and methods from the `Animal` class but provide their own implementations of the `speak` method to customize their behavior.

	Superclasses are used to promote code reusability, maintainability, and to create a logical hierarchy of classes in object-oriented programming.


What is a subclass

	In object-oriented programming, a subclass, also known as a derived class or child class, is a class that inherits properties and behaviors (attributes and methods) from another class called the superclass or base class or parent class. Subclasses are created to extend or specialize the functionality of the superclass. This is a fundamental concept in inheritance, which is one of the four fundamental principles of object-oriented programming (OOP), along with encapsulation, abstraction, and polymorphism.

	Here are some key points about subclasses:

	1. **Inheritance:** Subclasses inherit attributes and methods from their superclass. This means that they have access to all the attributes and methods of the superclass, and they can also override or extend those inherited members.

	2. **Specialization:** Subclasses are used to create more specific, specialized versions of the superclass. They can add additional attributes and methods, modify the behavior of inherited methods, or provide new methods.

	3. **Code Reusability:** Inheritance promotes code reuse. Instead of redefining common attributes and behaviors in every class, you can define them once in a superclass and have multiple subclasses inherit them.

	4. **Hierarchical Structure:** You can create a hierarchical structure of classes by having multiple levels of inheritance. A subclass can itself become a superclass for another subclass, forming a chain of inheritance.

	Here's a simple Python example to illustrate the concept:

	```python
	class Vehicle:
    	def __init__(self, brand, year):
        	self.brand = brand
        	self.year = year

    	def start_engine(self):
        	print(f"{self.brand} vehicle's engine started.")

	class Car(Vehicle):
    	def start_engine(self):
        	print(f"{self.brand} car's engine started.")

	class Motorcycle(Vehicle):
    	def start_engine(self):
        	print(f"{self.brand} motorcycle's engine started.")

	car = Car("Toyota", 2022)
	motorcycle = Motorcycle("Harley-Davidson", 2023)

	car.start_engine()  # Output: Toyota car's engine started.
	motorcycle.start_engine()  # Output: Harley-Davidson motorcycle's engine started.
	```

	In this example, `Car` and `Motorcycle` are subclasses of the `Vehicle` superclass. They inherit the `brand` and `year` attributes from `Vehicle` and override the `start_engine` method to provide their own implementations.

	Subclasses allow you to create a more organized and modular code structure by modeling real-world relationships and hierarchies in your software.


How to list all attributes and methods of a class or instance

In Python, you can list all attributes and methods of a class or an instance using the following techniques:

1. Using the `dir()` Function:
   The `dir()` function is a built-in Python function that returns a list of names in the current local scope. When you pass a class or an instance as an argument to `dir()`, it will return a list of attributes and methods associated with that class or instance.

   Here's how to use `dir()`:

   ```python
   class MyClass:
       def __init__(self):
           self.my_attribute = 42

       def my_method(self):
           pass

   instance = MyClass()

   # List attributes and methods of the class
   print(dir(MyClass))

   # List attributes and methods of an instance
   print(dir(instance))
   ```

   The `dir()` function will return a long list of names, including built-in methods and attributes. Some of them will be preceded by underscores, which indicates that they are considered "private" in Python convention.

2. Using `vars()` for Instances:
   The `vars()` function returns the `__dict__` attribute of an instance, which is a dictionary containing the instance's attributes and their values. While this method primarily lists attributes, it won't list methods. Here's how to use it:

   ```python
   class MyClass:
       def __init__(self):
           self.my_attribute = 42

       def my_method(self):
           pass

   instance = MyClass()

   # List attributes of an instance
   print(vars(instance))
   ```

   This will output: `{'my_attribute': 42}`

3. Using `__dict__` Attribute for Classes:
   You can also directly access the `__dict__` attribute of a class to see its attributes. This method is similar to `vars()` but applied to the class itself:

   ```python
   class MyClass:
       def __init__(self):
           self.my_attribute = 42

       def my_method(self):
           pass

   # List attributes of a class
   print(MyClass.__dict__)
   ```

	This will output a dictionary containing the class's attributes, methods, and other class-related data.

Please note that in all of these methods, you may see some built-in methods and attributes, as well as those that are part of the class's internal implementation. To get a cleaner list of user-defined attributes and methods, you may want to filter the results based on your specific criteria.
When can an instance have new attributes
How to inherit class from another
How to define a class with multiple base classes
What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functions

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

Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case
