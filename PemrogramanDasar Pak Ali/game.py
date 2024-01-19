import random

target = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < target:
        print("Try a higher number.")
    elif guess > target:
        print("Try a lower number.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break