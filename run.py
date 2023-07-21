import random
from words import fruits
from stages import hangman_stages

"""display the Hangman menu options"""
def display_menu():
    print("Hangman Menu :")
    print("1.Instructions")
    print("2.Play")
    print("3.Quit")

"""display hangman instructions"""
def display_instructions():
    print("Hangman is a word guessing game.")
    print("A random word will be chosen from fruits list, and you have to guess the letters.")
    print("You have 6 lives. Each incorrect guess will cost you a life.")
    print("Guess all the letters in the word to win!")

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
    guessed_letter = input("guess a letter:\n").lower()
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

