# Data Types in Python

## What are Data Types?
- A **data type** describes the kind of value a variable holds (number, text, list, etc.).  
- Python is a **dynamically-typed language**, meaning you **don’t need to declare types explicitly**.  
- Python determines a variable’s type **based on the value assigned**.

### Example:
```python
name = 'John Doe'  # Python knows this is a string
age = 25           # Python knows this is an integer
```
- Contrast with statically-typed languages (C#, Java, C++):

# In Java/C# style (not Python)
``` python
string name = 'John Doe'
int age = 25
```

# Tip:

- Python detects type errors only during execution.

- Some languages catch type errors at compile-time.

## Common Data Types in Python
# Integer

- Whole numbers without decimals.

```python
my_integer_var = 10
print('Integer:', my_integer_var)  # Integer: 10
print(type(my_integer_var))        # <class 'int'>
```

# Float

- Numbers with decimals.

```python
my_float_var = 4.50
print('Float:', my_float_var)      # Float: 4.5
print(type(my_float_var))          # <class 'float'>
```

# String

- Sequence of characters inside single or double quotes.

```python
my_string_var = 'hello'
print('String:', my_string_var)    # String: hello
print(type(my_string_var))         # <class 'str'>
```

# Boolean

- True or False.

```python
my_boolean_var = True
print('Boolean:', my_boolean_var)  # Boolean: True
print(type(my_boolean_var))        # <class 'bool'>
```

# Set

- Unordered collection of unique elements.

```python
my_set_var = {7, 5, 8}
print('Set:', my_set_var)          # Set: {7, 5, 8}
print(type(my_set_var))            # <class 'set'>
```

# Dictionary

- Collection of key-value pairs.

```python
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)  # {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))           # <class 'dict'>
```

# Tuple

- Immutable ordered collection.

```python 
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var)       # Tuple: (7, 5, 8)
print(type(my_tuple_var))           # <class 'tuple'>
```

# Range

- Sequence of numbers (often used in loops).

```python
my_range_var = range(5)
print('Range:', my_range_var)       # Range: range(0, 5)
print(type(my_range_var))           # <class 'range'>
```

# List

- Ordered collection that supports different types.

```python
my_list = [22, 'Hello world', 3.14, True]
print('List:', my_list)             # [22, 'Hello world', 3.14, True]
print(type(my_list))                # <class 'list'>
```

#None

- Special value representing the absence of a value.

```python
my_none_var = None
print('None:', my_none_var)         # None: None
print(type(my_none_var))            # <class 'NoneType'>
```
# Checking Data Types
- Using type()
```python
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1))  # <class 'str'>
print(type(my_var_2))  # <class 'int'>
Using isinstance()
isinstance('Hello world', str)   # True
isinstance(True, bool)           # True
isinstance(42, int)              # True
isinstance('John Doe', int)      # False
```

## Summary

- Python is dynamically typed — types are determined at runtime.

- Common data types: int, float, str, bool, set, dict, tuple, range, list, None.

- Use type() to check a variable’s type and isinstance() to test if it matches a specific type.