""" Text Analyser 📄"""

# ============================================
#   TEXT ANALYSER 📄
#   Week 3, Day 1 Project
# ============================================

def analyse_text(text):
    """Analyzes the given text and returns a dictionary with statistics."""
    char_count = len(text)
    char_no_space = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    
    # Character analysis using iteration
    vowels = sum(1 for char in text if char in "aeiouAEIOU")
    consonants = sum(1 for char in text if char.isalpha() and char not in "aeiouAEIOU")
    digits = sum(1 for char in text if char.isdigit())
    spaces = text.count(" ")
    
    # Indexing characters
    first_char = text[0] if char_count > 0 else None
    last_char = text[-1] if char_count > 0 else None
    first_word = text.split()[0] if word_count > 0 else None
    last_word = text.split()[-1] if word_count > 0 else None
    
    return {
        "char_count": char_count,
        "char_no_space": char_no_space,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "vowels": vowels,
        "consonants": consonants,
        "digits": digits,
        "spaces": spaces,
        "first_char": first_char,
        "last_char": last_char,
        "first_word": first_word,
        "last_word": last_word
    }
    
def print_report(text, stats):
    """Print a formatted analysis report."""
    preview = text[:50] + ("..." if len(text) > 50 else "")
    divider = "-" * 50
    
    print(f"\n{'=' * 50}")
    print(f"     TEXT ANALYSIS REPORT 📄")
    print(f"{'=' * 50}")
    print(f"  Preview :\"{preview}\"")
    print(f"{divider}")
    print(f"  Characters (total) : {stats['char_count']}")
    print(f"  Characters (no space) : {stats['char_no_space']}")
    print(f"  Words : {stats['word_count']}")
    print(f"  Sentences : {stats['sentence_count']}")
    print(divider)
    print(f"  Vowels : {stats['vowels']}")
    print(f"  Consonants : {stats['consonants']}")
    print(f"  Digits : {stats['digits']}")
    print(f"  Spaces : {stats['spaces']}")
    print(divider)
    print(f"  First Character : '{stats['first_char']}'")
    print(f"  Last Character : '{stats['last_char']}'")
    print(f"  First Word : '{stats['first_word']}'")
    print(f"  Last Word : '{stats['last_word']}'")
    print(f"  Reversed preview : \"{text[::-1][:30]}...\"")
    print(f"{'=' * 50}\n")
    
def main():
    """Main function to run the text analyser."""
    print("=" * 50)
    print("     TEXT ANALYSER 📄")
    print("=" * 50)
    
    example_text = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and elegant language!",
        "I have 3 cats, 2 dogs and 1 parrot at home.",
    ]
    
    while True:
        print("\n1. Analyze your own text")
        print("2. Analyze a preset example")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            user_text = input("\nEnter your text:\n").strip()
            if user_text:
                print_report(user_text, analyse_text(user_text))
            else:
                print("⚠ Please enter some text to analyze.")
        elif choice == "2":
            print("\nChoose an example text:")
            for i, ex in enumerate(example_text, 1):
                print(f"  {i}. {ex[:45]}...")
            ex = input("Choose an example (1-3): ").strip()
            if ex in ["1", "2", "3"]:
                print_report(example_text[int(ex)-1], analyse_text(example_text[int(ex)-1]))
            else:
                print("⚠ Invalid choice. Please choose 1, 2 or 3.")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️  Invalid choice!")
if __name__ == "__main__":
    main()