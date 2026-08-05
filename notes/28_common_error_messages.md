# What Are Some Common Error Messages in Python?

Understanding error messages is key to debugging quickly. They tell you exactly what went wrong — if you know how to read them.

Common Python errors: `SyntaxError`, `NameError`, `TypeError`, `IndexError`, `AttributeError`. These occur when Python doesn't understand your code, or your logic doesn't match the data you're working with.

## SyntaxError
Raised when code doesn't follow proper syntax rules.

    print("Hello, world!"
    # SyntaxError: unexpected EOF while parsing

This line is missing a closing parenthesis.

## NameError
Raised when Python can't find a variable by that name.

    print(name)
    # NameError: name 'name' is not defined

Here, `name` is being printed before it's ever defined.

## TypeError
Raised when you try to perform an operation on incompatible data types.

    5 + "5"
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

You can't add an integer and a string together.

## IndexError
Raised when you try to access an index that doesn't exist in a list — i.e., going out of bounds.

    my_list = [1, 2, 3]
    print(my_list[5])
    # IndexError: list index out of range

## AttributeError
Raised when you try to use a method or property that doesn't exist for that data type.

    num = 42
    num.append(5)
    # AttributeError: 'int' object has no attribute 'append'

The `int` object has no `append()` method — that's a list method.

---
Recognizing common error messages helps you fix problems faster. Instead of guessing, read the error message carefully — it usually tells you exactly what went wrong and where to look.