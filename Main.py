
from Workers.Display import *
from Workers.InputHandler import *

# The main script for a machine-learning movie recommender

title = 'find\n- a -\nfilm'

search_type = ''

chosen = ''

inputer = InputHandler()

while chosen not in inputer.quit_words:
    cls()
    print('\nWelcome to\n')
    display_title(title)
    try:
        search_type = inputer.get_search_type()
        cls()
        recs = []
        if chosen not in inputer.quit_words:
            recs = inputer.handle_input(search_type)
            cls()
            print(recs.to_string(header=True, justify=all))
            inputer.get_more_info(recs)
    except (ValueError, KeyError) as val:
        print(val)
        print('\nReceived unusable input. Please try again.\n')
    except (IndexError, AttributeError) as ind:
        print(ind)
        print('\nSorry, a bug got in. Please try again.\n')
    if chosen not in inputer.quit_words:
        cls()
        chosen = input('\nWould you like to try a new search? \n')
cls()
print()
print('Thanks for using')
print()
display_title(title)

