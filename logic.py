"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (number_one and number_two).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize number_one (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# --- GETTING USER INPUT ---
# We will ask the user to input two numbers
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

# --- LOGICAL CHECKS ---
# 1. Check if both numbers are greater than 0
if number_one > 0 and number_two > 0:
    print("\nBoth numbers are positive!")
else:
    print("\nAt least one number is not positive.")

# 2. Check if both numbers are greater than 100
if number_one > 100 and number_two > 100:
    print("Both numbers are greater than 100!")
else:
    print("At least one number is not greater than 100.")

# 3. Check if either number is even
if number_one % 2 == 0 or number_two % 2 == 0:
    print("At least one number is even!")
else:
    print("Both numbers are odd!")

# 4. Check if either number is less than 100
if number_one < 100 or number_two < 100:
    print("At least one number is less than 100!")
else:
    print("Both numbers are 100 or greater.")

# 5. Check if the numbers are not equal
if number_one != number_two:
    print("The numbers are not equal!")
else:
    print("The numbers are equal!")

# 6. Check if neither number is zero
if number_one != 0 and number_two != 0:
    print("Neither number is zero!")
else:
    print("At least one number is zero.")

# --- CATEGORIZING number_one ---
# Use if/elif/else to categorize number_one as Positive, Negative, or Zero
if number_one > 0:
    print(f"\nnumber_one ({number_one}) is Positive.")
elif number_one < 0:
    print(f"\nnumber_one ({number_one}) is Negative.")
else:
    print(f"\nnumber_one ({number_one}) is Zero.")