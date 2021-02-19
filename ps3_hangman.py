# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
ALLOWED_GUESSES = 8

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = True
    for letter in secretWord:
        if letter.lower() not in lettersGuessed:
            guessed = False
            break
    return guessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretList = []
    for i in range(len(secretWord)):
        if secretWord[i].lower() in lettersGuessed:
            secretList.append(secretWord[i])
        else:
            secretList.append('_')
    return ' '.join(secretList)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    notGuessed = list(string.ascii_lowercase)
    if len(lettersGuessed) > 0:
        for letter in lettersGuessed:
            notGuessed.remove(letter.lower())
    return ''.join(notGuessed)
    
def getGuess(lettersGuessed, secretWord):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: list, updated list of letters have been guessed so far
    '''    
    validGuess = False
    while not validGuess:
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Not a valid letter from a-z, have another go')
        elif guess not in string.ascii_lowercase:
            print('Not a valid letter from a-z, have another go')
        else:
            validGuess = True
    return guess

def checkGuess(guess, secretWord):
    '''
    Parameters
    ----------
    guess : string
        letter guessed by player.
    secretWord : string
        the secret word.

    Returns
    -------
    boolean - is the letter in the secret word yes or no.

    '''
    return guess in secretWord

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    lettersGuessed = []
    #mistakesMade = 0
    guessesLeft = ALLOWED_GUESSES
    #availableLetters = string.ascii_lowercase
    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print('-------------')
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed)) 
        guess = getGuess(lettersGuessed, secretWord)
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end='' )
        else:
            lettersGuessed.append(guess)
            if checkGuess(guess, secretWord):
                print('Good guess: ', end='')
            else:
                print('Oops! That letter is not in my word: ', end='')
                guessesLeft -= 1
        print(getGuessedWord(secretWord, lettersGuessed))
    print('-------------')
    if guessesLeft <= 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
    else:
        print('Congratulations, you won!')
        
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
