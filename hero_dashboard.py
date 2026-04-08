"""
-----------------------------------------------------------------------
Developer: Conrad Surratt
Date: April 7, 2026
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
OFFICE_NAME = "Conrad's Tech Solutions"
TAX_RATE = 0.05

def process_expenses(item, cost, qty):
    # Step 1: Logic
    subtotal = cost * qty
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    
    # Step 2: Create the summary string
    summary_text = f"Item: {item}, Quantity: {qty}"
    
    # Step 3: Return TWO values
    return total, summary_text

def main():
    print(f"--- {OFFICE_NAME} ---")
    
    try:
        # Collect input
        user_item = input("What are you buying? ")
        user_price = float(input("How much does it cost? "))
        user_qty = int(input("How many do you need? "))
    except ValueError:
        print("Error: Please use numbers for cost and quantity.")
        user_price = 0.0
        user_qty = 0
        user_item = "Unknown"

    # MUST use keyword arguments per Requirement #5
    # MUST unpack two values per Requirement #6
    # Note: the keywords (item=, cost=, qty=) must match the function header above
    final_bill, receipt_msg = process_expenses(item=user_item, cost=user_price, qty=user_qty)
    
    # Final Output
    print("\n--- RESULTS ---")
    print(f"Details: {receipt_msg}")
    print(f"Total: ${final_bill:.2f}")

# Call the main function
main()