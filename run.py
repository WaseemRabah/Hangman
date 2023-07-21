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

def play_hangman():
    """
    Play the Hangman game.
    
    1. Choose a random word from the list of fruits and convert it to lowercase.
    2. Create a list of underscores to represent the hidden word's letters.
    3. Initialize the number of lives the player has to 6.
    4. Print the welcome message and the initial state of the hidden word.
    5. Enter the game loop until the game is over or the player runs out of lives.
    6. Ask the player to guess a letter and convert it to lowercase.
    7. Check if the guessed letter is in the random word.
        - If the letter is correct, update the hidden word to reveal the guessed letter's position(s).
        - If the letter is incorrect, decrease the player's lives and display the corresponding hangman stage.
    8. Display the current state of the hidden word and the remaining lives.
    9. Check if the player has guessed all the letters correctly (no more underscores).
        - If so, print a victory message and set game_over to True.
    10. Check if the player has run out of lives (lives == 0).
        - If so, print a game over message along with the correct word, and set game_over to True.
    11. Repeat the game loop until the game is over.
    """
    random_word = random.choice(fruits).lower()
    print(random_word)
    hidden_word = ['_'] * len(random_word)
    lives = 6
    print("Welcome to Hangman !")
    print(' '.join(hidden_word))
    game_over = False
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

