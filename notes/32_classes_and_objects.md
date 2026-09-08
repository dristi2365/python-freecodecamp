# How Do Classes Work and How Do They Differ From Objects?

Classes and objects work together to organize and manage data. You build a **class** to define shared behavior, then create **objects** that use those behaviors. A class is like a blueprint or template used to create objects.

## Basic Class Syntax

    class ClassName:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def sample_method(self):               
            print(self.name.upper())

- **`class ClassName`** — the `class` keyword followed by the class name. Python convention: use **PascalCase** for class names.
- **`def __init__(self, name, age)`** — a special method automatically called when a new object is created. It initializes the object's attributes.
- **`self`** — the first parameter of `__init__` (and other methods), a reference to the specific object being created/used. By convention it's named `self`, though technically any name works. It lets you access the object's own attributes and methods.
- **`self.name = name`** and **`self.age = age`** — the attributes the objects will have.
- **`def sample_method(self):`** — a method each object can call.

## Attributes vs Methods
- **Attributes** — like variables within a class, used to store data.
- **Methods** — functions defined within a class; the actions objects can perform.

## Example: A Dog Class

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name.upper()} says woof woof!")

## Creating Objects
General syntax:

    object_1 = ClassName(attribute_1, attribute_2)
    object_2 = ClassName(attribute_1, attribute_2)

Calling methods on objects:

    object_1.method_name()
    object_2.method_name()

## Full Example: Creating Dog Objects

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

    dog_1 = Dog("Jack", 3)
    dog_2 = Dog("Thatcher", 5)

    # Call the bark method
    dog_1.bark()  # JACK says woof woof! I'm 3 years old!
    dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

Here, `dog_1` is initialized with `"Jack"` and `3`, setting its `name` and `age` attributes. `dog_2` is initialized with `"Thatcher"` and `5`. Calling `.bark()` on each produces different output, since each object holds its own unique `name` and `age`.

## Class vs Object: Summary
- A **class** is the template/blueprint — it defines what data and behavior the object should have.
- An **object** is what's created using that template — it holds the actual data and uses that behavior.
- You write a class **once**, and can create many objects from it, each with different data.