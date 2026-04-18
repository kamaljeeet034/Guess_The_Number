import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def difficulty_level(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def check_answer(guessed_number,attempts,answer):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1

    elif guessed_number>answer:
        print("your guessed number is too high")
        return attempts-1

    else:
        print(f"your guess was right , the answer is {answer} ")
def game():
    print(logo_art.logo)
    print("choose difficulty level .. Type easy or hard")

    level = input("enter difficulty level: ")

    answer = random.randint(1,50)
    print(answer)

    attempts  = difficulty_level(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} to guess the number")
        guessed_number=int(input("enter your guess:"))
        attempts = check_answer(guessed_number,attempts,answer)
        if attempts == 0:
            print("you are out of guesses .. you loose")
            return

        elif guessed_number!=answer:
            print("guess again")
        else:
            return

game()