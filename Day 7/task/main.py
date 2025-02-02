import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

chosen_word = random.choice(word_list)
print(chosen_word)

def check_guess_in_chosen_word(guess: str, chosen_word: str, pattern: str):
    display = [ch for ch in pattern]
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    pattern = ''.join(display)
    return pattern


# USer can iteratively guess a letter
# User has len(chosen_word) number of guesses
# If all guesses exhaust, user loses

# Store in memory the guessed pattern
# Update the pattern on every right guess

pattern = ""
for position in range(len(chosen_word)):
    pattern += "_"
print(pattern)

attempts = len(chosen_word)
win = False
while attempts > 0:
    attempts -= 1
    guess = input("Guess a letter: ").lower()
    print(guess)
    pattern = check_guess_in_chosen_word(guess, chosen_word, pattern)
    print(pattern)
    if "_" not in pattern:
        print("You Win!")
        win = True
        break

if not win:
    print("You Lose!")
