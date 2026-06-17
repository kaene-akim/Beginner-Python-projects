import random

answer = random.randint(0, 100)

lives = 10
attempts = 0

low = 0
high = 100

print("Welcome to the Number Guessing Game!")

while True:
    print(f"\nLives: {lives}")
    print(f"Guess a number between {low} and {high}")

    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < low or guess > high:
        print(f"Please choose a number between {low} and {high}.")
        continue

    attempts += 1

    if guess == answer:
        print(f"\n🎉 You win! The number was {answer}.")
        print(f"You found it in {attempts} guesses.")
        break

    lives -= 1

    if guess < answer:
        print("Too low!")
        low = max(low, guess + 1)

    else:
        print("Too high!")
        high = min(high, guess - 1)

    if lives == 0:
        print(f"\n💀 You lose! The number was {answer}.")
        break