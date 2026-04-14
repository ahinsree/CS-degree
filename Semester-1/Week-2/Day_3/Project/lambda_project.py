# ============================================
#   STUDENT DATA PIPELINE 📊
#   Lambda + map + filter + sorted
# ============================================

students = [
    {"name": "Alice",   "grade": 92, "age": 20},
    {"name": "Bob",     "grade": 65, "age": 22},
    {"name": "Charlie", "grade": 85, "age": 19},
    {"name": "David",   "grade": 71, "age": 21},
    {"name": "Eve",     "grade": 95, "age": 20},
    {"name": "Frank",   "grade": 58, "age": 23},
]

def main():
    print("=" * 45)
    print("     STUDENT DATA PIPELINE 📊")
    print("=" * 45)

    # Step 1: Filter — keep only passing students (grade >= 70)
    passing = list(filter(lambda s: s["grade"] >= 70, students))
    print(f"\n✅ Passing students ({len(passing)}):")
    for s in passing:
        print(f"   {s['name']}: {s['grade']}")

    # Step 2: Map — add letter grade to each passing student
    def add_letter(s):
        grade = s["grade"]
        letter = (lambda g:
            "A" if g >= 90 else
            "B" if g >= 80 else
            "C" if g >= 70 else "F"
        )(grade)
        return {**s, "letter": letter}

    graded = list(map(add_letter, passing))

    # Step 3: Sort — by grade descending
    ranked = sorted(graded, key=lambda s: s["grade"], reverse=True)

    print(f"\n🏆 Final Rankings:")
    print("-" * 45)
    for i, s in enumerate(ranked, 1):
        print(f"  {i}. {s['name']:<10} "
              f"Grade: {s['grade']}  "
              f"Letter: {s['letter']}")
    print("=" * 45)

if __name__ == "__main__":
    main()