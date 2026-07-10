import random

print("Let's play Hangman!")

words = ["python", "apple", "computer", "banana"]

answer = random.choice(words)

guessed_letters = []

lives = 6

# this should show the display of the word
def show_word():
    display = ""
    for letter in answer:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

print(show_word())
print("Lives left:", lives)