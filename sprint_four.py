"""
-----------------------------------------------------------------------
ASSIGNMENT 11B: SPRINT 4 - DATA PERSISTENCE
Project: Book Rental System (Refactored)
Developer: Conrad Surratt
-----------------------------------------------------------------------
"""
import datetime

# --- GLOBAL CONSTANTS ---
BOOKS_FILE = "books.txt"
RENTAL_HISTORY_FILE = "rental_history.txt"
RENTAL_COST_PER_BOOK = 3.00

# --- FUNCTION DEFINITIONS ---

def get_customer_info(default_name="Guest"):
    """Ask for the user's name and return it. Uses default if none provided."""
    name = input("Please enter your name: ").title().strip()
    if not name:
        name = default_name
    return name

def load_books(file_name=BOOKS_FILE):
    """Load available books from the file."""
    books = []
    with open(file_name, "r") as file:
        for line in file:
            if line.strip():
                books.append(line.strip())
    return books

def save_books(books, file_name=BOOKS_FILE):
    """Save the updated list of available books back to the file."""
    with open(file_name, "w") as file:
        for book in books:
            file.write(book + "\n")

def select_action():
    """Display menu options and return user's choice."""
    print("\n-----------------------------------")
    print("1. View Available Books")
    print("2. Rent a Book")
    print("3. Return a Book")
    print("4. View Rental History")
    print("5. Exit")
    
    choice = input("Please select an option (1-5): ").strip()
    
    # REPLACED: Using simple if/elif instead of a dictionary mapping
    if choice == "1":
        return "view"
    elif choice == "2":
        return "rent"
    elif choice == "3":
        return "return"
    elif choice == "4":
        return "history"
    elif choice == "5":
        return "exit"
    else:
        return "invalid"

def view_books(books):
    """Simple function to show the books available for rent."""
    print("\n--- Available Books ---")
    if not books:
        print("No books available to rent.")
    else:
        for book in books:
            print("- " + book)

def rent_book(books):
    """Handle renting a book and return rental details."""
    if not books:
        print("No books available to rent.")
        return None

    print("\nAvailable Books:")
    for book in books:
        print("- " + book)

    rented_book = input("\nPlease type the name of the book you want to rent: ").title().strip()
    
    if rented_book in books:
        books.remove(rented_book)
        save_books(books)
        print(f'Book "{rented_book}" rented successfully!')
        return rented_book
    else:
        print("That book is not available.")
        return None

def return_book(books):
    """Handle returning a book."""
    returned_book = input("Enter the name of the book you are returning: ").title().strip()
    if returned_book:
        books.append(returned_book)
        save_books(books)
        print(f'Book "{returned_book}" returned successfully!')

def calculate_rental_details():
    """Calculate rental cost and timestamps."""
    # Note: Using this because it was in the Sprint 4 Master Example
    right_now = datetime.datetime.now()
    current_time_str = right_now.strftime("%Y-%m-%d %H:%M:%S")
    
    # REPLACED: Removed datetime.date.today() and timedelta math
    # Switching to simple strings to stay in scope
    rental_date = "2026-04-06" 
    due_date = "2026-04-20" 
    cost = RENTAL_COST_PER_BOOK
    
    return cost, rental_date, due_date, current_time_str

def save_and_print_receipt(customer, book, cost, rental_date, due_date, current_time, file_name=RENTAL_HISTORY_FILE):
    """Save rental info to file and print human-readable receipt."""
    
    # SPRINT 4 REQUIREMENT: Appending to the log file with timestamp
    with open(file_name, "a") as file:
        file.write(f"[{current_time}] {customer}, {book}, {cost:.2f}\n")

    print("\nBOOK RENTAL SYSTEM - USER RECEIPT")
    print("-----------------------------------")
    print(f"USER: {customer}")
    print(f"RENTED BOOK: {book}")
    print(f"RENTAL DATE: {rental_date}")
    print(f"DUE DATE: {due_date}")
    print(f"TOTAL RENTAL COST: ${cost:.2f}")
    print("-----------------------------------")
    print("Thank you for using the Book Rental System!")

def view_rental_history(file_name=RENTAL_HISTORY_FILE):
    """Display the contents of rental history file."""
    print("\n--- Rental History ---")
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

# --- MAIN FUNCTION ---
def main():
    customer = get_customer_info()
    books = load_books()

    while True:
        action = select_action()

        if action == "rent":
            rented_book = rent_book(books)
            if rented_book:
                # Capture variables from the calculator
                cost, r_date, d_date, time_stamp = calculate_rental_details()
                save_and_print_receipt(customer, rented_book, cost, r_date, d_date, time_stamp)

        elif action == "return":
            return_book(books)

        elif action == "view":
            view_books(books)

        elif action == "history":
            view_rental_history()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

# --- RUN PROGRAM ---
main()