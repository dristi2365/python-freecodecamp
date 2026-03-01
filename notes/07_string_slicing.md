# String Slicing in Python

## Indexing Recap
Each character in a string has an **index** (starting from 0) and can be accessed using square brackets.

```python
my_str = "Hello world"

print(my_str[0])   # H
print(my_str[6])   # w
print(my_str[-1])  # d
```

## What is String Slicing?

- String slicing allows you to extract a portion of a string.

- Basic syntax:

```python
string[start:stop]
```

## Slicing with Start and Stop

- Extract characters from index start up to but not including stop.

```python
my_str = 'Hello world'
print(my_str[1:4])  # ell
```

- 📌 The stop index is non-inclusive.

```python
#Omitting Start or Stop
#Omitting the start index

#Defaults to index 0.

my_str = 'Hello world'
print(my_str[:7])  # Hello w

# Omitting the stop index

# Defaults to the end of the string.

my_str = 'Hello world'
print(my_str[8:])  # rld
```

- Slicing Does Not Modify the Original String

- Strings are immutable, so slicing creates a new string.

```python
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)      # Hello world
```

## Slicing the Entire String

- Omitting both start and stop extracts the full string.

```python
my_str = 'Hello world'
print(my_str[:])  # Hello world
```

## Using the Step Parameter

- The optional step parameter controls how many indices to skip.

Syntax:
string[start:stop:step]

### Example:
```python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```

## Reversing a String with Slicing

- You can reverse a string by setting step to -1.

```python
my_str = 'Hello world'
print(my_str[::-1])  # dlrow olleH
```

## Summary

- String slicing extracts parts of a string using indices.

- The stop index is not included.

- You can omit start, stop, or both.

- The step parameter controls how characters are selected.

- Strings are immutable, so slicing does not change the original string.