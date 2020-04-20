
# This is a number guessing game.
import random


def random_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        print("Welcome to the Number Guessing Game")
        print("Would you like to play on easy, medium, or hard level? Make a choice: ")

        set_level = True
        while set_level:
            level = input()
            if level == "easy":
                print("You've chosen the easy difficulty level")
                set_level = False
                break
            if level == "medium":
                print("You've chosen the medium difficulty level")
                set_level = False
                break
            if level == "hard":
                print("You've chosen the hard difficulty level")
                set_level = False
                break
            else:
                print("Invalid input!")
                print("Please type either easy, medium, or hard. ")


    # If the user selects Easy - 6 tries
        if level == 'easy':
            print("Because you selected easy, you'll have 6 tries to guess a number between 1-10.")
            guess_limit = 6
            while guess_limit != 0:
                guess = int(input("Guess a number: "))
                if guess == easy:
                    print("You got it right! ")
                    break
                else:
                    print("Wrong guess! Guess again")
                guess_limit -= 1
                print('You now have ' + str(guess_limit) + ' guesses left!')

                # If the user runs out of guesses
                if guess_limit == 0:
                    print("You've used all your available guessing power and still unable to guess right")
                    print('Game Over!')

    # If the user selects Medium - 4 tries
        if level == 'medium':
            print("Because you selected medium, you'll have 4 tries to guess a number between 1-20.")
            guess_limit = 4
            while guess_limit != 0:
                guess = int(input("Guess a number: "))
                if guess == medium:
                    print("You got it right! ")
                    break
                else:
                    print("Wrong guess! Guess again")
                guess_limit -= 1
                print('You now have ' + str(guess_limit) + ' guesses left!')

                # If the user runs out of guesses
                if guess_limit == 0:
                    print("You've used all your available guessing power and still unable to guess right")
                    print('Game Over!')

    # If the user selects Hard - 3 tries
        if level == 'hard':
            print("Because you selected hard, you'll have 3 tries to guess a number between 1-50.")
            guess_limit = 3
            while guess_limit != 0:
                guess = int(input("Guess a number: "))
                if guess == hard:
                    print("You got it right! ")
                    break
                else:
                    print("Wrong guess! Guess again")
                guess_limit -= 1
                print('You now have ' + str(guess_limit) + ' guesses left!')

                # If the user runs out of guesses
                if guess_limit == 0:
                    print("You've used all your available guessing power and still unable to guess right")
                    print('Game Over!')

        play_again = True
        while play_again:
            again = input("Would you care to play again? Yes or No ")
            if  again == 'No' or again == 'no':
                print('You Tried! See you again.')
                play_again = False
                play = False
            elif again == 'yes' or again == 'Yes':
                print("Let's start afresh then!")
                play_again = False
                play = True
            else:
                print('Please enter either yes or no.')
                input()
                play_again = False
                play = False


random_game()

