"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# --- Task 1: The Nagging Kid (While Loop) ---
# This boolean variable controls the while loop
is_there_yet = False

# Keep asking "Are we there yet?" until the user says "yes"
while not is_there_yet:
    answer = input("Are we there yet? ")
    if answer.lower() == "yes":
        is_there_yet = True
        print("Finally! We're here!\n")  # Add a break after they answer "yes"

# --- Task 2: 99 Bottles of Beer (For Loop) ---
# Use a for loop to count backwards from 99 to 1
for bottles in range(99, 0, -1):
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall!")
        print(f"{bottles} bottle of beer!")
        print("Take one down, pass it around")
        print("No more bottles of beer on the wall!!!!\n")
    else:
        print(f"{bottles} bottles of beer on the wall!")
        print(f"{bottles} bottles of beer!")
        print("Take one down, pass it around")
        print(f"{bottles-1} bottles of beer on the wall!\n")