# What Are Sets, and How Do They Work?

Sets are one of Python's built-in data structures. A core characteristic: **they don't store duplicate values** — adding a duplicate keeps only one copy.

## Key Characteristics
- **Mutable** — can be changed after creation
- **Unordered** — no indices or keys to access elements
- Can only contain **immutable** data types (numbers, strings, tuples)
- Support mathematical set operations: union, intersection, difference, symmetric difference

## Defining a Set
Elements go inside curly braces, separated by commas:

    my_set = {1, 2, 3, 4, 5}

### Empty Set Quirk
Empty curly braces `{}` create a **dictionary**, not a set. Use `set()` instead:

    set() # Set
    {}    # Dictionary

## Adding Elements

    my_set.add(6)

Result: `{1, 2, 3, 4, 5, 6}`

If the element already exists, nothing changes:

    my_set.add(5)
    # Still {1, 2, 3, 4, 5, 6}

## Removing Elements
Two options: `.remove()` and `.discard()`.

- `.remove()` raises a `KeyError` if the element isn't found
- `.discard()` does **not** raise an error

    my_set.remove(4)
    my_set.discard(4)

### Clearing a Set

    my_set.clear()

## Set Comparison Methods

### .issubset() and .issuperset()

    my_set = {1, 2, 3, 4, 5}
    your_set = {2, 3, 4, 6}

    print(your_set.issubset(my_set))    # False
    print(my_set.issuperset(your_set))  # False

### .isdisjoint()
Checks if two sets share **no** elements in common:

    print(my_set.isdisjoint(your_set))  # False (they share 2, 3, 4)

## Set Operators

### Union `|`
All elements from both sets:

    my_set | your_set  # {1, 2, 3, 4, 5, 6}

### Intersection `&`
Only elements common to both sets:

    my_set & your_set  # {2, 3, 4}

### Difference `-`
Elements in the first set but not the other:

    my_set - your_set  # {1, 5}

### Symmetric Difference `^`
Elements in either set, but not both:

    my_set ^ your_set  # {1, 5, 6}

## Compound Assignment Operators
Each operator has a compound form that updates the first set directly:

    |= &= -= ^=

Example:

    my_set -= your_set
    print(my_set)  # {1, 5}

## Membership Check with in

    print(5 in my_set)  # True or False

---
Sets are helpful when you don't need a specific order and only need to store **unique** values.