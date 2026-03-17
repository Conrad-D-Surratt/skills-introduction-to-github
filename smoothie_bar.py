"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# --- FUNCTION TO DETERMINE PRICE ---
def get_price(size):
    """Return the base price for a smoothie based on size."""
    size = size.title().strip()
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    elif size == "Large":
        return 5.00
    else:
        # Default price if the size is unrecognized
        return 3.00

# --- FUNCTION TO DISPLAY SMOOTHIE DETAILS ---
def blend(size, base, fruit, scoops):
    """Print the smoothie order details."""
    print("\n--- Blending Your Smoothie ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")

# --- MAIN FUNCTION ---
def main():
    print("Welcome to Monty's Smoothie Bar!")

    # Get user input for size, base, fruit
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input(f"Select Base {BASES}: ").title().strip()
    choice_fruit = input(f"Select Fruit {FRUITS}: ").title().strip()

    # Handle scoops input safely
    try:
        scoops = int(input("Number of fruit scoops: "))
        if scoops < 1:
            print("Invalid number of scoops. Defaulting to 1.")
            scoops = 1
    except ValueError:
        print("Invalid entry. Defaulting to 1 scoop.")
        scoops = 1

    # Store the price using the return value
    cost = get_price(choice_size)

    # Call the blend function to display order
    blend(choice_size, choice_base, choice_fruit, scoops)

    # Show total cost
    print(f"Total Bill: ${cost:.2f}")

# Run the program
main()