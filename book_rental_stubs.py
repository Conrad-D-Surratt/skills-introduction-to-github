"""
-----------------------------------------------------------------------
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Book Rental System
Developer: Your Name
-----------------------------------------------------------------------
"""

def get_customer_info():
    """Asks for the user's name and returns it."""
    # TODO: Ask for name and return it
    return "Conrad Surratt"  # placeholder

def select_action():
    """Displays menu options and returns user's choice."""
    # TODO: Capture choice (rent, return, view books, history)
    pass

def rent_book():
    """Handles renting a book and returns rental details."""
    # TODO: Ask which book, check availability
    pass

def return_book():
    """Handles returning a book and updates records."""
    # TODO: Ask which book is being returned
    pass

def calculate_rental_details(rental_data):
    """Calculates cost, due date, etc."""
    # TODO: Calculate rental cost and due date
    return 3.00, "2023-10-15"  # placeholders

def save_and_print_receipt(customer, rental_details):
    """Saves rental info to file and prints human-readable receipt."""
    # TODO: Write to rental_history.txt and print receipt
    pass

def main():
    # 1. Identity Phase
    customer = get_customer_info()
    print(f"Customer: {customer}")

    # 2. Data Collection Phase
    action = select_action()

    if action == "rent":
        # 3. Calculation Phase
        rental_data = rent_book()
        cost, due_date = calculate_rental_details(rental_data)

        # 4. Handoff Phase
        save_and_print_receipt(customer, rental_data)

    elif action == "return":
        return_book()

    elif action == "view":
        # TODO: Display books or history
        pass

# --- Run the program ---
if __name__ == "__main__":
    main()