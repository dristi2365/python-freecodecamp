# How Do Loops Work?

Loops repeat a block of code.

## for Loops
Iterate through a list:

    programming_languages = ['Rust', 'Java', 'Python', 'C++']

    for language in programming_languages:
        print(language)

Output:

    Rust
    Java
    Python
    C++

> Note: `print(language)` must be indented inside the loop. Without indentation, you'll get an `IndentationError`:

    """
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    IndentationError: expected an indented block after 'for' statement on line 3
    """

### Looping Through a String

    for char in 'code':
        print(char)

Output:

    c
    o
    d
    e

### Nested for Loops

    categories = ['Fruit', 'Vegetable']
    foods = ['Apple', 'Carrot', 'Banana']

    for category in categories:
        for food in foods:
            print(category, food)

The outer loop iterates through `categories`; for each category, the inner loop iterates through all of `foods`.

Output:

    Fruit Apple
    Fruit Carrot
    Fruit Banana
    Vegetable Apple
    Vegetable Carrot
    Vegetable Banana

## while Loops
Repeats a block of code **until** a condition is `False`.

    secret_number = 3
    guess = 0

    while guess != secret_number:
        guess = int(input('Guess the number (1-5): '))
        if guess != secret_number:
            print('Wrong! Try again.')

    print('You got it!')

Example run:

    Guess the number (1-5): 2
    Wrong! Try again.
    Guess the number (1-5): 1
    Wrong! Try again.
    Guess the number (1-5): 3
    You got it!

## break Statement
Stops the execution of a loop entirely.

    developer_names = ['Jess', 'Naomi', 'Tom']

    for developer in developer_names:
        if developer == 'Naomi':
            break
        print(developer)

Only `Jess` is printed — the loop stops once `'Naomi'` is reached.

## continue Statement
Skips the current iteration and moves to the next.

    developer_names = ['Jess', 'Naomi', 'Tom']

    for developer in developer_names:
        if developer == 'Naomi':
            continue
        print(developer)

Both `Jess` and `Tom` are printed — `'Naomi'` is skipped, but the loop continues.

## Loop else Clause
Both `for` and `while` loops can have an `else` clause, which runs only if the loop completes **without** hitting a `break`.

    words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

    for word in words:
        for letter in word:
            if letter.lower() in 'aeiou':
                print(f"'{word}' contains the vowel '{letter}'")
                break
        else:
            print(f"'{word}' has no vowels")

For each word, the inner loop checks each letter. If a vowel is found, it prints the vowel and `break`s (skipping the inner `else`). If no vowel is found, the inner loop completes normally and its `else` block runs.

Output:

    'sky' has no vowels
    'apple' contains the vowel 'a'
    'rhythm' has no vowels
    'fly' has no vowels
    'orange' contains the vowel 'o'

---
Loops are very common in Python — getting comfortable with them is important. Next up: the `enumerate()` and `range()` functions in loops.