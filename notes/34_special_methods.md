# What Are Special Methods and What Are They Used For?

Special methods, also known as **"magic methods"** or **"dunder methods"** (double underscore), are Python methods that start and end with `__`.

You've already used them without knowing it. `3 + 4` quietly runs `3.__add__(4)` under the hood. While you *can* call special methods directly, you rarely do — `3 + 4` is far clearer than `3.__add__(4)`.

`__init__()` is the special method you'll see and use most (the class initializer), along with others like `__len__()` and `__str__()`.

> Think of special methods as the "directors" of the interaction between a programmer and the Python interpreter.

## When Python Automatically Calls Special Methods

- **Arithmetic operations** — `__add__()` (addition), `__sub__()` (subtraction), `__mul__()` (multiplication), `__truediv__()` (division)
- **String operations** — `__add__()` (concatenation), `__mul__()` (repetition), `__format__()` (formatting), `__str__()`/`__repr__()` (text conversion)
- **Comparison operations** — `__eq__()` (equality), `__lt__()` (less-than), `__gt__()` (greater-than)
- **Iteration operations** — `__iter__()` (returns an iterator), `__next__()` (fetches the next item)

Built-in types (strings, numbers) already know how to do these things. But for your **own classes**, Python doesn't know how to handle them automatically — that's where special methods come in.

## Without Special Methods

    class Book:
       def __init__(self, title, pages):
           self.title = title
           self.pages = pages

    book1 = Book("Built Wealth Like a Boss", 420)
    book2 = Book("Be Your Own Start", 420)

    print(len(book1)) # TypeError: object of type 'Book' has no len()
    print(str(book1)) # <__main__.Book object at 0x102ed2900>
    print(book1 == book2) # False even though they have the same number of pages

- `len(book1)` fails — Python doesn't know how to get length without `__len__()`
- `str(book1)` prints the default object representation without `__str__()`
- `book1 == book2` is `False` — Python compares by memory identity, not content

## With Special Methods

    class Book:
       def __init__(self, title, pages):
           self.title = title
           self.pages = pages

       def __len__(self):
           return self.pages

       def __str__(self):
           return f"'{self.title}' has {self.pages} pages"

       def __eq__(self, other):
           return self.pages == other.pages
      
    book1 = Book("Built Wealth Like a Boss", 420)
    book2 = Book("Be Your Own Start", 420)

    print(len(book1)) # 420
    print(len(book2)) # 420
    print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
    print(str(book2)) # 'Be Your Own Start' has 420 pages
    print(book1 == book2) # True

## Real-World Example: A Shopping Cart
A cart needs to: add items, remove items, get item count, check what's inside, check if an item exists, and access an item by index.

Special methods used:
- `__len__()` — get the number of items
- `__iter__()` — loop through items
- `__contains__()` — check if an item is in the cart
- `__getitem__()` — access an item by index

### Cart Class

    class Cart:
       def __init__(self):
           self.items = []

       def add(self, item):
           self.items.append(item)

       def remove(self, item):
           if item in self.items:
               self.items.remove(item)
           else:
               print(f'{item} is not in cart')

       def list_items(self):
           return self.items

       def __len__(self):
           return len(self.items)

       def __getitem__(self, index):
           return self.items[index]

       def __contains__(self, item):
           return item in self.items

       def __iter__(self):
           return iter(self.items)

### Using the Cart

    cart = Cart()
    cart.add('Laptop')
    cart.add('Wireless mouse')
    cart.add('Ergo keyboard')
    cart.add('Monitor')

    for item in cart:
       print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

    print(len(cart)) # 4
    print(cart[3]) # Monitor

    print('Monitor' in cart) # True
    print('banana' in cart) # False

    cart.remove('Ergo keyboard')

    print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

    cart.remove('banana') # banana is not in cart