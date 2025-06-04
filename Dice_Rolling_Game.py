import random

def roll_dice():
    return random.randint(1, 6)

def play_round(round_num):
    input(f"\n Round {round_num} - Press Enter to roll your die...")

    user_roll = roll_dice()
    computer_roll = roll_dice()

    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {computer_roll}")

    if user_roll > computer_roll:
        print("You win this round!")
        return "user"
    elif user_roll < computer_roll:
        print("Computer wins this round!")
        return "computer"
    else:
        print("It's a tie!")
        return "tie"

def play_game():
    print("Welcome to the Dice Rolling Game!")
    rounds = 5
    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        winner = play_round(round_num)
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

    print("\n🏁 Final Result:")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry, the computer won this time.")
    else:
        print("It's a tie overall!")

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
