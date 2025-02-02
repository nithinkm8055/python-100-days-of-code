import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

computer_guess = random.randint(1,101)
print(f"Computer guessed: {computer_guess}")

lower_limit = 1
upper_limit = 100

level_dict = {
    "easy": 10,
    "hard": 5,
}

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level not in level_dict:
    exit(1)

num_attempts = level_dict[difficulty_level]
print(f"You have {num_attempts} remaining to guess the number")

guessed = False
while num_attempts > 0:
    guess = int(input("Guess a number"))
    if guess == computer_guess:
        print("You win")
        guessed = True
        break
    elif guess < computer_guess:
        print("Too Low")
        print("Guess Again")
    else:
        print("Too High")
        print("Guess Again")
    num_attempts -= 1
    print(f"You have {num_attempts} remaining to guess the number")

if not guessed:
    print("You Lose")