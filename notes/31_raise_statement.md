# What Is the Raise Statement and How Does It Work?

The `raise` statement lets you **manually trigger exceptions**, giving you control over when and how errors are generated — useful for custom error conditions and enforcing program behavior.

## Basic Usage: Raising a Built-in Exception

    def check_age(age):
        if age < 0:
            raise ValueError('Age cannot be negative')
        return age

    try:
        check_age(-5)
    except ValueError as e:
        print(f'Error: {e}') # Error: Age cannot be negative

`raise` is the keyword that triggers the exception — here, a `ValueError` with a custom message.

## Re-raising the Current Exception
Calling `raise` with no arguments inside an `except` block re-raises the exception currently being handled:

    def process_data(data):
        try:
            result = int(data)
            return result * 2
        except ValueError:
            print('Logging: Invalid data received')
            raise  # Re-raises the same ValueError

    try:
        process_data('abc')
    except ValueError:
        print('Handled at higher level')

This lets you log or clean up while still letting the error propagate up the call stack.

## Custom Exceptions
You can define your own exception classes by inheriting from `Exception` (or a subclass):

    class InsufficientFundsError(Exception):
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

    def withdraw(balance, amount):
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    try:
        new_balance = withdraw(100, 150)
    except InsufficientFundsError as e:
        print(f'Transaction failed: {e}')

> Classes and inheritance are covered in more detail in future lessons — for now, this shows how to build exceptions with custom logic.

## Chaining Exceptions with `from`
The `from` keyword shows the relationship between two errors.

### Suppressing Context with `from None`

    def parse_config(filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                return int(data)
        except FileNotFoundError:
            raise ValueError('Configuration file is missing') from None
        except ValueError as e:
            raise ValueError('Invalid configuration format') from e

    config = parse_config('config.txt')

`raise ... from None` suppresses the original exception context:

    Traceback (most recent call last):
      File "main.py", line 12, in <module>
        config = parse_config('config.txt')
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "main.py", line 7, in parse_config
        raise ValueError('Configuration file is missing') from None
    ValueError: Configuration file is missing

### Preserving the Trail with `from e`
`raise ... from e` chains the new exception to the original, keeping the full error trail visible:

    Traceback (most recent call last):
      File "main.py", line 5, in parse_config
        return int(data)
               ^^^^^^^^^
    ValueError: invalid literal for int() with base 10: ''

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "main.py", line 12, in <module>
        config = parse_config('config.txt')
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "main.py", line 9, in parse_config
        raise ValueError('Invalid configuration format') from e
    ValueError: Invalid configuration format

## Conditional Raising with assert
`assert` is shorthand for raising an `AssertionError` when a condition is false:

    def calculate_square_root(number):
        assert number >= 0, 'Cannot calculate square root of negative number'
        return number ** 0.5

    try:
        result = calculate_square_root(-4)
    except AssertionError as e:
        print(f'Assertion failed: {e}')

---
`raise` is essential for building robust applications — enforcing business rules, validating input, and giving clear, meaningful error messages to make code more predictable and easier to debug.