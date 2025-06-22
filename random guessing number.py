import random

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 15

print("Guess a number between 1 and 100")

while attempts < 15:
    try:
        guess = int(input("Enter your guessing number: "))
        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break
        elif guess < number_to_guess:
            print("TRY AGAIN! THE NUMBER IS TOO LOW.")
        else:
            print("TRY AGAIN! THE NUMBER IS TOO HIGH.")
    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts:
    print(f"The correct number was {number_to_guess}.")
