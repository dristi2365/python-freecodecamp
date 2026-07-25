# Common List Methods in Python

Continuing from list basics (accessing elements, slicing), here are common methods used with lists: `append()`, `pop()`, `sort()`, and more.

## append()
Adds an item to the **end** of the list.

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]
```

If you append a list, the entire list gets nested as a single element:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, [6, 8, 10]]
```

## extend()
Similar to `append()`, but adds each individual element from another list (no nesting).

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, 6, 8, 10]
```

## insert()
Inserts an element at a specific index. Takes two arguments: `index` and `item`.

```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers)  # [1, 2, 2.5, 3, 4, 5]
```

## remove()
Removes an element by **value** (removes only the first occurrence).

```python
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers)  # [10, 20, 30, 40, 50]
```

```python
numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)

print(numbers)  # [10, 20, 30, 40, 50, 50]
```

## pop()
Removes an element at a specific **index** and returns it.

```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(1)  # Returns 2
```

If no index is given, removes and returns the **last** element.

```python
numbers = [1, 2, 3, 4, 5]
numbers.pop()  # Returns 5
```

## clear()
Empties the list completely.

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers)  # []
```

## sort()
Sorts the list **in place** (modifies the original list).

```python
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers)  # [1, 2, 19, 35, 41, 67]
```

## sorted()
A built-in **function** (not a list method) that works on any iterable and returns a **new** sorted list, leaving the original unchanged.

```python
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers)         # [19, 2, 35, 1, 67, 41]  (unchanged)
print(sorted_numbers)  # [1, 2, 19, 35, 41, 67]
```

> **Note:** An iterable is an object you can loop over, accessing one item at a time. Both `sort()` and `sorted()` also accept optional `key` and `reverse` parameters (covered in a future lesson on tuples).

## reverse()
Reverses the order of elements **in place**.

```python
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers)  # [1, 2, 3, 4, 5, 6]
```

## index()
Finds the **first index** where a given element occurs.

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java')  # 1
```

If the element isn't found, it raises a `ValueError`:

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""
```