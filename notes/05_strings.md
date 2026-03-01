# Strings and String Immutability in Python

## What is a String?
- A **string** is a sequence of characters surrounded by **single (`'`) or double (`"`) quotation marks**.
- In Python, single and double quotes are treated the same.

### Examples:
```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

## Multi-line Strings

- You can create multi-line strings using triple quotes (''' or """).

```python
my_str_3 = """Multiline
string"""

my_str_4 = '''Another
multiline
string'''
```

## Strings with Quotes Inside

- If your string contains quotes, you have two options:

1. Use the opposite type of quotes
```python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```
2. Escape quotes using a backslash (\)
```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```
## Checking Characters in a String (in operator)

- Python provides the in operator to check if a string contains certain characters.

- It returns a boolean (True or False).

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)     # False
print('e' in my_str)      # True
print('f' in my_str)      # False
```

## String Length

- Use the built-in len() function to get the length of a string.

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

## String Indexing

- Each character in a string has an index.

- Indexing is zero-based (starts from 0).

```python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

## Negative Indexing

- Negative indexes start from the end of the string.

```python
my_str = 'Hello world'

print(my_str[-1])  # d
print(my_str[-2])  # l
```

## String Immutability

- In Python, strings are immutable, meaning they cannot be modified after creation.

- You can reassign a variable to a new string, but you cannot change characters directly.

```python
#Reassignment (Allowed)
greeting = 'hi'
greeting = 'hello'
print(greeting)  # hello

#Direct Modification (Not Allowed)
greeting = 'hi'
greeting[0] = 'H'  # TypeError: 'str' object does not support item assignment
```

## Other Immutable Data Types

- Some other immutable data types in Python include:

1. int

2. float

3. bool

4. tuple

5. range

## Summary

- Strings are sequences of characters in quotes.

- Python supports multi-line strings and escaped characters.

- Strings support indexing and length checking.

- Strings are immutable — they cannot be changed after creation.