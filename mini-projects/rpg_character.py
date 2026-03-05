# Function to create an RPG character with stats
def create_character(name, STR, INT, CHA):

    # ---- Name validation ----
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    # ---- Stats validation ----
    stats = [STR, INT, CHA]

    # Check if all stats are integers
    if (type(STR) != int) or (type(INT) != int) or (type(CHA) != int):
        return "All stats should be integers"

    # Stats must be at least 1
    if (STR < 1) or (INT < 1) or (CHA < 1):
        return "All stats should be no less than 1"

    # Stats cannot be greater than 4
    if (STR > 4) or (INT > 4) or (CHA > 4):
        return "All stats should be no more than 4"

    # Total stat points must equal 7
    if STR + INT + CHA != 7:
        return "The character should start with 7 points"

    # ---- Create visual stat bars ----
    # Filled circles represent stat points
    # Empty circles represent remaining capacity
    STR_bar = "●" * STR + "○" * (10 - STR)
    INT_bar = "●" * INT + "○" * (10 - INT)
    CHA_bar = "●" * CHA + "○" * (10 - CHA)

    # Return formatted character sheet
    return f"{name}\nSTR {STR_bar}\nINT {INT_bar}\nCHA {CHA_bar}"


# Example character creation
print(create_character("Aria", 3, 2, 2))