# Augmented Assignments in Python

## What is an Augmented Assignment?
An **augmented assignment** combines a binary operation with assignment in a single step.

### Basic syntax:
```python
variable <operator>= value
```

This is a shorter and cleaner version of:
```python
variable = variable <operator> value
```
Example: Addition Assignment (+=)
```python
my_var = 10
my_var += 5

print(my_var)  # 15
```
### Equivalent without augmented assignment:

```python
my_var = 10
my_var = my_var + 5

print(my_var)  # 15
```

## Why use augmented assignments?

- Cleaner and more readable

- Avoids repeating variable names

- Reduces chances of typos

## Common Augmented Assignment Operators
### Subtraction (-=)
```python
count = 14
count -= 3

print(count)  # 11
```

### Multiplication (*=)
```python
product = 65
product *= 7

print(product)  # 455
```

### Division (/=)
```python
price = 100
price /= 4

print(price)  # 25.0
```

### Floor Division (//=)
```python
total_pages = 23
total_pages //= 5

print(total_pages)  # 4
```

### Modulus (%=)
```python
bits = 35
bits %= 2

print(bits)  # 1
```

### Exponentiation (**=)
```python
power = 2
power **= 3

print(power)  # 8
```

## Augmented Assignments with Strings
### String Concatenation (+=)
```python
greet = 'Hello'
greet += ' World'

print(greet)  # Hello World
```

### String Repetition (*=)
```python
greet = 'Hello'
greet *= 3

print(greet)  # HelloHelloHello
```

### Invalid String Operations

Some augmented assignments do not work with strings and raise a TypeError.

```python
greet = 'Hello'
greet -= ' World'  # TypeError
greet = 'Hello'
greet /= 'World'  # TypeError
```

### Increment and Decrement Operators in Python

- Python does not support ++ or -- operators.

- Instead of:
```python
x++
```
- You should write:
```python
x += 1
```
- Why ++ doesn’t work
```python
my_var = 5

print(+my_var)    # 5
print(++my_var)   # 5
print(+++my_var)  # 5
```

- This applies the unary plus operator multiple times — it does not increment the value.

Correct way:
```python
my_var += 1
print(my_var)  # 6
```

## Summary

- Augmented assignments combine an operation and assignment.

- They improve readability and reduce repetition.

- Most arithmetic operators support augmented assignment.

- Strings support += and *=, but not others.

- Python does not use ++ or --; use += 1 instead.