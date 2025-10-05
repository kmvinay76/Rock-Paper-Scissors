import random

game = {1: "rock🪨", 2: "paper🗞️", 3: "scissor✂️"}
revesgame = {"rock": 1, "paper": 2, "scissor": 3}

user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors Game 🎮")
print("Type 'end' anytime to stop playing.\n")

while True:
    user_input = input("Enter your choice [rock, paper, scissor] or 'end' to quit: ").lower()
    if user_input == "end":
        print("\nHave a nice day... 😁")
        break
    if user_input not in revesgame:
        print("Invalid choice, please try again!")
        continue

    user_choice = revesgame[user_input]
    computer = random.choice([1, 2, 3])

    print(f"\nYou chose {game[user_choice]} and computer chose {game[computer]}")

    if user_choice == computer:
        print("It's a draw!")
    elif (user_choice == 1 and computer == 3) or \
         (user_choice == 2 and computer == 1) or \
         (user_choice == 3 and computer == 2):
        print("You win! 🎉")
        user_score += 1
    else:
        print("Computer wins! 🤖")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}\n")

print("\nFinal Result:")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")
if user_score > computer_score:
    print("🏆 YOU WON THE GAME!")
elif user_score < computer_score:
    print("💻 COMPUTER WON THE GAME!")
else:
    print("😅 It's a tie overall!")