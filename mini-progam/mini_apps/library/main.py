import pandas as pd
import numpy as np
import os

def listing(database):
    genre_list = set()

    for column in database.columns[1:]:
        genre_list.update(database[column].unique())

    return genre_list

def theme():
    os.system('cls')
    layer1 = True

    while layer1 == True:
        choice_theme = int(input('Anime[1], Manga[2], Exit[3]\nWhat theme you wanna pick?\nYour choice: '))
        os.system('cls')

        if choice_theme == 1: ## pick theme
            anime = pd.read_csv('E:\\Latihan\\GitHub Clone\\mini_projects\\mini-progam\\mini_apps\\library\\datas\\anime.csv')
            genre_anime = listing(anime)
            layer2 = True

            while layer2 == True:
                choice = int(input('Show All[1], Filter by Genre[2], Back[3], Exit[4]\nYour choice: '))

                if choice == 1: ## show all anime
                    showing = True
                    first_index = 0 ## index-ing showing
                    last_index = 10 ## index-ing showing
                    print(anime.Title[first_index:last_index].to_markdown(index=False))

                    while showing == True:
                        choice_showing = int(input('Next[1], Back[2], Exit[3]\nYour choice: '))
                        os.system('cls')

                        if choice_showing == 1:
                            first_index = last_index
                            last_index += 10
                            show_anime = anime.Title[first_index:last_index]

                            if len(show_anime) < 10: ## make dont repeat
                                print(show_anime.to_markdown(index=False), '\n\nThis is the end\n')
                                showing = False

                            else:
                                print(show_anime.to_markdown(index=False), '\n')

                        elif choice_showing == 2:
                            os.system('cls')
                            showing = False

                        elif choice_showing == 3:
                            os._exit(os.EX_OK)

                        else:
                            print("\nThat is not a valid number.")

                elif choice == 2: ## filtering by genre
                    os.system('cls')
                    choice_genre = int(input('Show All Genre[1], Filter Genre[2]\nYour choice: '))

                    if choice_genre == 1: ## show all genre
                        os.system('cls')
                        all_genre = []

                        for column in anime.columns:
                            if 'genre' in column:
                                all_genre.extend(np.unique([anime[str(column)]]))
                        print(np.unique(all_genre))

                    elif choice_genre == 2: ## search by genre
                        os.system('cls')
                        choice_genre_2 = [(input('What genre you want?\nYour choice: ')).lower()]
                        anime_by_genre = anime[anime.genre1.isin(choice_genre_2) | anime.genre2.isin(choice_genre_2) | anime.genre3.isin(choice_genre_2) | anime.genre4.isin(choice_genre_2) | anime.genre5.isin(choice_genre_2) | anime.genre6.isin(choice_genre_2)].Title
                        print(anime_by_genre.to_markdown(index=False),'\n\n')

                    elif choice_genre == 3:
                        os.system('cls')
                        layer2  = False

                    elif choice_genre == 4:
                        os._exit(os.EX_OK)

                    else:
                        print("\nThat is not a valid number.")

                elif choice == 3: ## back
                    os.system('cls')
                    layer2 = False

                elif choice == 4: ## exit
                    os._exit(os.EX_OK)

                else:
                    print("\nThat is not a valid number.")

        elif choice_theme == 2:
            manga = listing(manga)

        elif choice_theme == 3: ## exit
            os._exit(os.EX_OK)

        else:
            os.system('cls')
            print("i'm sorry that's not exist")

theme()