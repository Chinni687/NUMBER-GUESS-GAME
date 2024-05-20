import random
EASY_LEVEL_ATTEMPTS=20
HARD_LEVEL_ATTEMPTS=10
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is correct.... the answer {answer}")

def game():
    print("Let me think of a number between 1 to 250")
    answer=random.randint(1,50)
    print(answer)
    level=input("Choose level of difficulty...Type 'easy' or 'hard': ")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:  
        print(f"you have {attempts} attempts remaining to guess the number")
        guessed_number=int(input("Guess a number: "))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses... You lose!")
            return 
        elif guessed_number!=answer:
            print("Guess again....")



game()