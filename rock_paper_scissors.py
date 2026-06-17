import random

emojis = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}
choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")