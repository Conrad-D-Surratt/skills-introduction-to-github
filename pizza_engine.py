"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# --- GLOBAL PANTRY RULES ---
TOPPINGS = ("Pepperoni", "Mushrooms", "Green Peppers", "Extra Cheese")

# --- FUNCTION: THE PIZZA ENGINE ---
def make_pizza(customer, size, topping, is_delivery=False):
    """Processes pizza order and prints a ticket.
    
    :param customer: Name of the customer
    :param size: Pizza size (Small/Medium/Large)
    :param topping: Selected topping from TOPPINGS
    :param is_delivery: Boolean for delivery (default False)
    """
    print("\n--- OFFICIAL PIZZA TICKET ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery: {'Yes' if is_delivery else 'No'}")

# --- MAIN FUNCTION ---
def main():
    # Get customer info
    customer_name = input("Enter your name: ").title()
    
    # Display available toppings from global tuple
    print(f"Available toppings: {TOPPINGS}")
    
    # Select size
    size_choice = input("Select pizza size (Small/Medium/Large): ").title()
    
    # Select topping with safety check
    topping_choice = input("Select topping: ").title()
    if topping_choice not in TOPPINGS:
        print(f"Sorry, '{topping_choice}' is not available. Defaulting to 'Extra Cheese'.")
        topping_choice = "Extra Cheese"
    
    # Ask about delivery safely
    delivery_input = input("Do you want delivery? (Y/N): ").upper()
    if delivery_input == "Y":
        delivery_choice = True
    else:
        delivery_choice = False
    
    # Call the pizza engine using keyword arguments
    make_pizza(
        customer=customer_name,
        size=size_choice,
        topping=topping_choice,
        is_delivery=delivery_choice
    )

# --- RUN THE PROGRAM ---
main()