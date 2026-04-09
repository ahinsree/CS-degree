# ============================================
#   SCOPE EXPLORER 🔭
#   Week 2, Day 2 Project
#   Demonstrates all scope concepts
# ============================================

# ── Global variables ─────────────────────────
app_name = "Scope Explorer"
version = "1.0"
total_run = 0

def show_app_info():
    """Reads global variables — no issue."""
    print(f"\n{app_name} v{version}")
    print("=" * 30)
    
def run_demo(demo_name):
    """Increment global counter."""
    global total_run
    total_run += 1
    print(f"\n{total_run}: {demo_name}")
    print("-" * 30)

# ── Demo 1: Local scope ───────────────────────
def demo_local():
    run_demo("Local Scope")
    local_var = "I only exist here!"
    print(f"local_var: {local_var}")
    print("✅ Local_var accessible inside function")
    
# ── Demo 2: Global read ───────────────────────
def demo_global_read():
    run_demo("Global Read")
    print(f"app_name: = {app_name}")
    print("✅ Global variables are readable everywhere")

# ── Demo 3: LEGB rule ────────────────────────
def demo_legb():
    run_demo("LEGB Rule")
    x = "enclosing"
    def inner():
        x = "local"
        print(f"inner sees x:'{x}'")
        
    inner()
    print(f"outer sees x:'{x}'")
    print(f"global sees app_name:'{app_name}'")

# ── Demo 4: nonlocal ─────────────────────────
def demo_nonlocal():
    run_demo("Nonlocal Keyword")
    count = 0
    def increment():
        nonlocal count
        count += 1
        
    increment()
    increment()
    increment()
    print(f"count after three increment = {count}")
    
# ── Main ──────────────────────────────────────
def main():
    show_app_info()
    demo_local()
    demo_global_read()
    demo_legb()
    demo_nonlocal()
    
    divider = "=" * 30
    print(f"\n{divider}")
    print(f"Total demo runs: {total_run}")
    print(f"{divider}")    
if __name__ == "__main__":
    main()
    