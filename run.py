import random
#import the fruits from words.py.
from words import fruits
#create random_word that store the chosen word from fruits list.
random_word = random.choice(fruits).lower()
print(random_word)
#we do not want the user to see the word,so we hide it. 
hidden_word = ['_'] * len(random_word)
lives = 5
#welcome message.
print("Welcome to Hangman !")
print(' '.join(hidden_word))
#create guessed_letter that take the value from the user.
guessed_letter = input("guess a letter:").lower()