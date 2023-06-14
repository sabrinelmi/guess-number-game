import random


class TheGame:
    @staticmethod
    def guess_number(guess, number):
        if guess < number:
            return "Too low"
        elif guess > number:
            return "Too high"
        else:
            return "Correct"

    # number of guess:
    @staticmethod
    def make_limits():
        min_guess = random.randint(0, 50)
        max_guess = random.randint(51, 150)
        return min_guess, max_guess


class Player(TheGame):
    def play_game(self):
        total_guess = 10
        min_guess, max_guess = self.make_limits()
        # guess the number input;
        number = random.randint(min_guess, max_guess)

        while total_guess > 0:
            print("Total guesses left: ", total_guess)
            guess = input("Guess a number : ")

            # make it accept int, and float
            try:
                guess = float(guess)
            except ValueError:
                print("Not a valid number, please try again.")
                continue

            # make the maximum and minimum no.for the player
            if guess < min_guess or guess > max_guess:
                print(f"Use numbers between {min_guess} and {max_guess}")
                continue

            answer = self.guess_number(guess, number)
            print(answer)
            total_guess -= 1
            if answer == "Correct":
                print("You win!")
                return True

        if total_guess == 0:
            print("sorry You have run out of guesses")
            print(f"The right answer was {number} :")
            return False

    def play_again(self):
        # ask the player to play again
        response = input("Do you want to play again (y/n): ")
        if response == "n":
            print('Thanks for playing! Bye')
            return False
        elif response == 'y':
            return True
        else:
            print('That was not a legal answer. Try again.')


if __name__ == "__main__":
    try:
        player = Player()
        while True:
            if not player.play_game():
                break
            if not player.play_again():
                break

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting the game.")

print("Game ended.")
