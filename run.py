import random
from words import fruits
from stages import hangman_stages

def display_menu():
    print("Hangman Menu:")
    print("1. Instructions")
    print("2. Play")
    print("3. Quit")

def display_instructions():
    print("Hangman is a word guessing game.")
    print("A random word will be chosen, and you have to guess the letters.")
    print("You have 6 lives. Each incorrect guess will cost you a life.")
    print("Guess all the letters in the word to win!")

def play_hangman():
    random_word = random.choice(fruits).lower()
    hidden_word = ['_'] * len(random_word)
    lives = 6
    print("Welcome to Hangman!")
    print(' '.join(hidden_word))
    game_over = False

    while not game_over and lives > 0:
        guessed_letter = input("Guess a letter: ").lower()
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

def main():
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
