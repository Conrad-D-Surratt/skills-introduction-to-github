"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

def main():
    # Use a while loop to keep the tracker running
    while True:
        # Get the user choice first
        choice_input = input("Enter 'log' to record a bug, or 'quit' to stop: ")
        
        # Clean the input so it works even with caps or spaces
        user_choice = choice_input.lower()
        user_choice = user_choice.strip()

        if user_choice == "quit":
            print("Bug log updated!")
            break
        
        elif user_choice == "log":
            # Gather the three required pieces of data
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")

            # Get the current system time
            now_time = datetime.datetime.now()
            timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")

            # Store in a dictionary: Key is Timestamp, Value is a List
            bug_entry = {
                timestamp: [file_name, description, priority]
            }

            # Open the log file in append mode to add to the bottom
            with open("bug_log.txt", "a") as file:
                # Pull the data out of the dictionary using the indices [0, 1, 2]
                file.write(f"[{timestamp}]\n")
                file.write(f"File: {bug_entry[timestamp][0]}\n")
                file.write(f"Status: {bug_entry[timestamp][1]}\n")
                file.write(f"Priority: {bug_entry[timestamp][2]}\n")
                file.write("--------------------------------------------------\n")

        else:
            print("Invalid option, please type 'log' or 'quit'.")

# Start the program
main()