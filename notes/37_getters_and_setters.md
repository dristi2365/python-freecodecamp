# What Are Getters and Setters?

Getters and setters are methods that control how a class's attributes are accessed and modified. **Getters** retrieve a value, **setters** set a value.

## Properties
Properties connect getters and setters, and allow access to data. They **act like attributes but behave like methods** under the hood — you access them with dot notation, not parentheses.

Properties run extra logic behind the scenes when you get, set, or delete a value — useful for computing values or validating data before saving it.

### Why Properties Instead of Methods?
Mostly readability and convention. A method requires parentheses to call; a property is accessed like a normal attribute, keeping code clean even when extra logic runs behind the scenes.

## Decorators (Brief Context)
A **decorator** is a function that modifies the functionality of another function or class without changing its original code. To create a property, define a method and place `@property` above it — this turns the method into a property.

## Getters

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self): # A getter to get the radius
            return self._radius
      
        @property
        def area(self):  # A getter to calculate area
            return 3.14 * (self._radius ** 2)

    my_circle = Circle(3)

    print(my_circle.radius) # 3
    print(my_circle.area) # 28.26

> `_radius` (single underscore) is a convention signaling the attribute is for internal use and shouldn't be accessed directly from outside the class.

## Setters
Defined with the same method name, using `@<property_name>.setter`:

    class Circle:
        def __init__(self, radius):
            self.radius = radius # Calling the setter

        @property
        def radius(self):  # A getter to get the radius
            return self._radius

        @radius.setter
        def radius(self, value):  # A setter to set the radius
            if value <= 0:
                raise ValueError('Radius must be positive')
            self._radius = value

    my_circle = Circle(3)
    print('Initial radius:', my_circle.radius) # Initial radius: 3

    my_circle.radius = 8
    print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8

> Using `self.radius` inside `__init__` calls the setter during object creation, so invalid values are caught immediately.

The setter here doesn't just set the radius — it also validates that the value isn't negative.

### How It's Called Automatically
Once defined, Python automatically calls getters/setters via normal attribute syntax:

    my_circle.radius # This will call the getter
    my_circle.radius = 4 # This will call the setter

### ⚠️ Avoiding Infinite Recursion
Inside the setter, you **cannot** use the property's own name when assigning (`self.radius = value`) — that would call the setter again, causing infinite recursion and a `RecursionError`. Always use the underscore-prefixed form: `self._radius = value`.

## Deleters
A deleter runs custom logic when `del` is used on a property. Created with `@<property_name>.deleter`:

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        # Getter
        @property
        def radius(self):
            return self._radius

        # Setter
        @radius.setter
        def radius(self, value):
            if value <= 0:
                raise ValueError("Radius must be positive")
            self._radius = value

        # Deleter
        @radius.deleter
        def radius(self):
            print("Deleting radius...")
            del self._radius

### Using the Deleter

    # Create circle object with a radius
    my_circle = Circle(33)
    print("Initial radius:", my_circle.radius)  # 33

    # Delete the radius
    # This calls the deleter
    del my_circle.radius # Deleting radius...
    print("Radius deleted!") # Radius deleted!

    # Try to access radius after deletion
    try:
        print(my_circle.radius)
    except AttributeError as e:
        print("Error:", e) # Error: 'Circle' object has no attribute '_radius'

---
## Takeaways
- **Getters** let you retrieve or compute a value on the fly.
- **Setters** let you modify values safely by running checks before assignment.
- **Properties** tie getters and setters together so you can write logic while still using dot notation.
- **Deleters** let you define what happens when an attribute is deleted.