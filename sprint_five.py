"""
-----------------------------------------------------------------------
ASSIGNMENT 12B: SPRINT 5 - DATA PERSISTENCE
Project: Community Book Rental System (V5.0)
Developer: Conrad Surratt
-----------------------------------------------------------------------
"""
import datetime

# GLOBAL CONSTANTS
DATA_FILE = "rental_history.txt" 
HUMAN_REPORT = "latest_receipt.txt" 

def get_customer_info():
    """Asks for name and contact info."""
    name = input("Reader Name: ").title().strip()
    phone = input("Phone Number: ")
    return name, phone

def take_order():
    """Collects rental choices."""
    book = input("Book Title: ")
    period = input("Period (Daily/Weekly/Monthly): ")
    insurance = input("Rental Insurance (Yes/No): ")
    return {"book": book, "period": period, "insurance": insurance}

def calculate_total(order_data):
    """Calculates price based on rental period."""
    base_price = 5.00  

    if order_data["period"] == "Daily":
        base_price = 2.00
    elif order_data["period"] == "Weekly":
        base_price = 10.00
    elif order_data["period"] == "Monthly":
        base_price = 30.00

    total = base_price

    if order_data["insurance"] == "Yes":
        total += 2.50

    return total

def save_data_and_label(customer, total, order_data):
    """Saves to the Vault (history) and the Report (receipt)."""
    # Simplified date logic: No complex formatting codes
    current_date = str(datetime.date.today())

    # 1. APPEND to the History Log
    with open(DATA_FILE, "a") as file:
        file.write(f"{current_date},{customer},{order_data['book']},{total:.2f}\n")

    # 2. OVERWRITE the Latest Receipt
    with open(HUMAN_REPORT, "w") as file:
        file.write(f"BOOK RENTAL RECEIPT\n")
        file.write(f"DATE: {current_date}\n")
        file.write(f"Customer: {customer}\n")
        file.write("-" * 25 + "\n")
        for key, value in order_data.items():
            file.write(f"{key.capitalize()}: {value}\n")
        file.write("-" * 25 + "\n")
        file.write(f"TOTAL DUE: ${total:.2f}\n")

    print(f"\nSuccess: Records updated. Receipt available in {HUMAN_REPORT}")

def review_past_rentals():
    """Reads the history file back to the user."""
    print("\n--- ACCESSING RENTAL HISTORY VAULT ---")
    # Removed try/except to keep it strictly to lecture scope
    with open(DATA_FILE, "r") as file:
        for line in file:
            print(line.strip())

def main():
    print("Welcome to the Community Library System")
    
    choice = input("Type 'history' to see the Vault or press Enter to start: ")
    if choice.lower() == "history":
        review_past_rentals()

    # 1. Identity
    name, contact = get_customer_info()

    # 2. Collection
    current_rental = take_order()

    # 3. Calculation
    final_price = calculate_total(current_rental)

    # 4. Save
    save_data_and_label(customer=name, total=final_price, order_data=current_rental)

if __name__ == "__main__":
    main()