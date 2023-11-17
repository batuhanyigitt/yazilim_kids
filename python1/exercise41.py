import os
import json
import getpass
from datetime import datetime

# Function to create a new diary entry
def create_entry():
    entry = input("Write your diary entry:\n")
    category = input("Enter a category or tag for this entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    diary_entry = {
        "timestamp": timestamp,
        "entry": entry,
        "category": category
    }
    
    with open("diary.json", "a") as file:
        json.dump(diary_entry, file)
        file.write('\n')

# Function to view and search diary entries
def view_entries():
    search_date = input("Enter a date (YYYY-MM-DD) to search for entries (press Enter to skip): ")
    search_category = input("Enter a category or tag to search for entries (press Enter to skip): ")
    
    with open("diary.json", "r") as file:
        entries = [json.loads(line) for line in file]
    
    for entry in entries:
        if (not search_date or entry["timestamp"].startswith(search_date)) and (not search_category or entry["category"] == search_category):
            print(f"Timestamp: {entry['timestamp']}")
            print(f"Category: {entry['category']}")
            print(f"Entry: {entry['entry']}\n")

# Function to run the diary application
def main():
    if not os.path.exists("diary.json"):
        with open("diary.json", "w") as file:
            file.write('')
    
    while True:
        print("Personal Diary")
        print("1. Create a new diary entry")
        print("2. View and search diary entries")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            create_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
