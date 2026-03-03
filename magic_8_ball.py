"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# RESPONSES tuple with at least 8 options
RESPONSES = (
    "Yes", 
    "No", 
    "Maybe", 
    "Ask again later", 
    "Definitely", 
    "Absolutely not", 
    "I have no idea", 
    "Cannot predict now"
)

print("Welcome to the Digital Oracle!")

# Start the loop
while True:
    # Ask for user input
    user_question = input("\nAsk a question or type 'quit' to exit: ").strip().lower()

    # Check if the user wants to quit
    if user_question == "quit":
        print("Goodbye!")
        break

    # Provide a random response
    answer = random.choice(RESPONSES)
    print(f"Answer: {answer}")