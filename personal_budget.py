"""
-------------------------------------------------------
Assignment 3A: Personal Budget
Calculates total expenses and percentage of income spent
-------------------------------------------------------
"""

# --- 1. GET INPUT ---
monthly_income = float(input("\nEnter your monthly income: $"))
print()
rent = float(input("Enter rent expense: $"))
utilities = float(input("Enter utilities expense: $"))
groceries = float(input("Enter groceries expense: $"))
mcc = float(input("Enter McHenry County College expense: $"))
video_games = float(input("Enter video game expenses: $"))

# --- 2. CALCULATIONS ---
total_expenses = rent + utilities + groceries + mcc + video_games
remaining_balance = monthly_income - total_expenses
percent_spent = total_expenses / monthly_income

# --- 3. OUTPUT ---
print("\n--- Monthly Budget Summary ---")
print(f"Monthly Income:      ${monthly_income:,.2f}")
print(f"Total Expenses:      ${total_expenses:,.2f}")
print(f"Remaining Balance:   ${remaining_balance:,.2f}")
print(f"Percentage Spent:    {percent_spent:.2%}\n")
