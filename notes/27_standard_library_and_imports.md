# What Is the Python Standard Library, and How Do You Import a Module?

A **library** is like a toolbox for developers — pre-written, reusable code (functions, classes, data structures) instead of implementing everything from scratch.

## The Python Standard Library
Python ships with an extensive standard library of built-in modules — standardized, well-vetted solutions for common tasks:

- Interacting with the operating system
- Working with files
- Networking
- Working with date and time
- Performing mathematical operations
- Using regular expressions
- Testing and debugging code
- And much more

Popular built-in modules:
- **math** — complex mathematical operations
- **random** — generating random numbers
- **re** — regular expressions
- **datetime** — working with dates and times

## Basic Import Statement

    import module_name

Example:

    import math

To use something from the module, use **dot notation**:

    module_name.function_name()

Example — square root of 36:

    math.sqrt(36)

## Importing with an Alias
Useful for shortening long module names or avoiding naming conflicts:

    import module_name as module_alias

Example:

    import math as m 

Then use the alias:

    m.sqrt(36)

## Importing Specific Names
If you only need one or two functions/classes:

    from module_name import name1, name2

These names can then be used **without** the module prefix.

### With Aliases

    from module_name import name1 as alias1, name2 as alias2

### Example

    from math import radians, sin, cos

Full example — sine and cosine of an angle:

    from math import radians, sin, cos

    angle_degrees = 40
    angle_radians = radians(angle_degrees)

    sine_value = sin(angle_radians)
    cos_value = cos(angle_radians)

    print(sine_value) # 0.6427876096865393
    print(cos_value)  # 0.766044443118978

> ⚠️ This style can cause naming conflicts if the script already has functions/variables with the same name.

## Importing Everything with `*`

    from module_name import *

Example:

    from math import *
    print(sqrt(36))  # 6.0
    print(pow(5, 2)) # 25.0
    print(exp(1))    # 2.718281828459045

> ⚠️ **Generally discouraged** — can cause namespace collisions and makes it unclear where names come from.

## Importing Constants and Classes
Import statements work the same way for constants, classes, functions, and variables.

### Constant Example (math.pi)

    import math
    print(math.pi)

### Class Example (datetime.date)

    import datetime
    birthday = datetime.date(1959, 7, 15)
    print(birthday.day)    # 15
    print(birthday.month)  # 7
    print(birthday.year)   # 1959

> More details can be found in the official Python documentation for each module.

## The `if __name__ == '__main__':` Idiom
`__name__` is a special built-in variable:

- When a file is run **directly**, `__name__` is set to `"__main__"`.
- When a file is **imported** as a module, `__name__` is set to the module's name (usually the filename without `.py`).

This pattern lets code run only when the script is executed directly:

    if __name__ == '__main__': 
        # Code

If the script is imported instead, this block is **skipped**.

This allows a script to serve two purposes: run directly to execute its main logic, or be imported elsewhere without running that logic.