# Task 1: Fix this function using global keyword

high_score = 0
def update_score(new_score):
    global high_score
    if new_score > high_score:
        high_score = new_score

update_score(85)
update_score(92)
update_score(78)
print(f"High Score: {high_score}")

# Task 2: Rewrite Task 1 WITHOUT using global
# Use return instead — which is better practice?

high_score = 0
def update_score(current_high, new_score):
    if new_score > current_high:
        return new_score
    return current_high

high_score = update_score(high_score, 85)
high_score = update_score(high_score, 92)
high_score = update_score(high_score, 78)

print(f"High Score: {high_score}")
      