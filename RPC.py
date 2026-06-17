import random

choices = ["Rock", "Paper", "Scissors"]

win_count = 0
loss_count = 0

# what beats what
beats = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

while True:
    computer = random.choice(choices)

    user_input = input(
        "\nSelect your weapon:\n"
        "1. Rock\n"
        "2. Paper\n"
        "3. Scissors\n"
        "4. Quit\n"
        "Choice: "
    )

    if user_input == "4":
        break

    if user_input not in ["1", "2", "3"]:
        print("Invalid input")
        continue

    user = choices[int(user_input) - 1]

    print(f"You: {user} | Computer: {computer}")

    if user == computer:
        print("Draw")

    elif beats[user] == computer:
        print("You win!")
        win_count += 1

    else:
        print("You lose!")
        loss_count += 1

    print(f"Score → Wins: {win_count}, Losses: {loss_count}")