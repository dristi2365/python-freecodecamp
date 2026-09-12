# How to Handle Object Attributes Dynamically?

Attributes are variables that belong to an object — they hold data describing the object's state.

    class Car: 
        def __init__(self, brand, model): 
            self.brand = brand 
            self.model = model 

    my_car = Car('Lamborghini', 'Gallardo') 
    print(my_car.brand) # Lamborghini 
    print(my_car.model) # Gallardo 

Sometimes you don't know which attributes you need until the program is running (e.g. attribute names coming from user input or a config file). **Dynamic attribute handling** lets you access, modify, check, or delete attributes using their names as variables instead of fixed names in code.

Python provides four built-in functions for this: `getattr()`, `setattr()`, `hasattr()`, and `delattr()`.

## getattr()
Reads an attribute when you don't know its name until runtime. Raises `AttributeError` if missing — unless you provide a default value.

    getattr(object, attribute_name, default_value) 

Example:

    class Person: 
        def __init__(self, name, age): 
            self.name = name 
            self.age = age 

    person = Person('John Doe', 30) 
     
    print(getattr(person, 'name')) # John Doe 
    print(getattr(person, 'age')) # 30 
    print(getattr(person, 'city', 'Milano')) # Milano

`'Milano'` is returned as the default since `city` doesn't exist on `Person`.

### Real Power: Attribute Name from a Variable
When the attribute name comes from user input or a file, you can't use regular `object.attribute_name` syntax:

    class Person: 
        def __init__(self, name, age): 
            self.name = name 
            self.age = age 

    person = Person('John Doe', 30)

    attr_name = input('Enter the attribute you want to see: ')
    print(getattr(person, attr_name, 'Attribute not found'))

Typing `name` shows `John Doe`, `age` shows `30`, and anything nonexistent (like `email`) shows `'Attribute not found'`.

## dir()
Returns a list of all attribute names on an object — useful for looking through everything an object has.

    class Person: 
        def __init__(self, name, age): 
            self.name = name 
            self.age = age 

    person = Person('John Doe', 30)

    # Loop through all attributes of the person object with dir() function
    for attr in dir(person):
        # Ignore dunder methods like __init__ or __str__ and regular methods
        if not attr.startswith('__') and not callable(getattr(person, attr)): 
            value = getattr(person, attr)
            print(f'{attr}: {value}')

    # Output
    # age: 30
    # name: John Doe

`callable()` returns `True` if something can be called like a function/method. Checking `not callable(...)` filters out methods, leaving only data attributes.

## setattr()
Creates a new attribute or updates an existing one dynamically.

    setattr(object, attribute_name, value) 

Example — setting config values from runtime data:

    class Configuration:
        pass

    # Data loaded at runtime (like from a config or env file)
    settings_data = {
        'server_url': 'https://api.example.com',
        'timeout_sec': 30,
        'max_retries': 5
    }

    config_obj = Configuration()

    # Dynamically set attributes using dictionary keys and values
    for attr_name, attr_value in settings_data.items():
        setattr(config_obj, attr_name, attr_value)

    print(config_obj.server_url) # https://api.example.com
    print(config_obj.timeout_sec) # 30

## hasattr()
Checks whether an attribute exists — returns `True` or `False`. Good practice to check before using or deleting an attribute.

    hasattr(object, attribute_name)  

Example:

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    product_a = Product('T-Shirt', 25)

    required_attributes = ['name', 'price', 'inventory_id']

    for attr in required_attributes:
        if not hasattr(product_a, attr):
            print(f"ERROR: Product is missing the required attribute: '{attr}'")
        else:
            # Access the attributes dynamically once their existence is confirmed
            print(f'{attr}: {getattr(product_a, attr)}')

    # Output:
    # name: T-Shirt
    # price: 25
    # ERROR: Product is missing the required attribute: 'inventory_id'

The error appears because `inventory_id` doesn't exist on the `Product` instance.

## delattr()
Removes an attribute dynamically.

    delattr(object, attribute_name) 

Example — cleaning up sensitive/temporary attributes before saving:

    class UserSession:
        def __init__(self, user_id, token):
            self.user_id = user_id
            self.auth_token = token # sensitive
            self.temp_counter = 0 # temporary

    session = UserSession(101, 'a1b2c3d4e5')

    # List of attributes to remove dynamically before "saving" the session
    attributes_to_clean = ['auth_token', 'temp_counter']

    # Dynamically remove specified attributes
    for attr in attributes_to_clean:
        if hasattr(session, attr):
            delattr(session, attr)
            print(f'Removed attribute: {attr}')

    print('\nFinal attributes remaining:')

    # Loop through the remaining attributes with dir()
    for attr in dir(session):
        # Ignore dunder methods like __init__ or __str__ and regular methods
        if not attr.startswith('__') and not callable(getattr(session, attr)):
            print(f' - {attr}: {getattr(session, attr)}')

    # Output:
    # Removed attribute: auth_token
    # Removed attribute: temp_counter

    # Final attributes remaining:
    #  - user_id: 101