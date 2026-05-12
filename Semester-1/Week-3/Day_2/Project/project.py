# ============================================
#   STRING PROCESSOR 🔧
#   Week 3, Day 2 Project
# ============================================


def clean_text(text):
    """Strip and naormalise whitespace."""
    return " ".join(text.strip().split())

def word_stats(text):
    """Return word statistics."""
    words = clean_text(text).split()
    if not words:
        return {}
    return {
        "total"     : len(words),
        "unique"    : len(set(w.lower() for w in words)),
        "longest"   : max(words, key=len),
        "shortest"  : min(words, key=len),
        "avg_length": round(sum(len(w) for w in words) / len(words), 2)
    }
    
def transform_text(text, mode):
    """Transform text by mode."""
    modes = {
        "upper"    : text.upper(),
        "lower"    : text.lower(),
        "title"    : text.title(),
        "reverse"  : text[::-1],
        "no_vowels": "".join(c for c in text if c not in "aeiouAEIOU"),
        "no_spaces": text.replace(" ", ""),
        "slug"     : text.strip().lower().replace(" ", "-"),
    }
    return modes.get(mode, "⚠ Unknown mode")

def find_replace(text, find, replace):
    """Find and replace - returns result and count."""
    count = text.lower().count(find.lower())
    result = text.replace(find, replace)
    return result, count

def extract_info(text):
    """Extract key info from text."""
    words = text.split()
    return {
        "first_word"   : words[0],
        "last_word"    : words[-1],
        "char_count"   : len(text),
        "word_count"   : len(words),
        "has_digit"    : any(c.isdigit() for c in text),
        "has_upper"    : any(c.isupper() for c in text),
        "is_palindrome": (text.replace(" ", "") == text.replace(" ", "").lower()[::-1]),
        "is_pangram"   : set("abcdefghijklmnopqrstuvwxyz").issubset(set(text.lower())),
    }
    
def show_menu():
    """Display menu."""
    print(f"\n{'=' * 45}")
    print(f"         STRING PROCESSOR 🔧")
    print(f"{'=' * 45}")
    print("1. Clean text")
    print("2. Word statistics")
    print("3. Transform text")
    print("4. Find and replace")
    print("5. Extract info")
    print("6. Exit")
    print(f"{'=' * 45}")
    
def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("choose(1-6):").strip()
        
        if choice == "6":
            print("👋 Googbye!")
            break
        
        if choice not in("1", "2", "3", "4", "5"):
            print("⚠ Invalid choice. Try again.")
            continue
        
        text = input("\nEnter text:\n> ").strip()
        if not text:
            print("⚠ Please enter some text!")
            continue
        if choice == "1":
            print(f"\n Cleaned: \"{clean_text(text)}\"")
            
        elif choice == "2":
            s = word_stats(text)
            print(f"\n Total words   : {s['total']}")
            print(f" Unique words    : {s['unique']}")
            print(f"Longest word     : {s['longest']}")
            print(f"Shortest word    : {s['shortest']}")
            print(f"Average length   : {s['avg_length']}")
            
        elif choice == "3":
            print("\n Modes: upper | lower | title | reverse | no_vowels | no_spaces | slug")
            mode = input(" Choose mode:").strip()
            print(f"  Result: \"{transform_text(text, mode)}\"")
            
        elif choice =="4":
            find = input(" Find:").strip()
            replace = input(" Replace With: ").strip()
            result, count = find_replace(text, find, replace)
            print(f" Replaced {count} occurrence(s)")
            print(f" Result: \"{result}\"")
            
        elif choice == "5":
            info = extract_info(text)
            print()
            for key, value in info.items():
                print(f" {key:<15} : {value}")
            
if __name__ == "__main__":
    main()