"""
    No docstring available for this assignment. Copying and pasting this instead:
    1. Initialize balance = 1000.00
2. Start a WHILE True loop:
    a. Print Menu (1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit)
    b. Get user choice
    c. MATCH choice:
        case "1": Print formatted balance
        case "2": Get deposit amt -> Validate it is numeric -> Add to balance
        case "3": Get withdraw amt -> Validate it is numeric -> Check for Overdraft -> Subtract
        case "4": Get transfer amt -> Validate it is numeric -> Check for Overdraft -> Subtract
        case "5": Print goodbye -> Break loop
        case _: Print "Invalid Selection"
"""

# Initialize balance
balance = 1000.00

# Start the program loop
while True:
    # Print Menu
    print("\nATM Menu:")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    
    # Get user choice
    choice = input("Please choose an option (1-5): ")

    # Handle the user choice with match-case
    match choice:
        case "1":
            # Print balance
            print(f"Your balance is: ${balance:.2f}")

        case "2":
            # Deposit money
            deposit = input("Enter deposit amount: ")
            if deposit.isdigit() and float(deposit) > 0:
                balance += float(deposit)
                print(f"Deposited ${deposit}. New balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount. Please enter a positive number.")

        case "3":
            # Withdraw money
            withdrawal = input("Enter withdrawal amount: ")
            if withdrawal.isdigit() and float(withdrawal) > 0:
                if float(withdrawal) <= balance:
                    balance -= float(withdrawal)
                    print(f"Withdrew ${withdrawal}. New balance: ${balance:.2f}")
                else:
                    print("Error: Insufficient funds for withdrawal.")
            else:
                print("Invalid withdrawal amount. Please enter a positive number.")

        case "4":
            # Transfer money (just subtracting from balance for simplicity)
            transfer = input("Enter transfer amount: ")
            if transfer.isdigit() and float(transfer) > 0:
                if float(transfer) <= balance:
                    balance -= float(transfer)
                    print(f"Transferred ${transfer}. New balance: ${balance:.2f}")
                else:
                    print("Error: Insufficient funds for transfer.")
            else:
                print("Invalid transfer amount. Please enter a positive number.")

        case "5":
            # Exit the program
            print("Goodbye!")
            break

        case _:
            print("Invalid selection. Please choose a valid option (1-5).")