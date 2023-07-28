# The Hangman Game

![Responsive Mockup](documentation/hangman-responsive.png)

*The link to [the Hangman Game](https://hangmanap-507a8f5d3e20.herokuapp.com/)*

The Hangman game is a classic word guessing game where a player tries to guess a hidden word by suggesting letters one at a time. The game's name comes from the graphical representation of incorrect guesses, which gradually builds up a stick figure of a "hanged" man.

---

## How to play:

  1. Click this *[link](https://hangmanap-507a8f5d3e20.herokuapp.com/)* or copy this text: `https://hangmanap-507a8f5d3e20.herokuapp.com/` and paste it in your browser's address bar.
  1. As soon as the page is loaded, click 'RUN PROGRAM'.
  1. Press number 1 and then hit Enter to load the instructions.
  1. Press number 2 and then hit Enter to start the game.
  1. The game selects a random word from a predefined list of words.
  1. The chosen word is represented by a series of underscores, with each underscore indicating a letter in the word.
  1. The player has a limited number of attempts (lives) to guess the letters in the word.
  1. On each turn, the player guesses a letter. If the letter is present in the word, all occurrences of that letter are revealed in the hidden word.
  1. If the guessed letter is not in the word, the player loses a life, and a part of the Hangman is drawn on the screen.
  1. The game continues until the player guesses the entire word or runs out of lives.
  1. If the player successfully guesses the word before running out of lives, they win the game.
  1. If the player runs out of lives before guessing the word, the game ends, and the correct word is revealed.


---

## User Stories
### First Time Visitor Goals:
* As a first-time visitor, I want to understand the rules and gameplay of the Hangman game, so I can quickly get started without confusion.
* As a new player, I want clear instructions on how to guess letters and the consequences of incorrect guesses, so I can strategize and maximize my chances of winning.
* As a player unfamiliar with the game's words, I hope the game provides a varied and interesting selection of words to guess, making the gameplay engaging and enjoyable.
* As a user trying out the game for the first time, I expect an intuitive and easy-to-navigate menu that allows me to choose between viewing instructions, playing the game, or quitting.
* As a new player, I hope the game warns me if I repeat an incorrect letter guess, so I can avoid losing lives unnecessarily and improve my chances of winning.
* As a player experiencing the Hangman game for the first time, I look forward to celebrating my victories and receiving clear messages when I win or lose the game.
* As a user playing the game for the first time, I expect the game to maintain a fair level of challenge, ensuring that it's not too easy or too difficult to guess the hidden words.

### Frequent Visitor Goals:
* As a returning player, I expect the game to provide regular updates with new word lists, bug fixes, and feature enhancements, keeping the game fresh and engaging over time.
* As a frequent visitor, I look forward to unlocking achievements or earning rewards based on my performance, providing additional motivation to keep playing and improving. 

---

## Features

 **When the program is loaded**

The user can see the hangman menu and he can choose from:
![loading Program](documentation/loaded.png)

**When the user choose instructions.**
- The instructions will shows up;
![Instructions](documentation/instructions.png)

**When the user choose play.**
- The game will start;
![Play](documentation/play.png)

**When the user chose "Quit"**
The user will see a goodbye message, and the program will be stopped.
![Quit](documentation/quit.png)

---

## Flowchart

The flowchart represents the logic of the application:

  ![Flash Card Page](documentation/flowchart.png)

---

## Technologies Used

### Languages:

- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.

##### Third-party imports:

- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [GitHub](https://github.com/) was used to host the code of the website.
- [heroku.com](https://www.heroku.com/) was used to deploy the project.


---
