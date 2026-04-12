#  Combining All Parameter Types

# Order: regular → *args → keyword-only → **kwargs
def full_function(pos1, pos2, *args, key1 = "default", **kwargs):
    print(f"pos1   = {pos1}")
    print(f"pos2   = {pos2}")
    print(f"args   = {args}")
    print(f"key1   = {key1}")
    print(f"kwargs = {kwargs}")
    
full_function("A", "B",
              "C", "D", "E",
              key1 = "custom",
              extra1 = "F",
              extra2 = "G"
              )

# Memory rule:
"""def func(normal, *args, keyword=default, **kwargs)
          ↑         ↑          ↑               ↑
       regular   tuple       string           dict"""
       
       
# Practical example:
def send_email(to, subject, *cc, urgent = False, **headers):
    """
    send an email with flexible parameters.
    to      → required recipient
    subject → required subject
    *cc     → any number of CC recipients
    urgent  → optional flag
    **headers → any extra email headers
    """
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"CC: {cc}")
    print(f"Urgent: {urgent}")
    print(f"Headers: {headers}")
    print("─────────────────")
    
send_email(
    "alice@example.com",
    "Meeting Tomorrow",
    "bob@example.com", "charlie@example.com",
    urgent=True,
    reply_to="noreply@example.com",
    priority="high"
)