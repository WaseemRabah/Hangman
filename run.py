import random
from colorama import Fore, Style
from words import fruits
from stages import hangman_stages


"""display the Hangman menu options"""
def display_menu():
    print(Fore.MAGENTA + "Hangman Menu:")
    print(Fore.BLUE + "1.Instructions")
    print(Fore.YELLOW + "2. Play")
    print(Fore.RED + "3. Quit" + Style.RESET_ALL)

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
    hidden_word = ['_'] * len(random_word)
    lives = 6
    stage_index = 0
    print(Fore.GREEN + "Welcome to Hangman!" + Style.RESET_ALL)
    print(' '.join(hidden_word))
    game_over = False
    guessed_letters = set()
    while not game_over and lives > 0:
        guessed_letter = input("Guess a letter: ").lower()
        if guessed_letter in guessed_letters:
            print(Fore.YELLOW + f"You have already guessed '{guessed_letter}' and it was incorrect!" + Style.RESET_ALL)
            continue
        guessed_letters.add(guessed_letter)
        if guessed_letter in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guessed_letter:
                    hidden_word[i] = guessed_letter
        else:
            lives -= 1
            stage_index += 1
            print(Fore.RED + "Wrong letter...Try Again" + Style.RESET_ALL)
            print(hangman_stages[stage_index])
        print(' '.join(hidden_word))
        print("Lives:", lives)
        if '_' not in hidden_word:
            print("Congratulations! You guessed the word correctly!")
            game_over = True
        if lives == 0:
            print("Game over! You ran out of lives.")
            print("The word was:", random_word)
            game_over = True


def main():
    """
    The main function that controls the Hangman game's flow.

    1. Enter an infinite loop to keep the game running until the player chooses to quit.
    2. Display the main menu using the display_menu() function.
    3. Ask the player to enter their choice (1, 2, or 3) for instructions, play, or quit.
    4. If the player chooses '1', call the display_instructions() function to show the game instructions.
    5. If the player chooses '2', call the play_hangman() function to start playing the Hangman game.
    6. If the player chooses '3', print a farewell message and exit the loop to end the game.
    7. If the player enters an invalid choice, display an error message and prompt them to choose again.
    8. Repeat the loop to keep the game running until the player chooses to quit.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            display_instructions()
        elif choice == '2':
            play_hangman()
        elif choice == '3':
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()