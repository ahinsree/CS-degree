# Search Method

# ── find() — returns index, -1 if not found ──

text = "Hello, Python is great!. Python rocks!"
print(text.find("Python"))
print(text.find("Python", 10))  # Start searching from index 10
print(text.find("Java"))  # Not found, returns -1

# ── index() — same but RAISES ValueError ─────

print(text.index("Python"))
# print(text.index("Java"))     # ❌ ValueError — crashes!

# ── When to use which ────────────────────────
# find()  → when NOT finding is acceptable → check for -1
# index() → when it MUST exist → crash loudly if missing

# ── rfind() — search from RIGHT ──────────────
print(text.rfind("Python"))  # Finds last occurrence
print(text.rfind("o"))      # 35  ← last 'o'

# ── count() ──────────────────────────────────
print(text.count("Python"))     # 2
print(text.count("o"))          # 4
print(text.count("is"))         # 1

# ── startswith() & endswith() ────────────────
print(text.startswith("Hello"))    # True
print(text.startswith("Python"))   # False
print(text.endswith("rocks!"))     # True
print(text.endswith("great."))     # False

filename = "report.pdf"
if filename.endswith((".pdf", ".PDF", ".docx")):
    print("✅ Valid document")
    
# works with startswith too!
if filename.startswith(("rep", "Sum", "doc")):
    print("✅ Vailid filename prefix")
    
# ── in operator — simplest existence check ───
print("Python" in text)  # True
print("Java" in text)    # False
print("python" in text)  # False ← case sensitive!
print("python" in text.lower())  # True ← fix with lower()