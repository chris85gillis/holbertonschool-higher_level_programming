Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:


General

#**What is a superclass, baseclass or parentclass**

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


**What is a subclass**

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


**How to list all attributes and methods of a class or instance**

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


**When can an instance have new attributes**

	In Python, instances of a class can have new attributes added to them at any time during their lifetime. This flexibility is one of the dynamic features of Python. Here are some common scenarios in which you might add new attributes to an instance:

1. **During Initialization:** You can add attributes to an instance during its initialization (i.e., in the `__init__` method) by assigning values to them using the `self` keyword. These attributes become part of the instance as soon as it is created.

    ```python
    class MyClass:
        def __init__(self, attribute1, attribute2):
            self.attribute1 = attribute1
            self.attribute2 = attribute2

    instance = MyClass("value1", "value2")
    instance.new_attribute = "new_value"  # Adding a new attribute after initialization
    ```

2. **Dynamically After Initialization:** You can add new attributes to an instance at any point after its creation by simply assigning values to them. This can be useful when you want to store additional data as your program progresses.

    ```python
    instance = MyClass("value1", "value2")
    instance.new_attribute = "new_value"  # Adding a new attribute after initialization
    ```

3. **Conditional Attribute Creation:** You might conditionally add attributes to an instance based on certain conditions or logic within your code. This allows you to customize instances as needed.

    ```python
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)

    if student1.age < student2.age:
        student1.is_older = True  # Adding a new attribute conditionally
    else:
        student2.is_older = True
    ```

It's important to note that when you add new attributes to an instance, those attributes are specific to that instance and do not affect other instances of the same class. However, these attributes are not part of the class definition itself; they are unique to each instance. If you want to add attributes that are shared among all instances of a class, you should define them as class attributes in the class definition itself.

Adding attributes dynamically can be convenient, but it's essential to ensure that your code remains organized and well-documented to prevent unexpected behavior and maintainability issues.


**How to inherit class from another**

	In Python, you can create a subclass (also known as a derived class or child class) by inheriting from another class (known as a superclass or base class or parent class). Inheritance allows the subclass to inherit the attributes and methods of the superclass, and you can further customize or extend the subclass as needed.

Here's the basic syntax for inheriting a class from another:

```python
class Superclass:
    # Superclass attributes and methods

class Subclass(Superclass):
    # Subclass attributes and methods
```

Here's a step-by-step explanation of how to create a subclass by inheriting from a superclass:

1. Define the Superclass:
   Start by defining the superclass. This is the class from which you want to inherit attributes and methods.

   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           pass
   ```

2. Define the Subclass:
   Create the subclass by defining a new class and specifying the superclass in parentheses after the class name.

   ```python
   class Dog(Animal):
       def speak(self):
           return f"{self.name} says Woof!"
   ```

   In this example, `Dog` is the subclass, and it inherits from the `Animal` superclass.

3. Customize the Subclass:
   You can add new attributes and methods to the subclass or override the methods inherited from the superclass to customize its behavior.

   ```python
   class Cat(Animal):
       def speak(self):
           return f"{self.name} says Meow!"

       def chase_mouse(self):
           return f"{self.name} is chasing a mouse!"
   ```

   In this case, the `Cat` subclass adds a new method `chase_mouse()` in addition to overriding the `speak()` method from the `Animal` superclass.

4. Create Instances of the Subclass:
   You can create instances of the subclass, which will have access to both the inherited methods and any additional methods defined in the subclass.

   ```python
   dog = Dog("Buddy")
   cat = Cat("Whiskers")

   print(dog.speak())  # Output: Buddy says Woof!
   print(cat.speak())  # Output: Whiskers says Meow!
   print(cat.chase_mouse())  # Output: Whiskers is chasing a mouse!
   ```

That's the basic process of creating a subclass by inheriting from a superclass in Python. Inheritance allows you to build upon existing classes, promoting code reuse and creating a hierarchy of classes with specialized functionality.


**How to define a class with multiple base classes**

	In Python, you can define a class with multiple base classes by using a mechanism called "multiple inheritance." Multiple inheritance allows a class to inherit attributes and methods from more than one base class. To define such a class, you list the names of the base classes within parentheses after the class name.

Here's the basic syntax for defining a class with multiple base classes:

```python
class Subclass(BaseClass1, BaseClass2, ...):
    # Subclass attributes and methods
```

Here's a step-by-step explanation of how to define a class with multiple base classes:

1. Define the Base Classes:
   Start by defining the base classes that you want to inherit from. These are the classes whose attributes and methods you want to reuse in your subclass.

   ```python
   class Parent1:
       def method1(self):
           print("Method 1 from Parent1")

   class Parent2:
       def method2(self):
           print("Method 2 from Parent2")
   ```

2. Define the Subclass:
   Create the subclass by defining a new class and specifying the base classes within parentheses after the class name. Separate the base class names with commas.

   ```python
   class Child(Parent1, Parent2):
       def method3(self):
           print("Method 3 from Child")
   ```

   In this example, `Child` is the subclass, and it inherits from both `Parent1` and `Parent2`.

3. Customize the Subclass:
   You can add new attributes and methods to the subclass or override methods inherited from the base classes.

   ```python
   class Child(Parent1, Parent2):
       def method3(self):
           print("Method 3 from Child")

       def method1(self):
           print("Overridden Method 1 from Child")
   ```

   Here, the `Child` subclass overrides `method1` from `Parent1` with its own implementation.

4. Create Instances of the Subclass:
   You can create instances of the subclass, which will have access to the methods and attributes of both base classes.

   ```python
   child = Child()
   child.method1()  # Output: Overridden Method 1 from Child
   child.method2()  # Output: Method 2 from Parent2
   child.method3()  # Output: Method 3 from Child
   ```

That's how you define a class with multiple base classes using multiple inheritance in Python. Multiple inheritance can be a powerful feature, but it can also lead to complex class hierarchies, so use it judiciously and consider potential issues like method name conflicts (method overriding) and the method resolution order (MRO) when working with multiple base classes.


**What is the default class every class inherit from**

	In Python, every class implicitly inherits from a default base class called `object`. The `object` class is the root class for all classes in Python. It provides a set of fundamental methods and attributes that are available to all objects in Python. 

Here's a simple example to illustrate this:

```python
class MyClass:
    pass

my_instance = MyClass()

print(isinstance(my_instance, object))  # Output: True
```

In the above example, `MyClass` is a custom class that you've defined, but it still inherits from the `object` class, even though you haven't explicitly specified it. This means that `my_instance` is an instance of both `MyClass` and `object`.

The `object` class provides some fundamental methods such as `__str__`, `__repr__`, `__eq__`, and others that are inherited by all classes in Python. These methods are used for basic object manipulation and comparisons. You can override these methods in your custom classes to customize their behavior.

In Python 3, it's common to explicitly inherit from `object`, although it's not necessary because Python 3 classes automatically inherit from `object` if no other base class is specified:

```python
class MyClass(object):
    pass

my_instance = MyClass()

print(isinstance(my_instance, object))  # Output: True
```

In Python 2, it was necessary to explicitly inherit from `object` to enable some features associated with new-style classes. However, in Python 3, all classes are considered new-style classes and inherit from `object` by default.


**How to override a method or attribute inherited from the base class**

	In Python, you can override a method or attribute that is inherited from a base class (superclass) in a subclass by providing a new implementation in the subclass. This allows you to customize the behavior of the method or attribute for the specific needs of the subclass. Here's how you can override a method or attribute:

1. **Method Overriding:**

   To override a method inherited from a base class in a subclass, you define a new method with the same name in the subclass. The new method will replace the inherited method when called on instances of the subclass.

   ```python
   class BaseClass:
       def method(self):
           print("This is the method from the base class.")

   class SubClass(BaseClass):
       def method(self):
           print("This is the overridden method in the subclass.")

   instance = SubClass()
   instance.method()  # Output: This is the overridden method in the subclass.
   ```

   In this example, the `method()` of the `BaseClass` is overridden in the `SubClass`, and calling `method()` on an instance of `SubClass` executes the overridden version.

2. **Attribute Overriding:**

   To override an attribute inherited from a base class, you can assign a new value to that attribute in the subclass. This replaces the inherited attribute with the new value for instances of the subclass.

   ```python
   class BaseClass:
       attribute = "This is an attribute from the base class."

   class SubClass(BaseClass):
       attribute = "This is the overridden attribute in the subclass."

   instance = SubClass()
   print(instance.attribute)  # Output: This is the overridden attribute in the subclass.
   ```

   In this example, the `attribute` from the `BaseClass` is overridden in the `SubClass` by assigning a new value to it.

It's important to note that when you override a method or attribute in a subclass, the overridden version in the base class is completely replaced for instances of the subclass. If you want to extend or reuse the behavior of the method or attribute from the base class while adding some new functionality, you can call the base class's method or access its attribute using `super()` within the subclass's method:

```python
class BaseClass:
    def method(self):
        print("This is the method from the base class.")

class SubClass(BaseClass):
    def method(self):
        super().method()  # Call the method from the base class
        print("This is additional functionality in the subclass.")

instance = SubClass()
instance.method()
```

This way, you can both reuse the base class's behavior and add specific functionality in the subclass.


**Which attributes or methods are available by heritage to subclasses**

	In Python, when you inherit from a base class (superclass) and create a subclass, the subclass inherits all the attributes and methods that are defined in the base class unless they are marked as private (by starting with a double underscore `__`). Here's what is inherited by a subclass:

1. **Public Attributes and Methods:** Any attributes and methods that are not marked as private (i.e., they don't start with `__`) are inherited by the subclass. These attributes and methods are accessible and can be used directly in the subclass.

   ```python
   class BaseClass:
       def __init__(self):
           self.public_attribute = "I am a public attribute"

       def public_method(self):
           return "I am a public method"

   class SubClass(BaseClass):
       def __init__(self):
           super().__init__()

   instance = SubClass()
   print(instance.public_attribute)  # Accessing the inherited public attribute
   print(instance.public_method())   # Calling the inherited public method
   ```

2. **Protected Attributes and Methods:** In Python, there is no strict enforcement of access modifiers like "protected," but by convention, attributes and methods starting with a single underscore `_` are considered "protected." These attributes and methods are inherited by the subclass and can be used, but they are considered non-public, and it's a hint to other developers not to use them directly.

   ```python
   class BaseClass:
       def __init__(self):
           self._protected_attribute = "I am a protected attribute"

       def _protected_method(self):
           return "I am a protected method"

   class SubClass(BaseClass):
       def __init__(self):
           super().__init__()

   instance = SubClass()
   print(instance._protected_attribute)  # Accessing the inherited protected attribute
   print(instance._protected_method())   # Calling the inherited protected method
   ```

3. **Private Attributes and Methods:** Attributes and methods starting with double underscores `__` (e.g., `__private_attribute` or `__private_method`) are considered "private" in Python. They are name-mangled in a way that makes it harder to access them directly in the subclass. While technically inherited, they are not intended to be accessed directly in the subclass.

   ```python
   class BaseClass:
       def __init__(self):
           self.__private_attribute = "I am a private attribute"

       def __private_method(self):
           return "I am a private method"

   class SubClass(BaseClass):
       def __init__(self):
           super().__init__()

   instance = SubClass()
   # Attempting to access or call the private attribute/method directly will result in an AttributeError.
   ```

In summary, public and protected attributes and methods in the base class are inherited by the subclass and can be accessed and used directly. However, private attributes and methods are also technically inherited but are name-mangled in a way that discourages direct access from the subclass. They are intended to be treated as private implementation details of the base class and should not be relied upon or overridden in the subclass.


**What is the purpose of inheritance**

	Inheritance is a fundamental concept in object-oriented programming (OOP) with several important purposes and advantages:

1. **Code Reusability:** One of the primary purposes of inheritance is to promote code reuse. Instead of writing the same attributes and methods in multiple classes, you can define them once in a superclass and have multiple subclasses inherit these attributes and methods. This reduces code duplication and makes your code more maintainable.

2. **Modularity:** Inheritance allows you to create a modular and organized code structure. You can define common attributes and behaviors in a base class (superclass) and then create specialized subclasses that inherit and extend these features. This modular approach makes it easier to manage and update your code.

3. **Specialization and Customization:** Inheritance allows you to create specialized versions of a class by inheriting from a more general base class. Subclasses can customize the behavior of inherited methods or add new methods and attributes to tailor the class to specific requirements. This promotes flexibility and adaptability in your code.

4. **Polymorphism:** Inheritance is closely tied to the concept of polymorphism. Polymorphism allows objects of different classes to be treated as objects of a common base class. This enables you to write code that can work with a variety of objects, as long as they share a common interface defined in the base class. Polymorphism simplifies code and makes it more extensible.

5. **Code Organization:** Inheritance helps organize code hierarchies by modeling real-world relationships and hierarchies. For example, you can represent a hierarchy of animals with a base class "Animal" and subclasses like "Mammal," "Bird," and "Reptile." This makes the code structure intuitive and reflects the relationships between objects in the domain being modeled.

6. **Maintainability:** Inheritance can improve code maintainability because changes made to a base class are automatically inherited by its subclasses. This reduces the risk of introducing errors when updating the code, as you only need to make changes in one place (the base class) to affect all related subclasses.

7. **Encapsulation:** Inheritance can be used to encapsulate and hide implementation details in base classes while exposing a simplified interface to subclasses. This concept is known as information hiding or abstraction and helps manage complexity and reduce the likelihood of errors.

8. **Method Overriding:** Inheritance allows you to override methods from the base class in subclasses. This enables you to provide specialized implementations of methods in subclasses while maintaining a consistent interface defined by the base class.

In summary, the primary purpose of inheritance in OOP is to promote code reuse, modularity, and customization while improving code organization, maintainability, and flexibility. It allows you to model relationships and hierarchies in your code and leverage the principles of polymorphism and encapsulation.


**What are, when and how to use isinstance, issubclass, type and super built-in functions**

	In Python, the `isinstance()`, `issubclass()`, `type()`, and `super()` built-in functions are used to work with objects and classes in various ways. Here's an overview of each function, when to use them, and how to use them:

1. **`isinstance(object, classinfo)`**:

   - Purpose: To check if an object is an instance of a specific class or a tuple of classes.
   - When to use:
     - To test the type or class of an object.
     - In conditional statements to perform different actions based on the type of an object.
   - Example:

     ```python
     class Animal:
         pass

     class Dog(Animal):
         pass

     dog = Dog()
     
     print(isinstance(dog, Dog))    # True
     print(isinstance(dog, Animal)) # True
     print(isinstance(dog, str))    # False
     ```

2. **`issubclass(class, classinfo)`**:

   - Purpose: To check if a class is a subclass of a specific class or a tuple of classes.
   - When to use:
     - To check class inheritance relationships.
     - In conditional statements to determine if a class inherits from a particular base class.
   - Example:

     ```python
     class Animal:
         pass

     class Dog(Animal):
         pass

     print(issubclass(Dog, Animal)) # True
     print(issubclass(Animal, Dog)) # False
     ```

3. **`type(object)`**:

   - Purpose: To determine the type or class of an object.
   - When to use:
     - To retrieve the class of an object.
     - To perform type checking when you don't need to check for subclasses.
   - Example:

     ```python
     num = 42
     string = "Hello"
     
     print(type(num))    # <class 'int'>
     print(type(string)) # <class 'str'>
     ```

4. **`super([type[, object-or-type]])`**:

   - Purpose: To call methods and access attributes from a parent (superclass) class in the context of a subclass.
   - When to use:
     - In a subclass when you want to call a method or access an attribute from the superclass.
     - To avoid duplicating code by reusing methods and attributes from the superclass.
   - Example:

     ```python
     class Animal:
         def speak(self):
             return "Animal speaks"

     class Dog(Animal):
         def speak(self):
             return "Dog barks"

     dog = Dog()
     print(dog.speak())  # "Dog barks"
     
     # Using super() to call the superclass's method
     class Cat(Animal):
         def speak(self):
             return super().speak() + " and Cat meows"

     cat = Cat()
     print(cat.speak())  # "Animal speaks and Cat meows"
     ```

   In the example, `super()` is used to call the `speak()` method of the `Animal` superclass within the `Cat` subclass, allowing you to extend the behavior while reusing the superclass's method.


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
