import random


def guess_number(guess, number):
    if guess < number:
        return "Too low"
    elif guess > number:
        return "Too high"
    else:
        return "Correct"


# game rules

# number of guess:
def make_limits():
    min_guess = random.randint(0, 50)
    max_guess = random.randint(51, 150)
    return min_guess, max_guess


#
# game_is_running = True
while __name__ == "__main__":
    total_guess = 10
    min_guess, max_guess = make_limits()
    # guess the number input;
    number = random.randint(min_guess, max_guess)
    while total_guess > 0:
        print("Total guesses left: ", total_guess)
        guess = input("Guess a number : ")
        # make it accept int, and float
        if guess.replace(".", "", 1).isdigit():
            guess = float(guess)
        else:
            print("Not a valid number, please try again.")
            continue
        # make the maximum and minimum no.for the player
        if guess < min_guess or guess > max_guess:
            print(f"Use numbers between {min_guess} and {max_guess}")
            continue

        answer = guess_number(guess, number)
        print(answer)
        total_guess -= 1
        if answer == "Correct":
            print("You win!")
            break

    if total_guess == 0:
        print("sorry You have run out of guesses")
        print(f"The right answer was {number} :")
    # ask the player to play again
    while True:
        play_again = input("Do you want to play again (y/n): ")
        if play_again == "n":
            print('Thanks for playing! Bye')
            game_is_running = False
            break
        if play_again == 'y':
            break
        else:
            print('That was not a legal answer. Try again.')
