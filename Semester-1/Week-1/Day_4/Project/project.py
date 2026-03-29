import random
print("=" * 40)
print("      NUMBER GUESSING GAME 🎮")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
print("I'm thinking of a number between 1 and 100. Can you guess it?")
print(f"You have {max_attempts} attempts. Good luck!")
print("-" * 40)
while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"🎉Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("📈Too Low! Try again.")
    else:
        print("📉Too High! Try again.")
    remaining_attempts = max_attempts - attempts
    if remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts Left.")
    else:
        print(f"❌ Out of attempts! The secret number was {secret_number}. Better luck next time!")
    print("-" * 40)
        