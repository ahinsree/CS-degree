"""
📋 Project Specification:
Build a program that:

Adds income and expense transactions
Displays all transactions sorted by amount
Filters transactions by type (income/expense)
Calculates total income, total expenses, net balance
Finds largest and smallest transaction recursively
Generates a summary report

"""
"""
🗺️ Plan Before You Code:
STEP 1 → Data structure to store transactions
STEP 2 → add_transaction() — add income or expense
STEP 3 → get_total() — using *args or sum with lambda
STEP 4 → filter_by_type() — using filter + lambda
STEP 5 → sort_transactions() — using sorted + lambda
STEP 6 → find_largest() — recursive function
STEP 7 → generate_report() — combines all functions
STEP 8 → main() — menu-driven interface
"""

# ============================================
#   PERSONAL FINANCE TRACKER 💰
#   Week 2 Capstone Project
#   Combines: Functions, Scope, *args,
#   **kwargs, Lambda, map, filter,
#   sorted, Recursion
# ============================================

# ── Global data store ────────────────────────

transactions = [] # List to hold all transactions

# ── Core Functions ───────────────────────

def add_transaction(description, amount, **details):
    """
    Add a transaction to the tracker.
    description → what the transaction is
    amount      → positive = income, negative = expense
    **details   → any extra info (category, date, note)
    """
    transaction = {
        "description": description,
        "amount": amount,
        "type": "income" if amount > 0 else "expense",
        **details # Unpack additional details into the transaction dictionary
    }
    transactions.append(transaction) # Add to global list
    print(f"  ✅ Added: {description} → ₹{amount:,.2f}")

def get_total():
    """
    Calculate total income, total expenses, and net balance.
    
    """
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    net_balance = total_income + total_expenses # Expenses are negative
    return total_income, total_expenses, net_balance

def filter_by_type(transaction_type):
    """
    Filter transactions by type using filter + lambda.

    """
    return list(filter(lambda t: t["type"] == transaction_type, transactions))

def sort_transactions(by = "amount", reverse = False):
    """
    Sort transactions by a specified key using sorted + lambda.
    
    """
    return sorted(transactions, key=lambda t: abs(t[by]) if by == "amount" else t[by], reverse=reverse)

def find_largest(lst, index = 0, current_max = None):
    """
    Find largest transaction amount recursively.
    Uses recursion to traverse the list.
    
    """
    if index == len(lst): # Base case: reached end of list
        return current_max
    current = abs(lst[index]["amount"]) # Get absolute value for comparison
    if current_max is None or current > current_max:
        current_max = current
    return find_largest(lst, index + 1, current_max) # Recursive call for next index

def apply_tax(*amounts, tax_rate = 0.18):
    """
    Apply tax to multiple amounts using *args and lambda.
    Returns a list of amounts after tax.
    
    """
    return list(map(lambda a: round(a * (1 + tax_rate), 2), amounts)) # Apply tax to each amount

def generate_report():
    """
    Generate a full financial summary report.
    
    """
    if not transactions:
        print(" ⚠ No transactions yet!")
        return
    income, expenses, net = get_total()
    largest = find_largest(transactions)
    sorted_t = sort_transactions(by="amount", reverse=True)
    print(f"\n{'='*50}")
    print(f"    💰 FINANCIAL SUMMARY REPORT")
    print(f"{'='*50}")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Income: ₹{income:,.2f}")
    print(f"Total Expenses: ₹{expenses:,.2f}")
    print(f"Net Balance: ₹{net:,.2f}")
    print(f"Largest Transaction: ₹{largest:,.2f}")
    print(f"{'─' * 50}")
    for t in sorted_t:
        symbol = "+" if t["type"] == "income" else "-"
        print(f"  {t['description']:<20}"
              f"{t['type']:<10}"
              f"{symbol}₹{abs(t['amount']):>8,.2f}")
    print(f"{'='*50}")
    
def show_menu():
    """
    Display the main menu options.
    
    """
    print(f"\n{'='*50}")
    print(f"      PERSONAL FINANCE TRACKER💰")
    print(f"{'='*50}")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions(sorted)")
    print("4. View Income Only")
    print("5. View Expenses Only")
    print("6. Generate Report")
    print("7. Apply Tax Calculator")
    print("8. Exit")
    
def main():
    """
    Main program loop.
    
    """
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")
        
        if choice == "1":
            desc = input("Enter income description: ")
            amount = float(input("  Amount (₹): "))
            cat = input("  Category (optional): ")
            add_transaction(desc, abs(amount), category=cat if cat else "General")
            
        elif choice == "2":
            desc = input("Enter expense description: ")
            amount = float(input("  Amount (₹): "))
            cat = input("  Category (optional): ")
            add_transaction(desc, -abs(amount), category=cat if cat else "General")
            
        elif choice == "3":
            if not transactions:
                print(" ⚠ No transactions yet!")
                continue
            sorted_t = sort_transactions(by="amount", reverse=True)
            print(f"\n{'Description':<20} {'Type':<10} {'Amount':>10}")
            print(f"{'-'*42}")
            for t in sorted_t:
                symbol = "+" if t["type"] == "income" else "-"
                print(f"  {t['description']:<20}"
                      f"{t['type']:<10}"
                      f"{symbol}₹{abs(t['amount']):>8,.2f}")
            
        elif choice == "4":
            income = filter_by_type("income")
            if not income:
                print(" ⚠ No income transactions yet!")
            for t in income:
                print(f" ✅ {t['description']} → +₹{t['amount']:,.2f}")
                
        elif choice == "5":
            expenses = filter_by_type("expense")
            if not expenses:
                print(" ⚠ No expense transactions yet!")
            for t in expenses:
                print(f" ❌ {t['description']} → -₹{abs(t['amount']):,.2f}")
                
        elif choice == "6":
            generate_report()
            
        elif choice == "7":
            raw = input("Enter amounts separated by spaces: ")
            amounts = tuple(float(x) for x in raw.split())
            rate = input("Enter tax rate % (default 18%): ")
            tax_rate = float(rate) / 100 if rate else 0.18
            taxed = apply_tax(*amounts, tax_rate=tax_rate)
            print(f"   Original : {amounts}")
            print(f"   After Tax: {taxed}")
            
        elif choice == "8":
            print("  👋 Goodbye! Stay financially wise! 💰")
            break
        
    else:
        print(" ⚠ Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()