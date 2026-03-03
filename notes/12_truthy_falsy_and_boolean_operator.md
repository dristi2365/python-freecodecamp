# Truthy and Falsy Values, Boolean Operators, and Short-Circuiting in Python

## Truthy and Falsy Values

In Python, every value has an inherent boolean meaning.

- **Truthy values** evaluate to `True`
- **Falsy values** evaluate to `False`

### Common Falsy Values

- `None`
- `False`
- `0`
- `0.0`
- `""` (empty string)
- `[]`, `{}`, `()` (empty collections)

All other values (non-zero numbers, non-empty strings, etc.) are truthy.

---

## Using `bool()` to Check Truthiness

You can explicitly convert values using `bool()`:

```python
print(bool(False))  # False
print(bool(0))      # False
print(bool(''))     # False

print(bool(True))   # True
print(bool(1))      # True
print(bool('Hello'))  # True
```

## Boolean (Logical) Operators

Python has three logical operators:

- Operator	Description
1. `and` `True` if both operands are truthy
2. `or`	`True` if at least one operand is truthy
3. `not` Reverses the boolean value

### The and Operator

- Returns the first operand if it is falsy

- Otherwise returns the second operand

- Both must be truthy for a truthy result

Example
```python
is_citizen = True
age = 25

print(is_citizen and age)  # 25
```

Why 25?

is_citizen is True. So Python evaluates and returns the second value

### Using and in Conditionals
```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

### The or Operator

- Returns the first operand if it is truthy

- Otherwise returns the second operand

- Only one operand needs to be truthy

Example
```python
age = 19
is_employed = False

print(age or is_employed)  # 19
```

- Since age is truthy, it is returned immediately.

### Using or in Conditionals
```python
age = 19
is_student = True

if age < 18 or is_student:
    print("You are eligible for a student discount")
else:
    print("You are not eligible for a student discount")
```

### The not Operator

- Takes one operand

- Always returns True or False

- Reverses truthiness

Examples
```python
print(not '')        # True
print(not 'Hello')   # False
print(not 0)         # True
print(not 1)         # False
print(not False)     # True
print(not True)      # False
```

### Using not in Conditionals
```python
is_admin = False

if not is_admin:
    print("Access denied for non-administrators.")
else:
    print("Welcome, Administrator!")
```

### Short-Circuiting

- Both and and or use short-circuit evaluation.

- This means:

1. Python evaluates expressions from left to right

2. It stops as soon as the final result is determined

Example of and Short-Circuit
```python
False and print("Hello")
```
This prints nothing because:

- `False` is already falsy

- Python stops immediately

Example of or Short-Circuit
```python
True or print("Hello")
```
This prints nothing because:

- `True` is already truthy

- Python stops immediately

## Key Takeaways

- Every value in Python has a truth value.

- Falsy values include 0, "", None, and False.

- `and` returns the first falsy value or the last truthy value.

- `or` returns the first truthy value.

- `not` always returns a boolean.

- Short-circuiting improves performance and avoids unnecessary evaluation.

- Understanding truthy and falsy values and Boolean operators allows you to write cleaner, more efficient conditional logic.