# String Concatenation and String Interpolation in Python

## What is String Concatenation?
- **String concatenation** means combining multiple strings into one.
- In Python, this is commonly done using the **plus (`+`) operator**.

### Example:
```python
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)  # Hello World
```

## Concatenating Strings and Numbers

- You cannot concatenate strings and numbers directly in Python.

- Doing so results in a TypeError.

```python
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age)  # TypeError
```

## Converting Numbers to Strings

- Use the built-in str() function to convert numbers into strings.

```python
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age)  # John Doe26
```

## Augmented Assignment for Concatenation (+=)

- The += operator performs concatenation and assignment in one step.

```python
name = 'John Doe'
age = 26

name_and_age = name
name_and_age += str(age)

print(name_and_age)  # John Doe26
```

## What is String Interpolation?

- String interpolation is the process of inserting variables or expressions into a string.

- Python supports interpolation using f-strings (formatted string literals).

## Using f-Strings

- f-strings start with f before the quotation marks.

- Variables or expressions are placed inside {}.

```python
name = 'John Doe'
age = 26

name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age)
```

## f-Strings with Expressions

- You can also include expressions inside f-strings.

```python
num1 = 5
num2 = 10

print(f'The sum of {num1} and {num2} is {num1 + num2}')
```

- f-strings automatically convert non-string values to strings.

## Summary

- Use + to concatenate strings.

- Convert non-strings using str() when concatenating.

- Use += for concise concatenation.

- f-strings provide a clean and readable way to perform string interpolation.