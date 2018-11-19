
from Workers.Display import *
from Workers.InputHandler import *

# The main script for a machine-learning movie recommender

title = 'find\n- a -\nfilm'

search_type = ''

chosen = ''

inputer = InputHandler()

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

while chosen not in quit_words:
    cls()
    print('\nWelcome to\n')
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
    except (ValueError, KeyError) as val:
        print(val)
        print('\nReceived unusable input. Please try again.\n')
    except IndexError as ind:
        print(ind)
        print('\nSorry, a bug got in. Please try again.\n')
    if chosen not in quit_words:
        cls()
        chosen = input('\nWould you like to try a new search? \n')
cls()
print()
print('Thanks for using')
print()
display_title(title)

