# Lists in Python
## What Are Lists?

A list in Python is an ordered sequence of elements. Lists can contain different types of data such as strings, numbers, or even other lists.

Lists are:

- Ordered

- Mutable (can be changed)

- Zero-indexed (first element starts at index 0)

### Example
```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

## Accessing Elements in a List

You can access list elements using their index.
```python
cities = ['Los Angeles', 'London', 'Tokyo']

cities[0]  # 'Los Angeles'
cities[1]  # 'London'
cities[2]  # 'Tokyo'
```

## Negative Indexing

- Negative indexing starts from the end of the list.
```python
cities = ['Los Angeles', 'London', 'Tokyo']

cities[-1]  # 'Tokyo'
cities[-2]  # 'London'
```
- -1 always refers to the last element.

## Creating Lists with list()

- Another way to create a list is using the list constructor.
```python
developer = 'Jessica'

list(developer)
```
- Output: ['J', 'e', 's', 's', 'i', 'c', 'a']

- This works because strings are iterables, meaning they can be looped through one element at a time.

## Getting the Length of a List

- Use the len() function to count the number of elements.
```python
numbers = [1, 2, 3, 4, 5]

len(numbers)  # 5
```

## Updating List Elements

- Lists are mutable, so you can change values.
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

programming_languages[0] = 'JavaScript'

print(programming_languages)
```
- Output: ['JavaScript', 'Java', 'C++', 'Rust']

## IndexError (Out of Range)

- If you try to access or update an index that doesn't exist, Python raises an error.
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

programming_languages[10] = 'JavaScript'
```
- Error: IndexError: list assignment index out of range

## Removing Elements from a List

- You can remove an element using the del keyword.
```python
developer = ['Jane Doe', 23, 'Python Developer']

del developer[1]

print(developer)
```
- Output: ['Jane Doe', 'Python Developer']

## Checking if an Element Exists

- Use the in keyword to check if a value exists in a list.
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages       # True
'JavaScript' in programming_languages # False
```

## Nested Lists

- Lists can contain other lists.
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```
### Access the nested list:
```python
developer[2]
```
- Output: ['Python', 'Rust', 'C++']

### Access an element inside the nested list:
```python
developer[2][1]
```
- Output: 'Rust'

## Unpacking List Values

- You can assign list elements to variables.
```python
developer = ['Alice', 34, 'Rust Developer']

name, age, job = developer

# Now:

name = 'Alice'
age = 34
job = 'Rust Developer'

# Collecting Remaining Elements with *

The * operator can collect remaining values.

developer = ['Alice', 34, 'Rust Developer']

name, *rest = developer
```
- Output:

name = 'Alice'
rest = [34, 'Rust Developer']
Slice Operator

- The slice operator (:) allows you to access a portion of a list.
```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']

desserts[1:4]
```
- Output: ['Cookies', 'Ice Cream', 'Pie']

- Syntax:
```python
list[start:end]
```
- start is included

- end is excluded

## Step Slicing

- You can specify a step interval to skip elements.
```python
numbers = [1, 2, 3, 4, 5, 6]

numbers[1::2]
```
- Output: [2, 4, 6]

- Explanation:

1. Start at index 1

2. Go to the end

3. Step by 2

## Summary

- Lists are one of the most commonly used data structures in Python.

- They allow you to:

- Store multiple values

- Access elements using indexing

- Modify elements

- Remove elements

- Check for membership

- Work with nested data

- Extract portions using slicing

- Unpack values into variables