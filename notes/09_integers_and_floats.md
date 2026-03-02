# Working with Integers and Floating Point Numbers in Python

Integers and floats are the primary **numeric data types** in Python.  
They allow you to store numbers and perform mathematical operations.

---

## Integers
- Integers (`int`) are **whole numbers** without decimal points.
- They can be positive or negative.

```python
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))  # <class 'int'>
print(type(my_int_2))  # <class 'int'>
```

## Integer Arithmetic

```python
#Addition

my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints)  # 68

#Subtraction

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints)  # 44

#Multiplication

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)  # 48

#Division

div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints)  # 4.666666666666667
```

## Floating Point Numbers

Floats (float) are numbers with decimal points.

```python
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))  # <class 'float'>
print(type(my_float_2))  # <class 'float'>
```

## Float Arithmetic

```python
#Addition

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition)

#Subtraction

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction)

#Multiplication

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication)

#Division

float_division = my_float_2 / my_float_1
print('Float Division:', float_division)
```

## Mixing Integers and Floats

When you mix an integer and a float, Python returns a float.

```python
my_int = 56
my_float = 5.4

result = my_int + my_float
print(result)            # 61.4
print(type(result))      # <class 'float'>
```

## Advanced Arithmetic Operations

### Modulo (%)

Returns the remainder of a division.

```python
mod_ints = 56 % 12
mod_floats = 12.0 % 5.4

print(mod_ints)     # 8
print(mod_floats)   # 1.1999999999999993
```

### Floor Division (//)

Returns the greatest integer less than or equal to the result.

```python
floor_div_ints = 56 // 12
floor_div_floats = 12.0 // 5.4

print(floor_div_ints)    # 4
print(floor_div_floats)  # 2.0
```

### Exponentiation (**)

Raises a number to a power.

```python
exp_ints = 56 ** 12
exp_floats = 5.4 ** 12.0

print(exp_ints)
print(exp_floats)
```

### Floating Point Precision

Sometimes floats produce unexpected results:

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

This happens because:

- Numbers are stored in binary

- Some decimals cannot be represented exactly

- This causes small rounding errors

## Type Conversion

### Converting Numbers

```python
my_int = 56
my_float = float(my_int)

print(my_float)        # 56.0
print(type(my_float))  # <class 'float'>
my_float = 12.92563
my_int = int(my_float)

print(my_int)          # 12
print(type(my_int))    # <class 'int'>
Converting Strings
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))
```

## Useful Built-in Functions
### `round()`

- Rounds numbers to a specified number of decimal places.

```python
rounded_1 = round(4.798)
rounded_2 = round(4.253, 1)

print(rounded_1)  # 5
print(rounded_2)  # 4.3
abs()
```

- Returns the absolute value.

```python
num = -15
print(abs(num))  # 15
pow()
```

- Raises a number to a power (optionally with modulo).

```python
print(pow(2, 3))       # 8
print(pow(2, 3, 5))    # 3
```

## Summary

- Integers and floats are core numeric data types in Python.

- Mixing integers and floats results in a float.

- Python supports advanced arithmetic like modulo, floor division, and exponentiation.

- Floating-point math can have precision issues.

- Built-in functions help with rounding, absolute values, and type conversion.