from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
print(number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

continue_game = True
while continue_game:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess != number:
        attempts -= 1
        if attempts > 0:
            if guess > number:
                print("Too high")
            if guess < number:
                print("Too low")
        else:
            continue_game = False
            print("You've run out of guesses. Refresh the page to run again")
    else:
        print(f"You got it! The answer was {guess}")
        continue_game = False







#As long as user hasn't guessed correct or still has guesses:
#Let the user make guesses

#When a user guesses wrong deduct attempt from total attempts and give feedback

#When user guessed correct, end game and let them know the correct answer

#When user out of guesses, let them know