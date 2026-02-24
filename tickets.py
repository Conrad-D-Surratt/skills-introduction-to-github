"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: MOVIE TICKET BOOKING SYSTEM
-----------------------------------------------------------------------
[ ] 1. Create a list of 10 seats (numbered 1-10).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# List of seats (1 to 10)
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while seats:
    print("Available Seats:", seats)
    
    # Ask for seat number
    choice = int(input("Pick a seat (1-10) or 0 to quit: "))
    
    if choice == 0:
        print("Goodbye!")
        break
    
    # Check if the seat is available
    if choice in seats:
        seats.remove(choice)
        print(f"Seat {choice} booked!")
    else:
        print("Invalid seat or already taken.")

    if not seats:
        print("All seats are booked!")
        break