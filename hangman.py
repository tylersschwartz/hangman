#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylersschwartz
"""
import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    in_file = open(WORDLIST_FILENAME, 'r')
    line = in_file.readline()
    wordlist = line.split()
    return wordlist


def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def get_valid_guess(letters_guessed):
    """
    letters_guessed: set, what letters have been guessed so far
    Takes in user input, a lowercase alphabetical character.
    If is a valid input returns that character, else prints an error message and returns to input prompt
    until valid guess is given.
    """
    while True:
        guess = input("Please enter your guess: ", )
        guess = guess.lower()
        if len(guess) > 1:
            print("Please only enter a single character.")
        elif not guess.isalpha():
            print("Please use an alphabetical character.")
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter.")
        else:
            return guess


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: set, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    count = 0
    for l in secret_word:
        if l in letters_guessed:
            count += 1
    return count == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: set, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    """
    guess_word = ""
    for l in secret_word:
        if l in letters_guessed:
            guess_word = guess_word + l + " "
        else:
            guess_word += '_ '
    return guess_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: set of what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    import string
    letters_left = ""
    for l in string.ascii_lowercase:
        if l not in letters_guessed:
            letters_left += l
    return letters_left


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up a game of Hangman.

    At startup, lets the user know how many guesses the have left.

    User supplies one valid guess per round, or is prompted to
    after an invalid guess.

    User receives feedback whether or not the guess is in secret word.

    After each round, user is given the correctly guessed letters of the secret word,
    as well as the available letters and the number of guesses left.
    """
    guesses_left = 8
    letters_guessed = set()
    print("Welcome to Hangman!")
    print("I'm thinking of a word that is", len(secret_word), "letters long.")
    while guesses_left > 0:
        print("-----------")
        print("You have", guesses_left, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        guess = get_valid_guess(letters_guessed)
        letters_guessed.add(guess)
        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                break
        else:
            print("Nope! That letter is not in the word: ", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
    if is_word_guessed(secret_word, letters_guessed):
        print("-----------")
        print("Congratulations, you guessed correctly!")
    else:
        print("-----------")
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


secret_word = choose_word(wordlist).lower()
hangman(secret_word)
