import random
#import the fruits from words.py.
from words import fruits
#import the hangman_stages from stagen.py
from stages import hangman_stages
#create random_word that store the chosen word from fruits list.
random_word = random.choice(fruits).lower()
print(random_word)
#we do not want the user to see the word,so we hide it. 
hidden_word = ['_'] * len(random_word)
lives = 6
#welcome message.
print("Welcome to Hangman !")
print(' '.join(hidden_word))
game_over = False
#create a loob to check if the guessed letter in the random word.
while not game_over and lives > 0:
    guessed_letter = input("guess a letter:").lower()
    if guessed_letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guessed_letter:
                hidden_word[i] = guessed_letter
    else:
        lives -= 1
        print(hangman_stages[6 - lives])

    print(' '.join(hidden_word))
    print("Lives:", lives)

    if '_' not in hidden_word:
        print("Congratulations! You guessed the word correctly!")
        game_over = True
    if lives == 0:
        print("Game over! You ran out of lives.")
        print("The word was:", random_word)
        game_over = True