# ENGETO_PYTHON_PROJECT_2
## Project assignment
### Introduction
The goal of this project is to create a program that simulates the classic logic game "Bulls and Cows." After displaying an introductory message, the application allows the user to guess a secret four-digit number, evaluating the accuracy of each attempt.
### Requirements
1. The code must contain a header with the contact details of the author of the project.
2. The program greets the user and displays an introductory message.
3. The program then generates a secret 4-digit number (the digits must be unique and the number must not start with 0).
4. The player guesses the number. The program notices the player if the input is shorter or longer than 4 digits, contains duplicate digits, starts with 0 or includes non-numeric characters.
5. The program evaluates the user's guess.
6. The program displays the number of bulls (if the user guesses both the digit and its correct position) and cows (if the user guesses the correct digit but in the wrong position). The feedback must correctly reflect singular and plural forms — meaning "1 bull" / "2 bulls" and likewise for "1 cow / "2 cows".
7. The code should be organized into short and well-structured functions.

Example of introductory text:

    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    Enter a number:
    -----------------------------------------------
Gameplay example:

    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    Enter a number:
    -----------------------------------------------
    >>> 1234
    0 bulls, 2 cows
    -----------------------------------------------
    >>> 6147
    1 bull, 1 cow
    -----------------------------------------------
    >>> 2417
    3 bulls, 0 cows
    -----------------------------------------------
    >>> 2017
    Correct, you've guessed the right number
    in 4 guesses!
    -----------------------------------------------
    That's {amazing, average, not so good, ...}
