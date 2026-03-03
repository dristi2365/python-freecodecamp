# Conditional Statements and Logical Operators in Python

Conditional statements allow you to control the flow of your program based on whether conditions evaluate to `True` or `False`.

They are essential for writing decision-making logic in Python.

---

## Comparison Operators

Comparison operators compare two values and return a Boolean (`True` or `False`).

| Operator | Name                     | Description |
|----------|--------------------------|-------------|
| ==       | Equal                    | Checks if two values are equal |
| !=       | Not equal                | Checks if two values are not equal |
| >        | Greater than             | Checks if left value is greater than right value |
| <        | Less than                | Checks if left value is less than right value |
| >=       | Greater than or equal    | Checks if left value is greater than or equal to right value |
| <=       | Less than or equal       | Checks if left value is less than or equal to right value |

### Examples

```python
print(3 > 4)   # False
print(3 < 4)   # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
```

## The if Statement

The if statement runs code only when a condition is True.

Syntax
```python
if condition:
    # Code block
 ```
### Example
```python
age = 18

if age >= 18:
    print("You are an adult")
```
- Important: Indentation

- Python uses indentation to define code blocks.

- Incorrect indentation will raise an error:
```python
age = 18

if age >= 18:
print("You are an adult")  # IndentationError
```

- The Python style guide recommends four spaces for indentation.

## The else Statement

The else block runs when the if condition is False.

Syntax
```python
if condition:
    # Code if True
else:
    # Code if False
```
### Example
```python
age = 12

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")
```

## The elif Statement

Use elif when checking multiple conditions.

Syntax
```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition1 is False and condition2 is True
else:
    # Code if all conditions are False
```
### Example
```python
age = 12

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

- You can use multiple elif blocks:
```python
age = 2

if age >= 65:
    print("You are a senior citizen")
elif age >= 30:
    print("You are an adult in your prime")
elif age >= 18:
    print("You are a young adult")
elif age >= 13:
    print("You are a teenager")
elif age >= 3:
    print("You are a young child")
else:
    print("You are a toddler or an infant")
```

## Logical Operators

- Logical operators allow you to combine multiple conditions.

- Operator	Description
1. and	True if both conditions are True
2. or	True if at least one condition is True
3. not	Reverses the boolean value

### Examples
```python
age = 21
is_member = True

if age >= 18 and is_member:
    print("Access granted")

if age < 18 or not is_member:
    print("Access restricted")
```

## Key Takeaways

- Comparison operators return Boolean values.

- if runs code when a condition is True.

- else runs when the condition is False.

- elif allows checking multiple conditions.

- Indentation defines code blocks in Python.

- Logical operators (and, or, not) combine conditions.

- Conditional statements are the foundation of writing dynamic and responsive programs in Python.