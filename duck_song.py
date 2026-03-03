"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Conrad Surratt
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ---
instrument = "Acoustic Guitar"

# Print the length of 'instrument'
print(len(instrument))

# Print the first and last letter of 'instrument'
print(instrument[0])
print(instrument[-1])

# Use min() and max() to find and print the lowest and highest ASCII characters
print(min(instrument))
print(max(instrument))

# --- TASK 2: THE CLEANUP CREW ---
messy_input = "   vOLUME_knob_11   "

# Strip spaces, make everything uppercase, and replace underscores with spaces
messy_input = messy_input.strip().upper().replace("_", " ")

print(messy_input)

# --- TASK 3: THE VALIDATOR ---
serial_number = "90210"

# Check if the serial number is valid (only digits)
if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")

# --- TASK 4: THE DUCK BRIDGE ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

# Loop through name_string
for char in name_string:
    # Join the letters into a string with spaces
    current_name = " ".join(duck_letters)
    
    # Print the song lyrics
    print("There was a teacher who had a duck and Ducky was his Name-o")
    print(f"({current_name}) \n" * 3)
    print("and Ducky was his Name-o!\n")
    
    # Replace the letter at the current index with a placeholder ("*")
    duck_letters[count] = "*"
    count += 1

# After the loop, print the final version
final_name = " ".join(duck_letters)
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!")