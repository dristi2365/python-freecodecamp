# How Do Functions Work in Python?

Functions are reusable pieces of code that run when you call them. They help organize programs and avoid repeating code.

Python comes with many built-in functions that make programming easier.

---

## Built-in Functions

### `print()`

Displays output to the terminal.

```python
print("Hello World")
input()
```
Prompts the user for input.
```python
name = input('What is your name?')  # User types "Kolade"
print('Hello', name)  # Output: Hello Kolade
```

### int()

Converts values into integers.
```python
print(int(3.14))   # 3
print(int('42'))   # 42
print(int(True))   # 1
print(int(False))  # 0
```
### Creating Custom Functions

You can write your own functions using the def keyword.

Syntax
```python
def function_name():
    # function body
```
The indented code inside the function is called the function body.

Example: Simple Function
```python
def hello():
    print('Hello World')
```
To run it, call the function:
```python
hello()  # Hello World
```
Python uses indentation to define code blocks. Everything indented under def belongs to that function.

## Parameters and Arguments
### Parameters

Parameters are placeholder variables inside the function definition.
```python
def calculate_sum(a, b):
    print(a + b)
```
Here, a and b are parameters.

### Arguments

- Arguments are the actual values passed when calling the function.
```python
calculate_sum(3, 1)  # 4
```
- If you call the function without arguments:
```python
calculate_sum()
```
- You will get a TypeError.

## The return Keyword

- Functions use the `return` keyword to send a value back.

- If you don’t use `return`, Python returns None by default.

- Without `return`
```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1)
print(my_sum)  # None
```
- The function prints the result but does not return it.

- With `return`
```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)  # 4
```
- Now the function returns the value, and it gets stored in my_sum.

## Key Takeaways

- Functions make code reusable.

- Parameters are placeholders.

- Arguments are actual values passed in.

- `return` sends a value back.

- Without `return`, Python returns None.