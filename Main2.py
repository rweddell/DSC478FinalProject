
import warnings
from Workers.Display import *
from Workers.InputHandler import *
from Workers import Engine

# The main script for a machine-learning movie recommender

title = 'find\n- a -\nfilm'

search_type = ''

chosen = ''

inputer = InputHandler()

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

while chosen not in quit_words:
    cls()
    display_title(title)
    try:
        search_type = inputer.get_search_type()
        cls()
        recs = []
        if chosen not in quit_words:
            recs = inputer.handle_input(search_type)
            print()
            for i in range(len(recs.values)):
                print(i, recs.values[i])
                inputer.get_more_info(recs)
    except (KeyError, IndexError) as ke:
        print(ke)
        print('Sorry, we could not find that movie\n')
    except ValueError as val:
        print(val)
        print('Received incorrect input. Please try again.\n')
    if chosen not in quit_words:
        chosen = input('Would you like to try a new search? \n')
cls()
print()
#print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')
print('Thanks for using')
print()
display_title(title)

