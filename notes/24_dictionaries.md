# What Are Dictionaries, and How Do They Work?

Dictionaries are built-in data structures that store collections of **key-value pairs** — similar to a real dictionary, where you look up a word to find its meaning.

Use dictionaries when you need to associate values with unique keys — helpful for fast lookups and representing structured data.

## Basic Syntax

    dictionary = {
        key1: value1,
        key2: value2
    }

Each key maps to a value. Keys must be **unique** and **immutable**. Values can repeat and be of any data type.

### Example: Pizza Dictionary

    pizza = {
        'name': 'Margherita Pizza',
        'price': 8.9,
        'calories_per_slice': 250,
        'toppings': ['mozzarella', 'basil']
    }

## Creating a Dictionary with dict()
Builds a dictionary from a sequence of key-value pairs (e.g. a list of tuples):

    pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

## Accessing Values: Bracket Notation

    dictionary[key]

Example:

    pizza['name']
    # 'Margherita Pizza'

## Updating Values
Assign a new value to a key. If the key doesn't exist, a new key-value pair is created. Dictionaries preserve insertion order.

    pizza['name'] = 'Margherita'
    print(pizza['name'])  # 'Margherita'

## Dictionary Methods

### .get()
Retrieves a value by key, with an optional default if the key doesn't exist (avoids errors):

    dictionary.get(key, default)

    pizza.get('toppings', [])  # ['mozzarella', 'basil']

### .keys()
Returns a view object of all keys:

    pizza.keys()
    # dict_keys(['name', 'price', 'calories_per_slice'])

### .values()
Returns a view object of all values:

    pizza.values()
    # dict_values(['Margherita Pizza', 8.9, 250])

> A **view object** shows the dictionary's content without creating a separate copy of the data.

### .items()
Returns a view object of all key-value pairs:

    pizza.items()
    # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

### .clear()
Removes all key-value pairs:

    pizza.clear()

### .pop()
Removes a key-value pair by key and returns its value. Accepts an optional default if the key doesn't exist — otherwise raises a `KeyError`:

    pizza.pop('price', 10)
    pizza.pop('total_price')  # KeyError

### .popitem()
Removes and returns the **last inserted** item (Python 3.7+):

    pizza.popitem()

### .update()
Merges another dictionary's key-value pairs in. Shared keys get overwritten; new keys get added:

    pizza.update({ 'price': 15, 'total_time': 25 })

Result:

    {
        'name': 'Margherita Pizza', 
        'price': 15, 
        'calories_per_slice': 250, 
        'toppings': ['mozzarella', 'basil'], 
        'total_time': 25
    }

---
These are some of the most commonly used dictionary methods — there are more, and picking the right one helps you perform complex operations efficiently.