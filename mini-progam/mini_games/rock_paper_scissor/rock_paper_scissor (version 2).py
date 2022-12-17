from secrets import choice
import os

class history_match:
    win = 0
    draw = 0
    lose = 0


def match(history, list_choice):
    computer_choice = choice(list_choice)
    print('---------------\nRock, Paper, Scissor')
    player_choice = input('Your choice: ').lower()

    if player_choice in list_choice:
        if player_choice == 'rock' and computer_choice == 'scissor':
            os.system('cls')
            print('\nYou Win, Computer choose:', computer_choice)
            history.win += 1

        elif player_choice == 'scissor' and computer_choice == 'paper':
            os.system('cls')
            print('\nYou Win, Computer choose:', computer_choice)
            history.win += 1

        elif player_choice == 'paper' and computer_choice == 'rock':
            os.system('cls')
            print('\nYou Win, Computer choose:', computer_choice)
            history.win += 1

        elif player_choice == 'rock' and computer_choice == 'rock':
            print('\nDraw')
            history.draw += 1

        elif player_choice == 'scissor' and computer_choice == 'scissor':
            print('\nDraw')
            history.draw += 1

        elif player_choice == 'paper' and computer_choice == 'paper':
            print('\nDraw')
            history.draw += 1

        else:
            os.system('cls')
            print('\nYou Lose, Computer choose:', computer_choice)
            history.lose += 1
    else:
        print('That is not a valid choice.')

def rock_paper_scissor():
    print('-----------------\nRock-Paper-Scissor\n-----------------')
    print('Wanna play ?\nYes[1], No[2]')
    menu1 = int(input('Your choice: '))
    history = history_match
    os.system('cls')

    while int(menu1) == 1:
        list_choice = ["scissor","rock","paper"]
        play = history.draw + history.lose + history.win

        if play > 0:
            print('\n-----------------\nPlay[1], Histori[2], Exit[3]')
            menu2 = input('Your choice: ')

            if int(menu2) == 1:
                os.system('cls')
                match(history, list_choice)

            elif int(menu2) == 2:
                os.system('cls')
                print('-----------------\nShow Histori[1], Clean Histori[2], Play[3]')
                menu3 = input('Your choice: ')

                if int(menu3) == 1:
                    print('---------------\nPlay: ', play, '\nWin: ',history.win, '\nDraw: ', history.draw, '\nLose: ', history.lose)
                
                elif int(menu3) == 2:
                    os.system('cls')
                    history.win = 0
                    history.draw = 0
                    history.lose = 0                    
                    print('---------------\nPlay: 0', '\nWin: ',history.win, '\nDraw: ', history.draw, '\nLose: ', history.lose)
                    print('\nPlay Match[1], Exit[]')
                    menu4 = input('Your choice:')
                    if int(menu4) == 1:
                        match(history, list_choice)
                    else:
                        os._exit(os.EX_OK)
                
                elif int(menu3) == 3:
                    os.system('cls')
                    match(history, list_choice)
                
                else:
                    os.system('cls')
                    print('\nThat is not a valid number.')

            elif int(menu2) == 3:
                os._exit(os.EX_OK)

            else:
                print('\nThat is not a valid number.')
        
        else:
            match(history, list_choice)
    
    else:
        os._exit(os.EX_OK)
            
rock_paper_scissor()