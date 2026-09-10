# What Are Methods and Attributes, and How Do They Work?

## Attributes
Attributes are variables that belong to an object — they hold data. There are two kinds: **instance attributes** and **class attributes**.

- **Instance attributes** — unique to each object, usually set via `__init__`.
- **Class attributes** — belong to the class itself, shared by all instances of that class.

You access attributes using **dot notation**.

### Example: Class vs Instance Attributes

    class Dog:
        species = "French Bulldog" # Class attribute

        def __init__(self, name):
            self.name = name # Instance attribute

    print(Dog.species) # French Bulldog

    dog1 = Dog("Jack")
    print(dog1.name)    # Jack
    print(dog1.species) # French Bulldog

    dog2 = Dog("Tom")
    print(dog2.name)    # Tom
    print(dog2.species) # French Bulldog

> Class attributes can be accessed directly from the class itself. Instance attributes require creating an object first.

### Another Example: Car Class

    class Car:
        def __init__(self, color, model):
            self.color = color
            self.model = model

    car_1 = Car("red", "Toyota Corolla")
    car_2 = Car("green", "Lamborghini Revuelto")

    print(car_1.model) # Toyota Corolla
    print(car_2.model) # Lamborghini Revuelto

    print(car_1.color) # red
    print(car_2.color) # green

## Methods
Methods are functions defined inside a class — they let objects perform actions that operate on or modify their own data. Also accessed via dot notation.

### Example: Dog with a bark() Method

    class Dog:
       species = "French Bulldog"

       def __init__(self, name):
         self.name = name

       def bark(self):
           return f"{self.name} says woof woof!"

    jack = Dog("Jack")
    jill = Dog("Jill")

    print(jack.bark()) # Jack says woof woof!
    print(jill.bark()) # Jill says woof woof!

### Example: Car with a describe() Method

    class Car:
        def __init__(self, color, model):
            self.color = color  # Instance attribute
            self.model = model  # Instance attribute

        def describe(self):
            return f"This car is a {self.color} {self.model}"

    car_1 = Car("red", "Toyota Corolla")
    car_2 = Car("green", "Lamborghini Revuelto")

    print(car_1.describe()) # This car is a red Toyota Corolla
    print(car_2.describe()) # This car is a green Lamborghini Revuelto