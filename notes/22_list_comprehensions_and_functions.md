# What Are List Comprehensions and What Are Some Useful Functions to Work With Lists?

## The Long Way: Loop + Condition
A common pattern for building a filtered list:

    even_numbers = []

    for num in range(21):
        if num % 2 == 0:
            even_numbers.append(num)

    print(even_numbers)

This creates an empty list, loops through numbers `0` to `20`, checks if each is evenly divisible by `2`, and appends it if so.

## List Comprehensions
A more concise way to build a list: combine a loop and condition directly inside square brackets.

    even_numbers = [num for num in range(21) if num % 2 == 0]
    print(even_numbers)

Same result, one line — no separate loop and conditional block needed.

### List Comprehension with if/else
You can also use an if/else inside a comprehension to produce different values depending on a condition:

    numbers = [1, 2, 3, 4, 5]
    result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
    print(result)

This creates a list of tuples labeling each number as `'Even'` or `'Odd'`.

Output:

    [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

## filter()
Selects elements from an iterable that meet a condition. Takes a **function** and an **iterable** as arguments.

    words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

    def is_long_word(word):
        return len(word) > 4

    long_words = list(filter(is_long_word, words))
    print(long_words)  # ['mountain', 'river', 'cloud']

Here, `is_long_word` checks if a word's length is greater than 4, and `filter()` keeps only the words that pass.

## map()
Applies a function to **every element** of an iterable. Also takes a function and an iterable as arguments.

    celsius = [0, 10, 20, 30, 40]

    def to_fahrenheit(temp):
        return (temp * 9/5) + 32

    fahrenheit = list(map(to_fahrenheit, celsius))
    print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

## sum()
Returns the sum of an iterable (list, tuple, etc.).

    numbers = [5, 10, 15, 20]
    total = sum(numbers)
    print(total)  # 50

### Optional start Argument
Sets an initial value for the summation. Can be passed positionally or as a keyword argument:

    numbers = [5, 10, 15, 20]
    total = sum(numbers, 10)  # positional argument
    print(total)  # 60

    numbers = [5, 10, 15, 20]
    total = sum(numbers, start=10)  # keyword argument
    print(total)  # 60

Both produce the same result — the keyword version is just more explicit.

---
List comprehensions and functions like `map()`, `filter()`, and `sum()` can feel confusing at first, but get easier with practice.