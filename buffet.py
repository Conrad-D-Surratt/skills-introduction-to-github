"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: February 2, 2026
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price.
3. Print the final price formatted as currency.
-----------------------------------------------------------------------
"""

# Ask the user for their age
age = int(input("\nPlease enter your age: "))

# Determine price based on their age
if age < 1:
    price = 0.00
elif age <= 11:
    price = float(age)
elif age <= 64:
    price = 16.95
else:
    price = 12.95

# Output the final price
print(f"Your buffet price is ${price:.2f}\n")