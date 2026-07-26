# What Are the Enumerate and Zip Functions and How Do They Work?

## The Problem: Tracking Index Manually
A `for` loop repeats a block of code for each item in an iterable:

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

    for language in languages:
        print(language)

To track the index of each element, one option is manually creating and incrementing an `index` variable:

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

    index = 0

    for language in languages:
        print(f'Index {index} and language {language}')
        index += 1

## enumerate()
A cleaner way to track index: `enumerate()` keeps track of the index for an iterable and returns an **enumerate object**.

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

    list(enumerate(languages))
    # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

Each entry is a tuple of `(count, value)`.

### Using enumerate() in a Loop

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

    for index, language in enumerate(languages):
        print(f'Index {index} and language {language}')

Output:

    Index 0 and language Spanish
    Index 1 and language English
    Index 2 and language Russian
    Index 3 and language Chinese

This removes the need for manually creating and updating an `index` variable.

### Optional start Argument
Sets the starting value for the count (default is `0`):

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

    for index, language in enumerate(languages, 1):
        print(f'Index {index} and language {language}')

Output:

    Index 1 and language Spanish
    Index 2 and language English
    Index 3 and language Russian
    Index 4 and language Chinese

## zip()
Used to iterate over **multiple iterables in parallel**. It combines lists into pairs of elements and returns an iterator of tuples.

    developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
    ids = [1, 2, 3, 4]

    list(zip(developers, ids))
    # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

### Using zip() in a Loop

    developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
    ids = [1, 2, 3, 4]

    for name, dev_id in zip(developers, ids):
        print(f'Name: {name}')
        print(f'ID: {dev_id}')

`zip()` combines the two lists into pairs of elements, and the `for` loop unpacks each tuple into `name` and `dev_id`.

Output:

    Name: Naomi
    ID: 1
    Name: Dario
    ID: 2
    Name: Jessica
    ID: 3
    Name: Tom
    ID: 4

---
`enumerate()` and `zip()` are powerful functions that, combined with loops, make your code much more concise.