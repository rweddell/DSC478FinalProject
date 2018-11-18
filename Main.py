
import warnings
from Workers.Display import *
from Workers.InputHandler import *
from Workers import Engine

# The main script for a machine-learning movie recommender

#print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")
title = 'find\n-a-\nfilm'

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

genres = ['Action', 'Adventure', 'Animation' 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science'
          'Thriller', 'War', 'Western']

engine = Engine.Engine()

search = [engine.get_content_recommendations, engine.get_top_genre, engine.get_top_movies]

while chosen not in quit_words:
    cls()
    display_title(title)
    try:
        search_type = int(input('Enter an option number :\n'
                                '0 Get top-rated movies\n'
                                '1 Get top-rated movies for a genre\n'
                                '2 Get movies similar to a chosen movie\n'))
        chosen = None
        if search_type is 1:
            cls()
            for i in range(len(genres)):
                print(i, genres[i])
            chosen = input("Enter the index of the genre that you want:\n")
        elif search_type is 2:
            chosen = input("Enter a movie title or type 'exit' to quit:  \n")
            num_sim = int(input("How many recommended movies would you like?:\n"))
        cls()
        recs = []
        if chosen not in quit_words:
            recs = engine.handle_input(search_type, chosen, num_sim)
            print()
            for i in range(len(recs.values)):
                print(i, recs.values[i])
            print('\nWould you like to know more about one of these titles?')
            more = ''
            while more not in quit_words:
                more = input('\nType the title or title index or type "exit":  \n')
                if more in quit_words:
                    break
                elif more.isnumeric():
                    more = recs.title.values[int(more)]
                if more not in recs.values:
                    print("Please enter a value from the list of choices.")
                else:
                    print(engine.find_summary(more))
                print()
                cls()
    except (KeyError, IndexError) as ke:
        print(ke)
        print('Sorry, we could not find that movie\n')
    except ValueError as val:
        print(val)
        print('Received incorrect input. Please try again.\n')
    if chosen not in quit_words:
        chosen = input('Do you want to continue? \n')
cls()
print()
#print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')
print('Thanks for using')
print()
display_title(title)

