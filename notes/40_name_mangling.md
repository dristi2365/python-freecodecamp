# What Is Name Mangling and How Does It Work?

## Recap: Single vs Double Underscore
A **single underscore** (`_attr`) is a convention meaning "for internal use" — not enforced by Python. A **double underscore** (`__attr`) actively **prevents** direct access from outside the class.

    class Example:
        def __init__(self):
            self._internal = 'I can be accessed from outside the class, but should not'
            self.__private = 'You cannot access me directly from outside the class'

    obj = Example()

    print(obj._internal) # I can be accessed from outside the class, but should not
    print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'

## What Is Name Mangling?
Prefixing an attribute with `__` triggers **name mangling** — Python internally renames it by adding an underscore and the class name as a prefix: `__attribute` → `_ClassName__attribute`.

### Seeing It with `__dict__`
`__dict__` is a special attribute containing an object's attributes as a dictionary.

    class Example:
        def __init__(self, internal, private):
            self._internal = internal
            self.__private = private

    example1 = Example(
        'I can be accessed from outside the class, but should not',
        'I cannot be accessed directly from outside the class'
    )

    print(example1.__dict__)

Result:

    {
      '_internal': 'I can be accessed from outside the class, but should not',
      '_Example__private': 'I cannot be accessed directly from outside the class'
    }

`__private` is stored internally as `_Example__private` — meaning it **can** technically still be accessed from outside using that mangled name:

    class Example:
        def __init__(self, internal, private):
            self._internal = internal
            self.__private = private

    example1 = Example(
        'I can be accessed from outside the class, but should not',
        'I cannot be accessed directly from outside the class'
    )
    example2 = Example(
        'I should not be accessed from outside the class',
        'But I can be accessed from outside the class with name mangling'
    )

    print(example1._Example__private) # I cannot be accessed directly from outside the class
    print(example2._Example__private) # But I can be accessed from outside the class with name mangling

## Why Does Python Do This?
The main purpose: **prevent accidental attribute/method overriding during inheritance**.

    class Parent:
        def __init__(self):
            self.__data = 'Parent data'

    class Child(Parent):
        def __init__(self):
            super().__init__()
            self.__data = 'Child data'

    c = Child()
    print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

Thanks to name mangling, `Parent` and `Child` each get their own separate mangled attribute (`_Parent__data` and `_Child__data`) — so `Child` doesn't accidentally overwrite `Parent`'s data.

### Without Name Mangling (Single Underscore / No Prefix)
If neither class uses a double-underscore prefix, the child's attribute **overwrites** the parent's:

    class Parent:
       def __init__(self):
           self.data = 'Parent data'

    class Child(Parent):
       def __init__(self):
           super().__init__()
           self.data = 'Child data'

    c = Child()
    print(c.__dict__)  # {'data': 'Child data'}

## Which Should You Use?
- **Single underscore (`_`)** — if the attribute is only for internal use within the class.
- **Double underscore (`__`)** — if the class will be **inherited**, so the parent's attribute doesn't get accidentally overridden by a child class.