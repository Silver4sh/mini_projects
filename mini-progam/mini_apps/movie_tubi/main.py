import pandas as pd
import os

database = pd.read_csv('E:\\Latihan\\GitHub Clone\\mini_projects\\mini-progam\\mini_apps\\movie_tubi\\raw_data\\tubi.csv')
database = database.rename(columns={
    'Title_URL': 'URL',
    'Content': 'Year',
    'Content1': 'Duration',
    'Content2': 'Rate',
    'Content3': 'Genre'
})

def movie(database):
    total_database = len(database)
    show_data = total_database/10
    os.system('cls')
    print('---------------\nMovie (tube)\n---------------\n')
    menu1 = False
    while menu1 == False:
        print('Show all Movie[1], Filter by:[2], Exit[3]')
        choice_1 = int(input('Your choice: '))

        if choice_1 == 1:
            print(database.to_markdown())
            print('\nBack[1], Exit[2]')
            choice_2 = int(input('You choice: '))

            if choice_2 == 1:
                os.system('cls')

            elif choice_2 == 2:
                os._exit(os.EX_OK)

            else:
                print('\nThat is not a valid number.')

        elif choice_1 == 2:
            print('Filter by: Year[1], Rate[2], Genre[3], ... Back[4]')
            choice_2 = int(input('Your choice: '))

            if choice_2 == 1:
                os.system('cls')
                years_list = database.Year.unique()
                min_ = years_list.min()
                max_ = years_list.max() 
                
            elif choice_2 == 2:
                os.system('cls')
                rate_list = list(database.Rate.unique())
                print('List Rate:\n', rate_list)
                choice_rate = [input('Your Choice: ').upper()]
                get_data_rate = database[database.Rate.isin(choice_rate)]
                print(get_data_rate, '\n')

            elif choice_2 == 3:
                os.system('cls')
                print('Genre List: ')
                choice_genre = [input('*can multiple\nYour Choice: ')]
                choice_genre = [genre.title() for genre in choice_genre]
                get_data_genre = database[database.Genre.isin(choice_genre)]
                print(get_data_genre, '\n')

            elif choice_2 == 4:
                print('d')
            
            else:
                print('\nThat is not a valid number.')

        elif choice_1 == 3:
            os._exit(os.EX_OK)

        else:
            print('\nThat is not a valid number.')

movie(database)