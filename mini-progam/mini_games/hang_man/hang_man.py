from hang_man.words import words
from secrets import choice
import string
import os

def hangman():
    pick_word = choice(words).upper()

    alphabet = set(string.ascii_uppercase)
    lives = 8

    user_letters = []
    word_in_spell = []
    char_in_word = set(pick_word)

    for char in pick_word:
        word_in_spell.append(char)
    
    while len(char_in_word) > 0 and lives > 0:
        os.system('cls')
        print('You have ', lives, ' lives left and you have used these letters: ', ' '.join(user_letters))

        word_disp = [word if word in user_letters else '-' for word in pick_word]
        print('Current word: ', ' '.join(word_disp))

        user_pick_letter = input('Guess a letter: ').upper()
        if user_pick_letter in alphabet - set(user_letters):
            user_letters.append(user_pick_letter)
            if user_pick_letter in char_in_word:
                char_in_word.remove(user_pick_letter)
                print('')
            else:
                lives -= 1
                os.system('cls')
                print('\nYour letter, ', user_pick_letter, 'is not in the word.')
        elif user_pick_letter in user_letters:
            os.system('cls')
            print('\nYou have already used the letter, Guess another letter.')
        else:
            os.system('cls')
            print('\nThat is not a valid letter.')

    if lives == 0:
        os.system('cls')
        print('You died, sorry. the word was', pick_word)
    elif len(char_in_word) == 0:
        os.system('cls')
        print('You win, the word is: ', pick_word)
hangman()