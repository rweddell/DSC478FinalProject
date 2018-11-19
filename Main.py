
import warnings
from Workers.Display import *
from Workers.InputHandler import *
from Workers import Engine

# The main script for a machine-learning movie recommender

title = 'find\n- a -\nfilm'

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction',
          'Thriller', 'War', 'Western']

engine = Engine.Engine()

search = [engine.get_content_recommendations, engine.get_top_genre, engine.get_top_movies]

while chosen not in quit_words:
    cls()
    print('\nWecome to\n')
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
            ind = int(input("\nEnter the index of the genre that you want:\n"))
            chosen = genres[ind]
        elif search_type is 2:
            chosen = input("\nEnter a movie title or type 'exit' to quit:  \n")
        num_sim = int(input("\nHow many recommended movies would you like?:\n"))
        cls()
        recs = []
        if chosen not in quit_words:
            recs = engine.handle_input(search_type, chosen, num_sim)
            print()
            for i in range(len(recs.values)):
                print(i, recs.values[i])
            more = ''
            while more not in quit_words:
                more = input('\nWould you like to know more about one of these titles?\n'
                             'Type the title or title index or type "exit":  \n')
                if more in quit_words:
                    break
                elif more.isnumeric():
                    more = recs.title.values[int(more)]
                if more not in recs.values:
                    print("\nPlease enter a value from the list of choices.\n")
                else:
                    print(engine.find_summary(more))
                print()
    except (KeyError, IndexError) as ke:
        print(ke)
        print('\nSorry, we could not find that movie\n')
    except ValueError as val:
        print(val)
        print('\nReceived incorrect input. Please try again.\n')
    if chosen not in quit_words:
        chosen = input('\nWould you like to start a new search? \n')
cls()
print()
#print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')
print('Thanks for using')
print()
display_title(title)
