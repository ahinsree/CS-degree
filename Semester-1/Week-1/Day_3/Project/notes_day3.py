def print_header():
    """Prints the header and gets the date."""
    print("=" * 40)
    print("   DAY 3 REVISION NOTES - LOOPS")
    print("   CS50P Lecture 2 + MIT 6.0001 Lecture 2")
    date = input("Enter today's date (YYYY-MM-DD): ")
    print(f"   Date: {date}")
    print("=" * 40 + "\n")
    return date

def get_notes():
    """Gathers notes from the user."""
    notes = {
        "KEY RESOURCES WATCHED TODAY": [
            "1. CS50P Lecture 2",
            "2. MIT 6.0001 Lecture 2"
        ],
        "LOOP DEFINITIONS": [
            "FOR LOOP → use when",
            "WHILE LOOP → use when",
            "BREAK   → (in my own words)",
            "CONTINUE → (in my own words)",
            "PASS    → (in my own words)",
            "NESTED LOOP → (in my own words)"
        ],
        "INSIGHTS & CHALLENGES": [
            "BIGGEST INSIGHT FROM CS50P TODAY",
            "BIGGEST INSIGHT FROM MIT 6.0001 TODAY",
            "SOMETHING I FOUND DIFFICULT",
            "SOMETHING I EXPLORED BEYOND THE LESSON"
        ]
    }

    user_notes = {}

    for category, questions in notes.items():
        print(f"\n--- {category} ---\n")
        user_notes[category] = {}
        for question in questions:
            user_notes[category][question] = input(f"{question}: ")
    
    return user_notes

def display_notes(date, notes):
    """Displays the collected notes."""
    print("\n\n" + "=" * 20)
    print("YOUR REVISION NOTES")
    print("=" * 20)
    print(f"Date: {date}")
    
    for category, questions_and_answers in notes.items():
        print(f"\n--- {category} ---")
        for question, answer in questions_and_answers.items():
            print(f"  {question}: {answer}")


def save_notes(date, notes):
    """Saves the notes to a text file."""
    filename = f"notes_{date}.txt"
    with open(filename, 'w') as f:
        f.write("=" * 20 + "\n")
        f.write("YOUR REVISION NOTES\n")
        f.write("=" * 20 + "\n")
        f.write(f"Date: {date}\n")

        for category, questions_and_answers in notes.items():
            f.write(f"\n--- {category} ---\n")
            for question, answer in questions_and_answers.items():
                f.write(f"  {question}: {answer}\n")
    print(f"Notes saved to {filename}")

def main():
    """Main function to run the script."""
    while True:
        print("\nMenu:")
        print("1. Create new notes")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = print_header()
            notes = get_notes()
            display_notes(date, notes)
            save_choice = input("Do you want to save these notes to a file? (yes/no): ")
            if save_choice.lower() == 'yes':
                save_notes(date, notes)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
