import random

number = random.randint(1, 100)
chances = 10

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. You have 10 chances to guess it.\n")

while chances > 0:
    guess = input("Enter your guess (between 1 and 100): ")

    if not guess.isdigit():
        print("Please enter a valid number.\n")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.\n")
        continue

    if guess == number:
        print(f"Congratulations! You guessed the number correctly: {number}")
        break
    elif guess < number:
        chances -= 1
        print("Too low! Try again.")
    else:
        chances -= 1
        print("Too high! Try again.")

    if chances > 0:
        print(f"Chances left: {chances}\n")

if chances == 0:
    print(f"Sorry! You have used all your chances. The correct number was {number}.")