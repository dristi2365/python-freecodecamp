# What Is Scope in Python and How Does It Work?

In Python, **scope** determines where a variable can be accessed in your code. It controls the lifetime of a variable and how Python resolves variable names.

Python follows the **LEGB rule** to determine scope:

- **L — Local scope**: Variables defined inside functions or classes.
- **E — Enclosing scope**: Variables in nested (outer) functions.
- **G — Global scope**: Variables defined at the top level of a file.
- **B — Built-in scope**: Predefined names in Python.

Python searches for variables in this exact order: **Local → Enclosing → Global → Built-in**.

---

## Local Scope (L)

A variable declared inside a function can only be accessed within that function.

```python
def my_func():
    my_var = 10
    print(my_var)

my_func()  # 10
print(my_var)  # NameError: name 'my_var' is not defined
```
my_var is local to my_func() and cannot be accessed outside it.

## Enclosing Scope (E)

A nested function can access variables from its enclosing (outer) function.

```python
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func()  # Hello there!
```

- Here, inner_func() can access msg from outer_func().

- When Outer Functions Cannot Access Inner Variables
```python
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func()  # NameError
```
- res is locally scoped to inner_func() and cannot be accessed by outer_func().

### Using nonlocal

To modify a variable from the enclosing scope, use the nonlocal keyword.
```python
def outer_func():
    msg = 'Hello there!'
    res = ""

    def inner_func():
        nonlocal res
        res = 'How are you?'
        print(msg)

    inner_func()
    print(res)

outer_func()

# Output:
# Hello there!
# How are you?
```

## Global Scope (G)

Global variables are defined outside functions and can be accessed anywhere.
```python
my_var = 100

def show_var():
    print(my_var)

show_var()  # 100
print(my_var)  # 100
```
- Using the global Keyword, you can declare a variable as global inside a function.
```python
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars()  # 7 10
print(my_var_2)  # 10
Modifying a Global Variable
my_var = 10

def change_var():
    global my_var
    my_var = 20

change_var()
print(my_var)  # 20
```

## Built-in Scope (B)

Built-in scope contains Python's predefined functions and objects.
```python
print(str(45))        # '45'
print(type(3.14))     # <class 'float'>
print(isinstance(3, str))  # False
```

- These are available anywhere in your program.

## Key Takeaways

- Scope determines where variables are accessible.

- Python follows the LEGB rule.

- `nonlocal` modifies enclosing scope variables.

- `global` modifies global variables.

- Built-in names are always available.