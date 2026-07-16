# Project Members: Hanwen Tang, Veer Sharma, Megan Shaw, Aidan Cheng

import random

print("Let's play Hangman!")

word_bank = ["python", "apple", "computer", "banana"]

answer = random.choice(word_bank)

guessed_letters = []

lives = 6


def display_word():
    display = ""
    for letter in answer:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

while lives > 0:

    print(display_word())
    print("Lives left:", lives)

    guess = input("Guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed this. Try a different letter.")
        continue


    guessed_letters.append(guess)

    if guess in answer:
        print("Correct!")
    else:
        print("Letter not found!")
        lives -= 1

    if "_" not in display_word():
        print(display_word())
        print("You won!")
        break

if lives == 0:
    print("Out of lives, game over!")
    print("The word was:", answer)
