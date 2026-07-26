# What Are Ranges and How Can You Use Them in a Loop?

The `range()` function generates a sequence of integers.

## Basic Syntax

    range(start, stop, step)

The **`stop`** argument is the only required one — it's an integer marking the end point (non-inclusive) for the sequence.

    for num in range(3):
        print(num)

This generates numbers `0` to `2`. `3` itself is **not included** since `stop` is non-inclusive.

## The start Argument
Defaults to `0` if not specified. You can set a different starting point:

    for num in range(1, 5):
        print(num)

This generates `1, 2, 3, 4`.

## The step Argument
By default, the sequence increments by `1`. Use `step` to change that:

    for num in range(2, 11, 2):
        print(num)

This generates even numbers: `2, 4, 6, 8, 10`.

## Required Argument
Calling `range()` with no arguments raises a `TypeError`:

    ERROR!
    Traceback (most recent call last):
      File "<main.py>", line 1, in <module>
    TypeError: range expected at least 1 argument, got 0

## Integers Only — No Floats
`range()` only accepts integers, not floats (numbers with decimal points like `3.4`):

    ERROR!
    Traceback (most recent call last):
      File "<main.py>", line 1, in <module>
    TypeError: 'float' object cannot be interpreted as an integer

## Decrementing Sequences
Use a negative `step` to count down:

    for num in range(40, 0, -10):
        print(num)

This prints `40, 30, 20, 10`.

## Creating a List from range()
Combine `range()` with the `list` constructor to generate a list of integers:

    numbers = list(range(2, 11, 2))
    print(numbers)  # [2, 4, 6, 8, 10]

---
`range()` is a handy way to generate sequences of integers — you'll likely use it a lot in Python programs.