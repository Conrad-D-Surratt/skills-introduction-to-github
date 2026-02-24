"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# Step 1: Define the MONTHS tuple (constant)
MONTHS = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")

# Step 2: Use a for loop to display each month
print("Here are the months of the year:")
for month in MONTHS:
    print(month)

# Step 3: Attempt to modify the tuple and catch the TypeError
print("\nAttempting to modify the tuple...")

try:
    MONTHS[0] = "Smarch"  # This will raise a TypeError because tuples are immutable
except TypeError:
    print("!! ERROR: System settings are locked and immutable. You cannot change the tuple. !!")

# Step 4: Add meaningful comments (explaining why modification failed)
# You can't change anything inside a tuple. Once you create it, it stays.
# Trying to change one of the months gives you an error, and that's why I used try or except.