#hangman to do list

#1. get a list to display the handed figure at different states.
#2. end the game when either the personn gets the word, or the figure is complete
import random


# Load words from file
word_list = []

with open("hangman.txt", "r") as file:
    for line in file:
        word_list.append(line.strip())

answer = random.choice(word_list).lower()

# Create hidden word
revealed = ["_"] * len(answer)

# Game state
lives = 10
guessed_letters = set()
is_playing = True

print("\nWelcome to Hangman!")

while is_playing:

    print("\n" + "*" * 25)
    print("Word:", " ".join(revealed))
    print(f"Lives remaining: {lives}")
    print("*" * 25)

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1:
        print("Please enter exactly one letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Correct guess
    if guess in answer:

        print(f"'{guess}' is in the word!")

        for i in range(len(answer)):
            if answer[i] == guess:
                revealed[i] = guess

        if "_" not in revealed:
            print("\nWord:", "".join(revealed))
            print("🎉 You win!")
            is_playing = False

    # Incorrect guess
    else:
        lives -= 1

        print(f"'{guess}' is not in the word.")

        if lives == 0:
            print(f"\nYou lose. The word was '{answer}'.")
            is_playing = False



