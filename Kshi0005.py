import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < lower_bound or guess > upper_bound:
                print(f" Guess a number within the range {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("its low, Try again.")
            elif guess > secret_number:
                print("Its high, Try again.")
            else:
                print(f"Congratulations! You took {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    number_guessing_game()
