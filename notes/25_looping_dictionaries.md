# What Are Some Common Techniques to Loop Over a Dictionary?

Looping over a dictionary lets you access and process its key-value pairs — useful for updating values or applying logic to them.

### Example Dictionary

    products = {
        'Laptop': 990,
        'Smartphone': 600,
        'Tablet': 250,
        'Headphones': 70,
    }

The `.values()`, `.keys()`, and `.items()` methods return **view objects**, which can be iterated over in `for` loops.

## Iterating Over Values

    for price in products.values():
        print(price)

Output:

    990
    600
    250
    70

## Iterating Over Keys
Use `.keys()`, or iterate over the dictionary directly (equivalent):

    for product in products.keys():
        print(product)

    # Or

    for product in products:
        print(product)

Output:

    Laptop
    Smartphone
    Tablet
    Headphones

## Iterating Over Key-Value Pairs
Use `.items()` to get tuples of each key and its value:

    for product in products.items():
        print(product)

Output:

    ('Laptop', 990)
    ('Smartphone', 600)
    ('Tablet', 250)
    ('Headphones', 70)

### Unpacking Key and Value into Separate Variables
Define two loop variables, separated by a comma — key first, then value:

    for product, price in products.items():
        print(product, price)

Output:

    Laptop 990
    Smartphone 600
    Tablet 250
    Headphones 70

## Practical Example: Applying a 20% Discount
Loop through key-value pairs and reassign each value:

    products = {
        'Laptop': 990,
        'Smartphone': 600,
        'Tablet': 250,
        'Headphones': 70,
    }

    for product, price in products.items():
        products[product] = round(price * 0.8)

    print(products)

Result:

    {
        'Laptop': 792, 
        'Smartphone': 480, 
        'Tablet': 200, 
        'Headphones': 56
    }

## Looping with enumerate()
`enumerate()` adds a counter (default starts at `0`) to each item during iteration.

### Over Keys

    for product in enumerate(products):
        print(product)

Output:

    (0, 'Laptop')
    (1, 'Smartphone')
    (2, 'Tablet')
    (3, 'Headphones')

Unpacked into separate variables:

    for index, product in enumerate(products):
        print(index, product)

### Over Values

    for price in enumerate(products.values()):
        print(price)

Output:

    (0, 990)
    (1, 600)
    (2, 250)
    (3, 70)

Unpacked:

    for index, price in enumerate(products.values()):
        print(index, price)

Output:

    0 990
    1 600
    2 250
    3 70

### Over Key-Value Pairs

    for index, product in enumerate(products.items()):
        print(index, product)

Output:

    0 ('Laptop', 990)
    1 ('Smartphone', 600)
    2 ('Tablet', 250)
    3 ('Headphones', 70)

### Custom Starting Count
Pass a second argument to `enumerate()` to set the starting count:

    for index, product in enumerate(products.items(), 1):
        print(index, product)

Output:

    1 ('Laptop', 990)
    2 ('Smartphone', 600)
    3 ('Tablet', 250)
    4 ('Headphones', 70)

This works with any variation shown above — just pass the initial number as the second argument.

---
There are many techniques to loop over a dictionary — choose the one that best fits your project.