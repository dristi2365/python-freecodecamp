# What Are Lambda Functions and How Do They Work?

## Regular Functions with def
Up to now, functions have been defined using the `def` keyword:

    def square(num):
        return num ** 2

    print(square(4))  # 16

## Lambda Functions
For higher order functions like `map()` and `filter()`, you can use an anonymous inline function — a **lambda function**.

Here's `square()` refactored as a lambda:

    lambda num: num ** 2

Lambda functions are anonymous — this one no longer has the name `square` attached to it.

### Using Lambdas with filter()

    numbers = [1, 2, 3, 4, 5]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # [2, 4]

Here, a lambda is passed directly into `filter()` to build a new list of even numbers.

## Best Practices

### Avoid Assigning Lambdas to Variables
This defeats the purpose of using an anonymous function:

    numbers = [1, 2, 3, 4, 5]

    square = lambda x: x ** 2
    squared_numbers = list(map(square, numbers))
    print(squared_numbers)  # [1, 4, 9, 16, 25]

Instead, use a regular function:

    numbers = [1, 2, 3, 4, 5]

    def square(num):
        return num ** 2

    squared_numbers = list(map(square, numbers))
    print(squared_numbers)  # [1, 4, 9, 16, 25]

### Avoid Overly Complex Lambdas
This lambda works, but it's hard to read:

    result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
    print(result)  # 14

A regular function with `if`/`else` is clearer:

    def calculate_expression(x):
        if x > 0:
            return x**2 + 2*x - 1
        else:
            return x**3 - x + 4

    print(calculate_expression(3))  # 14

---
**Rule of thumb:** Use a lambda for a single inline expression. Use a regular function for anything more complex.