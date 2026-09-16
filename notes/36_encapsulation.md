# What is Object-Oriented Programming, and How Does Encapsulation Work?

**Object-oriented programming (OOP)** is a programming style where everything in code is treated like a real-world object. A class is a blueprint for creating objects — each object has **attributes** (data) and **methods** (behaviors).

### Reminder: Basic Class Syntax

    class ClassName:
       def __init__(self, parameters):
           attribute = value

       def method_name(self):
           # method logic

Example:

    class Car:
       def __init__(self, brand, color):
           self.brand = brand
           self.color = color

    # create two objects from the Car class
    car1 = Car('Toyota', 'red')
    car2 = Car('Lambo', 'green')

    print('Car 1 Brand:', car1.brand) # Car 1 Brand: Toyota
    print('Car 1 Color:', car1.color) # Car 1 Color: red

    print('Car 2 Brand:', car2.brand) # Car 2 Brand: Lambo
    print('Car 2 Color:', car2.color) # Car 2 Color: green

## The Four Principles of OOP
Encapsulation, inheritance, polymorphism, and abstraction. This lesson covers **encapsulation**.

## Encapsulation
The bundling of an object's attributes and methods into a single unit — the class. It hides the internal state behind public methods/attributes, while private attributes/methods control how data changes and who can access it.

### Example: Wallet with a Single-Underscore Convention

    class Wallet:
       def __init__(self, balance):
           self._balance = balance # For internal use by convention

       def deposit(self, amount):
           if amount > 0:
               self._balance += amount # Add to the balance safely

       def withdraw(self, amount):
           if 0 < amount <= self._balance:
               self._balance -= amount # Remove from the balance safely

> A single underscore prefix (`_balance`) is just a **convention** — it signals "internal use," but Python doesn't enforce it. Accessing it directly from outside the class goes against encapsulation and can lead to bugs.

### True Privacy with Double Underscore
A double underscore prefix (`__balance`) makes an attribute genuinely inaccessible from outside the class:

    class Wallet:
       def __init__(self, balance):
           self.__balance = balance # Private attribute

       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount # Add to the balance safely

       def withdraw(self, amount):
           if 0 < amount <= self.__balance:
               self.__balance -= amount # Remove from the balance safely

    account = Wallet(500)
    print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

### Accessing Private Data with a Getter
Define a public method like `get_balance()` to read the private attribute:

    class Wallet:
       def __init__(self, balance):
           self.__balance = balance

       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount

       def withdraw(self, amount):
           if 0 < amount <= self.__balance:
               self.__balance -= amount
      
       def get_balance(self):
           return self.__balance


    acct_one = Wallet(100)
    acct_one.deposit(50)
    print(acct_one.get_balance()) # 150

    acct_two = Wallet(450)
    acct_two.withdraw(28)
    print(acct_two.get_balance()) # 422

    acct_two.deposit(150)
    print(acct_two.get_balance()) # 572

### Private Helper Methods for Validation
A private `__validate` method can centralize validation logic used by multiple public methods:

    class Wallet:
       def __init__(self):
           self.__balance = 0

       def __validate(self, amount):
           if amount < 0:
               raise ValueError('Amount must be positive')

       def deposit(self, amount):
           self.__validate(amount)
           self.__balance += amount

       def withdraw(self, amount):
           self.__validate(amount)
           if amount > self.__balance:
               raise ValueError('Insufficient funds')
           self.__balance -= amount

       def get_balance(self):
           return self.__balance

    acct_one = Wallet()
    acct_one.deposit(3)
    print(acct_one.get_balance()) # 3

    acct_one.deposit(50)
    print(acct_one.get_balance()) # 53

    acct_one.deposit(-4)  # ValueError: Amount must be positive
    acct_one.withdraw(-8) # ValueError: Amount must be positive
    acct_one.withdraw(58) # ValueError: Insufficient funds

`__validate` runs behind the scenes inside `deposit()` and `withdraw()` to ensure the amount is always valid.

> A future lesson covers more on how double-underscore-prefixed attributes work internally.

---
**Summary:** Encapsulation locks down internal data behind clear public methods. This keeps classes safe from tampering and centralizes validation in one place — you can update or extend code freely, knowing outside code only touches the interfaces you expose.