"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
1. Header Docstring included.
2. NATO_ALPHABET constant is a dictionary (Full A-Z).
3. Program takes a word and uppercases it.
4. Program loops through letters and prints NATO words.
5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# Define the NATO alphabet dictionary
NATO_ALPHABET = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", 
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", 
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", 
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", 
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", 
    "Z": "Zulu"
}

# Ask for a word to spell out using the NATO alphabet
word = input("Enter word to spell: ").upper()

# Loop through each letter in the word and print its NATO code
for letter in word:
    try:
        # Check if the letter exists in the NATO_ALPHABET dictionary
        print(NATO_ALPHABET[letter])
    except KeyError:
        # Handle any characters that are not in the alphabet (like punctuation or numbers)
        print(f"WARNING: '{letter}' is not a valid letter for NATO spelling.")