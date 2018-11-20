
from Workers.Display import *
from Workers import Engine

# Main script for a machine-learning movie recommender

title = 'find\n- a -\nfilm'

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction',
          'Thriller', 'War', 'Western']

engine = Engine.Engine()

search = [engine.get_content_recommendations, engine.get_top_genre, engine.get_top_movies]

# Main loop
while chosen not in inputer.quit_words:
    cls()
    print('\nWecome to\n')
    display_title(title)
    try:
        # Asks user for what kind of recommendation that they want
        search_type = inputer.get_search_type()
        cls()
        recs = []
        if chosen not in inputer.quit_words:
            # Processes request
            recs = inputer.handle_input(search_type)
            cls()
            # Prints results of request
            print(recs.to_string(header=True, justify=all))
            # If desired, prints wikipedia entry for chosen movie
            inputer.get_more_info(recs)
    except (ValueError, KeyError) as val:
        print(val)
        print('\nReceived unusable input. Please try again.\n')
    except (IndexError, AttributeError) as ind:
        print(ind)
        print('\nSorry, a bug got in. Please try again.\n')
    if chosen not in quit_words:
        cls()
        # Asks user if they would like to continue, or exit
        chosen = input('\nWould you like to try a new search? \n')
cls()
print()
print('Thanks for using')
print()
display_title(title)
