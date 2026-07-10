import random

print("Let's play Hangman!")

word_bank = ["python", "apple", "computer", "banana"]

answer = random.choice(word_bank)

guessed_letters = []

lives = 6

# this should show the display of the word
def display_word():
    display = ""
    for letter in answer:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

print(display_word())

print("Lives left:", lives)

while lives > 0:
    guess = input("Guess a letter: ").upper()
    if len(guess)!= 1 and guess != answer:
        print("invalid answer")
