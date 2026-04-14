"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# --- GLOBAL CONSTANTS ---
CONFIG_FILE = "menu_config.txt"

# --- PHASE 1: CREATING THE DATA ---

def create_menu_config():
    """Gathers categories to build the external config file."""
    print("--- Phase 1: Menu Configuration ---")
    menu_dict = {}
    
    #categories
    categories = ["COFFEE", "FOOD", "SIDES", "DRINKS"]
    
    for cat in categories:
        items = input(f"Enter items for {cat} (separated by commas): ").strip()
        menu_dict[cat] = items
    
    # Write to file using 'w'
    with open(CONFIG_FILE, "w") as file:
        for key, value in menu_dict.items():
            file.write(f"{key}:{value}\n")
    print(f"\nSuccessfully created {CONFIG_FILE}!\n")

# --- PHASE 2: READING & PARSING ---

def load_menu_from_file():
    """Reads and parses the .txt file into a Dictionary."""
    temp_menu = {}
    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                # Parsing Pipeline: strip and split
                if ":" in line:
                    parts = line.strip().split(":")
                    category = parts[0].strip()
                    details = parts[1].strip()
                    temp_menu[category] = details
        return temp_menu
    except FileNotFoundError:
        #Handle missing file
        print(f"Error: {CONFIG_FILE} not found. Starting setup...")
        return None

def split_to_variables(menu_data):
    #Break dictionary into individual variables.
    # We use .get() to avoid crashes if a key is missing
    v1 = menu_data.get("COFFEE", "None")
    v2 = menu_data.get("FOOD", "None")
    v3 = menu_data.get("SIDES", "None")
    v4 = menu_data.get("DRINKS", "None")
    return v1, v2, v3, v4

def display_final_menu(c1, c2, c3, c4):
    """Print each category and its details."""
    print("="*30)
    print("      CAFE SYSTEM MENU")
    print("="*30)
    
    labels = ["COFFEE", "FOOD", "SIDES", "DRINKS"]
    items = [c1, c2, c3, c4]
    
    for i in range(len(labels)):
        print(f"\n[{labels[i]}]")
        # Split the detail string back into a list for clean printing
        individual_items = items[i].split(",")
        for item in individual_items:
            print(f"  - {item.strip()}")

# --- MAIN LOGIC ---

def main():
    # Attempt to load existing data
    menu_items = load_menu_from_file()
    
    # If file doesn't exist, run Phase 1
    if menu_items is None:
        create_menu_config()
        # Try loading again after creation
        menu_items = load_menu_from_file()
    
    # Phase 2: Process and Display
    if menu_items:
        coffee, food, sides, drinks = split_to_variables(menu_items)
        display_final_menu(coffee, food, sides, drinks)

if __name__ == "__main__":
    main()