import random

number = random.randint(1, 100)
guesses = 0

print("Welcome to the guessing game")
print("I am thinking of a number between 1 and 100")


while True:
    try:
        user_input = int(input("Enter your guess: "))
        guesses += 1

        if user_input > number:
            print("too high!")
        elif user_input < number:
            print("too low!")
        else:
            print(f"you guessed correctly in {guesses} tries!")
            break

    except ValueError:
        print("Please enter a valid number")