# Common Methods for Tuples

## count()
Returns how many times an item appears in a tuple.

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust')  # 2
```

If the item isn't present, returns `0`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript')  # 0
```

If no argument is passed, Python raises a `TypeError`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""
```

## index()
Finds the index of a given item in a tuple.

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java')  # 1
```

If the item isn't found, raises a `ValueError`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: tuple.index(x): x not in tuple
"""
```

### Optional start and stop Arguments
You can pass a `start` index to control where the search begins:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3)  # 5
```
Since `'Python'` appears at both index 2 and 5, starting the search at index 3 skips the first match and returns 5 instead.

You can also add a `stop` index:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5)  # 2
```
This searches from index 2 up to, but not including, index 5.

## sorted()
Works on any iterable, including tuples. Always returns a **new list** — it does not modify the original.

```python
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers)  # [2, 3, 7, 13, 18, 45, 67, 78]
```

> This differs from the `sort()` method, which sorts a list **in place** and returns `None`.

### Custom Sorting with `key`
Sort by a custom criterion, e.g. string length:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

### Reverse Order with `reverse`

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

---
Tuples are a common data type in Python — knowing their methods and functions helps write more efficient code.