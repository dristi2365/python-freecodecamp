# Employee Profile Generator Workshop
# Demonstrates string concatenation, interpolation, and slicing

first_name = 'John'
last_name = 'Doe'

# Full name
full_name = first_name + ' ' + last_name

# Address using += operator
address = '123 Main Street'
address += ', Apartment 4B'

# Basic employee info
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Experience details
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Using f-strings
position = 'Data Analyst'
salary = 75000

employee_card = (
    f'Employee: {full_name} | '
    f'Age: {employee_age} | '
    f'Position: {position} | '
    f'Salary: ${salary}'
)
print(employee_card)

# String slicing examples
employee_code = 'DEV-2026-JD-001'

department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)