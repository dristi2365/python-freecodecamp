# What Are Tuples and How Do They Work?

A tuple is a Python data type used to create an **ordered sequence of values**. Tuples can contain a mixed set of data types:

```python
developer = ('Alice', 34, 'Rust Developer')
```

## Tuples vs Lists: Immutability
Tuples are similar to lists, but while lists are **mutable**, tuples are **immutable** — elements cannot be changed once created.

Trying to update a tuple raises a `TypeError`:

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""
```

## Accessing Elements
Use bracket notation with the index number:

```python
developer = ('Alice', 34, 'Rust Developer')
developer[1]  # 34
```

### Negative Indexing
Access elements from the end using negative indices:

```python
numbers = (1, 2, 3, 4, 5)
numbers[-2]  # 4
```

### Out-of-Range Index
Passing an index that exceeds or equals the tuple's length raises an `IndexError`:

```python
numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
"""
```

## Creating Tuples with the tuple() Constructor
You can create a tuple from an iterable (string, list, or another tuple):

```python
developer = 'Jessica'
tuple(developer)  # ('J', 'e', 's', 's', 'i', 'c', 'a')
```

## Checking Membership with `in`

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages        # True
'JavaScript' in programming_languages  # False
```

## Unpacking Tuples
Just like lists, tuples can be unpacked into variables:

```python
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name)  # 'Alice'
print(age)   # 34
print(job)   # 'Rust Developer'
```

### Collecting Remaining Elements with `*`

```python
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']
```
Here, `name` is `'Alice'`, and `rest` is a **list** containing the remaining elements.

## Slicing Tuples
Just like with lists, you can use the slice operator to extract a portion of a tuple:

```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3]  # ('pie', 'cookies')
```

> The first number is the starting index, the second is the ending index (the item at the ending index is **not** included).

## Deleting Items (Not Possible)
Since tuples are immutable, you can't delete an item — this raises a `TypeError`:

```python
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
"""
```

## When to Use a Tuple vs a List
- **Use a list** if you need a dynamic collection where you can add, remove, or update elements.
- **Use a tuple** if you're working with a fixed, immutable collection of data.

*Next lesson: common methods for working with tuples.*