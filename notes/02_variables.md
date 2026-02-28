# Variables in Python

## What is a Variable?
- Variables are like **labeled boxes** for storing and referencing data of different types.  
- To declare a variable in Python, **assign a value** to an identifier using the `=` operator.  
- Unlike JavaScript (`let`, `const`) or C# (`char`), Python **does not require special keywords**.

### Example:
```python
name = 'John Doe'
age = 25
```
name holds 'John Doe' (a string)

age holds 25 (an integer)

# Naming Rules

- Variable names must start with a letter or underscore (_) — not a number.

- Variable names can only contain letters, numbers, and underscores.

- Variable names are case-sensitive (age, Age, AGE are all different).

- Variable names cannot be Python reserved keywords like if, class, or def.

### Example of invalid variable:
```python
variable_name = 5

# SyntaxError: invalid syntax
```

# Naming Conventions

-Use snake_case: lowercase words separated by underscores:

``` python 
my_variable_name = 'freeCodeCamp'
```

- Use descriptive names: clearly communicate the purpose of the variable:

``` python
user_age = 30
```

- Avoid single-letter variable names except in loops (i, j, k are fine in loops).

## Comments

Comments start with # and are ignored by Python.

# Single-line comment:

``` python
# This is a single-line comment
```

# Multi-line comment:

``` python
# This is a
# multi-line
# comment
```

- Use comments to explain your code or leave reminders, not to explain variable names — variable names should already be descriptive.

## Summary

- Variables store and reference data in Python.

- Follow naming rules and conventions to avoid syntax errors.

- Use comments wisely to explain code logic, not variable names.