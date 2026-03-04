# Apply Discount Calculator
# FreeCodeCamp Lab - Mini Project


def apply_discount(price, discount):
    # Validate that price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # Validate that discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # Ensure price is positive
    if price <= 0:
        return "The price should be greater than 0"

    # Ensure discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # Calculate discount amount
    discount_amount = (discount / 100) * price

    # Calculate final price
    final_price = price - discount_amount

    return final_price


# Test cases
print(apply_discount(100, 20))      # Expected: 80.0
print(apply_discount(200, 50))      # Expected: 100.0
print(apply_discount(100, 0))       # Expected: 100.0
print(apply_discount(74.5, 59.6))   # Expected: 30.098