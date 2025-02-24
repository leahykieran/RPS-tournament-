from bot import Bot, RPS


class RPSGame:
    def __init__(self, bot=None):
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.bot: Bot = Bot("BOT") if not bot else bot
        self.player_choice = None
        self.computer_choice = None
        print("Game is starting...")

    def player_input(self):
        while True:
            try:
                choice = int(input("Enter your choice: 1. Rock 2. Paper 3. Scissors\n"))
                if choice in (1, 2, 3):
                    self.player_choice = RPS(choice)
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def computer_input(self):
        self.computer_choice = self.bot.next_move()

    def check_winner(self):
        print(f"You chose: {self.player_choice}, Computer chose: {self.computer_choice}")
        if self.player_choice == self.computer_choice:
            self.tie_score += 1
            print("It's a tie!")
        elif (self.player_choice == RPS.ROCK and self.computer_choice == RPS.SCISSORS) or \
             (self.player_choice == RPS.PAPER and self.computer_choice == RPS.ROCK) or \
             (self.player_choice == RPS.SCISSORS and self.computer_choice == RPS.PAPER):
            self.player_score += 1
            print("You win!")
        else:
            self.computer_score += 1
            print("Computer wins!")

    def play(self):
        while True:
            self.player_input()
            self.computer_input()
            self.check_winner()
            print(f"Score - Player: {self.player_score}, Computer: {self.computer_score}, Ties: {self.tie_score}")
            play_again = input("Do you want to play again? (Y/N): ").strip().lower()
            if play_again != 'y':
                print("Game Over. Thanks for playing!")
                break


if __name__ == "__main__":
    game = RPSGame()
    game.play()
    input("Press Enter to exit...")
    

