import random
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
n = random.randint(0, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(n)

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
for i in range(attempts):
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts to guess the number. Make a guess: "))
        attempts = attempts - 1
        if guess < n:
            print("Too low.")
        elif guess > n:
            print("Too high.")
        else:
            print("You got it!")
            attempts = 0
print("Game over!")


