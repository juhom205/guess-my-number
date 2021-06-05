
import random

attempts_list = []
print("-------------")
print("Made by juhom")
print("-------------")

def show_score():
    if len(attempts_list) <= 0:
        print("There is no high score.Take it or leave")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))


def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello explorer! Welcome to guess my number.")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to guess my number? (Yes/No) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number between 1 and 10")
            if int(guess) == random_number:
                print("Congrats you guessed my number!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("Understandable, have a great day!")
                    break
            elif int(guess) > random_number:
                print("My number is lower :>")
                attempts += 1
            elif int(guess) < random_number:
                print("My number is higher :>")
                attempts += 1
        except ValueError as err:
            print("Do you think I'm stupid? That is not a valid input...")
            print("({})".format(err))
    else:
        print("Understandable, have a great day!")


if __name__ == '__main__':
    start_game()
