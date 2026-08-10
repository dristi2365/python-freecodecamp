# How Does Exception Handling Work?

Exception handling is the process of catching and managing errors during program execution, so code doesn't crash unexpectedly. Python provides `try`, `except`, `else`, and `finally` blocks for this.

## Basic try/except

    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")

- **try**: the block of code where an error might occur
- **except**: runs if an error of the specified type is raised inside `try`

Here, dividing by zero raises a `ZeroDivisionError`, which gets caught and handled.

## Adding else and finally

    try:
        x = 10 / 2
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print('Division successful:', x)
    finally:
        print('This block always runs.')

- **else**: runs if **no** exception is raised in the `try` block
- **finally**: always runs, regardless of whether an exception occurred — useful for clean-up tasks like closing files or releasing resources

## Catching Multiple Exceptions (Separate Blocks)
Use separate `except` clauses for different exception types:

    try:
        number = int('abc')
        result = 10 / number
    except ValueError:
        print('That was not a valid number.')
    except ZeroDivisionError:
        print("Can't divide by zero.")

This makes error responses more specific and useful.

## Accessing the Exception Object
Use `as` to alias the exception object (commonly `e`), giving access to the actual error message:

    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f'Error occurred: {e}')

## Catching Multiple Exceptions in One Clause
Specify exceptions as a tuple to catch several types with a single `except`:

    try:
        number = int(input('Enter a number: '))
        result = 10 / number
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error occurred: {e}')

---
Exception handling lets programs recover from errors gracefully. Using `try`, `except`, `else`, and `finally` helps you anticipate issues and build more resilient applications.