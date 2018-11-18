
import warnings
from Workers.Display import *
with warnings.catch_warnings(record=True) as warn:
    from Workers import Engine


# The main script for a machine-learning movie recommender

#print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

engine = Engine.Engine()

search = [engine.get_content_recommendations]

while chosen not in quit_words:
    cls()
    display_title('rec-a-film')
    # TODO: do something separate for kid's movie recommendations
    chosen = input("Enter a movie title or type 'exit' to quit:  \n")
    num_sim = input("How many similar movies would you like to see?:\n")
    recs = []
    try:
        if chosen not in quit_words:
            recs = engine.get_content_recommendations(chosen, num_sim)
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
                    more = recs.values[int(more)]
                if more not in recs.values:
                    print("Please enter a value from the list of choices.")
                else:
                    print(engine.find_summary(more))
                print()
    except (KeyError, IndexError) as ke:
        print(ke)
        print('Sorry, we could not find that movie\n')
    except ValueError as val:
        print(val)
        print('Something went wrong\n')
    if chosen not in quit_words:
        chosen = input('Do you want to continue? \n')
cls()
print()
#print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')
display_title('Thanks for using rec-a-film')

