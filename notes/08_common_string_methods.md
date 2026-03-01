# Common String Methods in Python

Python provides many built-in **string methods** that make working with text easy and efficient.  
These methods **do not modify the original string** — they return a **new string**.

---

## `upper()`
Returns a new string with all characters converted to uppercase.

```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

## `lower()`

Returns a new string with all characters converted to lowercase.

```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```
## `strip()`

- Removes leading and trailing whitespace (or specified characters).

```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # hello world
replace(old, new)
```

- Replaces all occurrences of old with new.

```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
split(separator)
```

- Splits a string into a list.
- If no separator is provided, it splits on whitespace.

```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
join(iterable)
```

- Joins elements of an iterable into a string using a separator.

```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
startswith(prefix)
``` 
- Returns True if the string starts with the given prefix.

```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
endswith(suffix)
```

- Returns True if the string ends with the given suffix.

```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
find(substring)
```

- Returns the index of the first occurrence of a substring.
- Returns -1 if not found.

```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
count(substring)
```

- Returns how many times a substring appears in a string.

```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
capitalize()
```

- Capitalizes the first character and lowercases the rest.

```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
isupper()
```

- Returns True if all letters are uppercase.

```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
islower()
```
- Returns True if all letters are lowercase.

```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
title()
```

- Capitalizes the first letter of each word.

```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

## Summary

- String methods return new strings (strings are immutable).

- Methods like upper(), lower(), and title() change case.

- Methods like split() and join() help manipulate text structure.

- Methods like find() and count() help search strings.