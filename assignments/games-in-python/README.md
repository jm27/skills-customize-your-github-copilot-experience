
# 📘 Assignment: Games in Python — Hangman

## 🎯 Objective

Build a playable Hangman game that reinforces Python fundamentals: strings, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Word Setup and Selection

#### Description
Create the game foundation by preparing the word bank and picking a random secret word each round.

#### Requirements
Completed program should:

- Define a list of at least 10 school-appropriate words.
- Randomly select one word at the start of the game; store it in a consistent case (e.g., lowercase).
- Initialize the masked word display using underscores or dashes to match the word length.
- Store and display the number of attempts the player has left.


### 🛠️ Gameplay Loop and Outcomes

#### Description
Implement the interactive loop where players guess letters, track progress, and see clear win/lose results.

#### Requirements
Completed program should:

- Prompt for single-letter guesses until the player wins or runs out of attempts.
- Reject invalid input (non-letters, repeats) with a friendly message and do not consume an attempt.
- Reveal correctly guessed letters in all matching positions in the masked display.
- Track incorrect guesses, decrement remaining attempts, and show guessed letters so far.
- End the game with a win message when the word is fully revealed or a lose message that shows the correct word.
