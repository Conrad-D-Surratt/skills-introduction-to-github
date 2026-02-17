"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# 1. Validate First Name (Cannot be blank)
first_name = input("Enter First Name: ")
while first_name == "":
    first_name = input("Please enter First Name: ")

# 2. Validate Last Name (Cannot be blank)
last_name = input("Enter Last Name: ")
while last_name == "":
    last_name = input("Please enter Last Name: ")

# 3. Validate Chaperone Status (Must be Y or N)
chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()
while chaperone not in ['Y', 'N']:
    chaperone = input("Please enter 'Y' or 'N' for chaperone: ").upper()

# 4. Validate Phone Number (Must be numeric)
phone_number = input("Enter phone number: ")
while phone_number == "":
    phone_number = input("Please enter phone number: ")

# If you want to make sure the phone number is a number, add this:
while not phone_number.isdigit():
    print("Error: Phone number must be a valid number.")
    phone_number = input("Please enter a valid phone number: ")

# 5. Validate Ticket Count (Must be an Integer and > 0)
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break  # Valid number! Escape the loop!
    except ValueError:
        print("Error: Please enter a valid number.")

# Print confirmation
print(f"\nRegistration Complete for {first_name} {last_name}!")
print(f"Phone Number: {phone_number}")
print(f"Chaperone Status: {chaperone}")
print(f"Tickets Ordered: {tickets}")
