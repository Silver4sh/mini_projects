from secrets import choice
import string
import os

def pick_theme():
    os.system('cls')
    print('---------------\nHang Man\n---------------\n')
    choice = False

    while choice == False:
        theme_list = ['Animal', 'Country', 'Fruits']
        print('What theme do yo wanna play ?\n',theme_list)
        theme_words = input('Your choice: ').lower()

        if theme_words == 'animal':
            from words.animal import words
            choice = True
            return words

        elif theme_words == 'country':
            from words.country import words
            choice = True
            return words

        elif theme_words == 'fruits':
            from words.fruits import words
            choice = True
            return words

        else:
            os.system('cls')
            print('---------------\nThat is not a valid theme.\n---------------\n')

def hangman():
    menu1 = False

    while menu1 == False:
        words = pick_theme()
        menu1 = True
        menu2 = False

    while menu2 == False:
        pick_word = choice(words).upper()
        alphabet = set(string.ascii_uppercase)
        list_menu2 = ['Yes[1], No[2], Change Theme[3]']
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
            print('\nWanna play againt?\n', list_menu2)
            choice_menu2 = input('Youre choice: ')

            if int(choice_menu2) == 2:
                os._exit(os.EX_OK)

            elif int(choice_menu2) == 3:
                menu1 = False
                words = pick_theme()
            else:
                print('\nThat is not a valid number.')

        elif len(char_in_word) == 0:
            os.system('cls')
            print('You win, the word is: ', pick_word)
            print('\nWanna play againt?\n', list_menu2)
            choice_menu2 = input('Youre choice: ')

            if int(choice_menu2) == 2:
                os._exit(os.EX_OK)

            elif int(choice_menu2) == 3:
                menu1 = False
                words = pick_theme()

            else:
                print('\nThat is not a valid number.')
hangman()