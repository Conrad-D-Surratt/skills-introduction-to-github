"""
-----------------------------------------------------------------------
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Book Rental System (Refactored)
Developer: Conrad Surratt
-----------------------------------------------------------------------
"""

import datetime

# --- GLOBAL CONSTANTS ---
BOOKS_FILE = "books.txt"
RENTAL_HISTORY_FILE = "rental_history.txt"
RENTAL_COST_PER_BOOK = 3.00
RENTAL_DAYS = 14

# --- FUNCTION DEFINITIONS ---

def get_customer_info(default_name="Guest"):
    """Ask for the user's name and return it. Uses default if none provided."""
    name = input("Please enter your name: ").title().strip()
    if not name:
        name = default_name
    return name

def load_books(file_name=BOOKS_FILE):
    """Load available books from the file."""
    try:
        with open(file_name, "r") as file:
            books = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with empty book list.")
        books = []
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
    mapping = {"1": "view", "2": "rent", "3": "return", "4": "history", "5": "exit"}
    return mapping.get(choice, "invalid")

def rent_book(books):
    """Handle renting a book and return rental details."""
    if not books:
        print("No books available to rent.")
        return None

    print("\nAvailable Books:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book}")

    try:
        selection = int(input("\nPlease select a book number to rent: "))
        if 1 <= selection <= len(books):
            rented_book = books.pop(selection - 1)
            save_books(books)
            print(f'Book "{rented_book}" rented successfully!')
            return rented_book
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def return_book(books):
    """Handle returning a book."""
    returned_book = input("Enter the name of the book you are returning: ").title().strip()
    if returned_book:
        books.append(returned_book)
        save_books(books)
        print(f'Book "{returned_book}" returned successfully!')

def calculate_rental_details(cost=RENTAL_COST_PER_BOOK, days=RENTAL_DAYS):
    """Calculate rental cost and due date using global constants."""
    rental_date = datetime.date.today()
    due_date = rental_date + datetime.timedelta(days=days)
    return cost, rental_date, due_date

def save_and_print_receipt(*, customer, book, cost, rental_date, due_date, file_name=RENTAL_HISTORY_FILE):
    """Save rental info to file and print human-readable receipt. Uses keyword arguments for clarity."""
    # Save to raw log
    with open(file_name, "a") as file:
        file.write(f"{customer}, {book}, {rental_date}, {due_date}, {cost:.2f}\n")

    # Print human-readable receipt
    print("\nBOOK RENTAL SYSTEM - USER RECEIPT")
    print("-----------------------------------")
    print(f"USER: {customer}")
    print(f"RENTED BOOK: {book.upper()}")
    print(f"RENTAL DATE: {rental_date}")
    print(f"DUE DATE: {due_date}")
    print(f"TOTAL RENTAL COST: ${cost:.2f}")
    print("-----------------------------------")
    print("Thank you for using the Book Rental System!")

def view_rental_history(file_name=RENTAL_HISTORY_FILE):
    """Display the contents of rental history file."""
    print("\n--- Rental History ---")
    try:
        with open(file_name, "r") as file:
            history = file.readlines()
            if not history:
                print("No rental history yet.")
            else:
                for entry in history:
                    print(entry.strip())
    except FileNotFoundError:
        print(f"{file_name} not found.")

# --- MAIN FUNCTION ---
def main():
    customer = get_customer_info()
    books = load_books()

    while True:
        action = select_action()

        if action == "rent":
            rented_book = rent_book(books)
            if rented_book:
                cost, rental_date, due_date = calculate_rental_details()
                save_and_print_receipt(
                    customer=customer,
                    book=rented_book,
                    cost=cost,
                    rental_date=rental_date,
                    due_date=due_date
                )

        elif action == "return":
            return_book(books)

        elif action == "view":
            view_rental_history()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

# --- RUN PROGRAM ---
if __name__ == "__main__":
    main()