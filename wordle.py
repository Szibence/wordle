# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:07:10 2024

@author: szibence
"""

import random


def print_color(text, color, end='\n'):
    """
    Print text in a given color.

    Parameters
    ----------
    text : str
        Text to print.
    color : str
        Color to use. Must be one of the following:
        - "red"
        - "green"
        - "yellow"
        - "blue"
        - "purple"
        - "cyan"
        - "white"

    Returns
    -------
    None.

    """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m"
    }

    if color not in colors:
        raise ValueError("Invalid color. Must be one of: red, green, yellow, blue, purple, cyan, white")

    print(colors[color] + text + "\033[0m", end=end)


def check_guess(guess, goal):
    """
    Check whether each letter in the guess is in the goal word and in the correct position.

    Parameters
    ----------
    guess : str
        The guessed word.
    goal : str
        The word to guess.

    Returns
    ----------
    results : list of str
        List of results for each letter in the guess. Each result is one of the following:
        - "correct": the letter is in the correct position
        - "misplaced": the letter is in the word but in the wrong position
            - Note: if the letter is in the word multiple times, the number it will be counted as "correct" and \
            "misplaced" (summed) will not be greater than the number of times the letter appears in the word
        - "wrong": the letter is not in the word
    """
    
    # Check if input words are valid
    if guess.isalpha() == False or goal.isalpha() == False:
        raise ValueError("The guess and the goal word must contain only letters.")
    if len(guess) != len(goal):
        raise ValueError("The guess and the goal word must have the same length.")

    # Fill results with "wrong" for each letter in the guess
    results = ["wrong" for i in range(len(guess))]
    # Create list of checked letters with the same length as the guess
    checked_letters = ["_" for i in range(len(guess))]

    # Check for correct letters
    for i in range(len(guess)):
        if guess[i] == goal[i]:
            results[i] = "correct"
            checked_letters[i] = guess[i]

    # Check for misplaced letters
    for i in range(len(guess)):
        if guess[i] in goal and results[i] != "correct":
            if checked_letters.count(guess[i]) < goal.count(guess[i]):
                results[i] = "misplaced"
            checked_letters[i] = guess[i]
    
    return results


def print_guess_results(guess, results):
    """
    Print the guess and the results of the guess.

    Parameters
    ----------
    guess : str
        The guessed word.
    results : list of str
        List of results for each letter in the guess.

    Returns
    -------
    None.
    """
    for i in range(len(guess)):
        if results[i] == "correct":
            print_color(guess[i], "green", end='')
        elif results[i] == "misplaced":
            print_color(guess[i], "yellow", end='')
        else:
            print_color(guess[i], "red", end='')
    print()


def main():

    # Only words with this length will be considered
    word_length = 5
    guess_limit = 6

    # Load the word list
    with open("words_alpha.txt", 'r') as wordlist:
        # Remove leading and trailing whitespaces from each word
        # Only keep words with the correct length
        words = [word.strip() for word in wordlist if len(word.strip()) == word_length]

    word_to_guess = random.choice(words)
    guesses = 0

    # DEBUG start ---------------------

    # print(words[0:10])

    # word_to_guess = "green"
    # print_color(word_to_guess, "green")

    # DEBUG end -----------------------

    print("Welcome to Wordle!")
    print("The word to guess has {} letters.".format(word_length))

    while guesses < guess_limit:
        guess = input("Enter your guess: ")

        if guess == word_to_guess:
            if guesses == 0:
                print("Wow, an Ace! You guessed the word on the first try!")
            elif guesses == 1:
                print("Amazing, a Deuce! You guessed the word on the second try!")
            elif guesses == 5:
                print("Phew, you made it! You guessed the word on the last try!")
            else:
                print("Congratulations! You guessed the word!")
            print("The word was: ", end='')
            print_color(word_to_guess, "green")
            break

        # Check if the guess is valid
        if len(guess) != word_length:
            print("Invalid guess. The word has {} letters.".format(word_length))
            continue
        if guess not in words:
            print("Invalid guess, not a valid word.")
            continue

        guesses += 1

        if guesses >= guess_limit:
            print("You ran out of guesses! The word was:", end='')
            print_color(word_to_guess, "green")
            break

        results = check_guess(guess, word_to_guess)

        print("Guess results:")
        print_guess_results(guess, results)

        print("Guesses left: {}".format(guess_limit - guesses))


if __name__ == "__main__":
    main()
