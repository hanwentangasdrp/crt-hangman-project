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

#check for letters
if len(guess)!= 1:
        print("Invalid input. Please enter one letter.")
        continue
        print("You've already guessed this. '{guessed}' Try a different letter.")
        continue 
    

# add validity 
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
