#Number guessing game
import random
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
number_guessing_game()