# What Is Inheritance and How Does It Promote Code Reuse?

**Inheritance** is a key OOP concept: a **subclass** (child class) can use the attributes and methods of a **base class** (parent class). This enables code reuse, clear class hierarchies, and customized behavior without rewriting everything — by extending or overriding methods in the child class.

## Basic Syntax

    class Parent:
        # Parent attributes and methods

    class Child(Parent):
        # Child inherits, extends, and/or overrides where necessary

Passing `Parent` into `Child`'s definition is what creates the inheritance. This is **single inheritance** — a child class inheriting from exactly one parent.

## Example: Inheriting Attributes and Methods

    class Animal:
        def __init__(self, name):
            self.name = name

        def sound(self):
            return f'{self.name} makes a sound'

    class Dog(Animal):
        bark = 'woof! woof!! woof!!!'

    jack = Dog('Jack')
    print(jack.sound())  # Jack makes a sound
    print(jack.bark)  # woof! woof!! woof!!!

`Dog` reuses `self.name` and `sound()` from the parent `Animal` class without redefining them.

## Overriding a Method
Redefine a parent method in the child class to change its behavior:

    class Animal:
        def __init__(self, name):
            self.name = name

        def sound(self):
            return f'{self.name} makes a sound.'

    class Dog(Animal):
        bark = 'woof! woof!! woof!!!'

        # Override sound() to use bark class variable
        def sound(self):
            return f'{self.name} barks {self.bark}'

    jack = Dog('Jack')
    print(jack.sound())  # Jack barks woof! woof!! woof!!!

## Extending a Method with super()
To keep the parent's original behavior *and* add to it, use `super()`:

    class Animal:
        def __init__(self, name):
            self.name = name

        def sound(self):
            return f'{self.name} makes a sound'

    class Dog(Animal):
        bark = 'woof! woof!! woof!!!'

        # Call Animal.sound(), then append bark
        def sound(self):
            base = super().sound()
            return f'{base}, then {self.name} barks {self.bark}'

    jack = Dog('Jack')
    print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!

Here, `base` holds the result of calling `Animal`'s `sound()`, and the `Dog`-specific sound is appended to it — extending functionality while preserving the original behavior.

## Multiple Inheritance
A child class can inherit from **more than one** parent class.

### Basic Syntax

    class Parent:
        # Attributes and methods for Parent

    class Child:
        # Attributes and methods for Child

    class GrandChild(Parent, Child):
        # GrandChild inherits from both Parent and Child
        # GrandChild can combine or override behavior from each

### Example: A Frog (Walker + Swimmer)

    class Walker:
        def walk(self):
            return 'I can walk on land'

    class Swimmer:
        def swim(self):
            return 'I can swim in water'

    # Amphibian inherits from both Walker and Swimmer
    class Amphibian(Walker, Swimmer):
        def __init__(self, name):
            self.name = name

        def introduce(self):
            return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

    frog = Amphibian('Freddy')
    print(frog.introduce())
    # Output: I'm Freddy the frog. I can walk on land and I can swim in water