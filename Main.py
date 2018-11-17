
import warnings
import os
with warnings.catch_warnings(record=True) as warn:
    from Workers import Engine


# The main script for the machine-learning movie recommender


def cls():
    # clears the console when called from shell/console
    os.system('cls' if os.name == 'nt' else 'clear')


print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

engine = Engine.Engine()

while chosen not in quit_words:
    cls()
    print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER\n")
    chosen = input("Enter a movie title or type 'exit' to quit:  \n")
    recs = []
    try:
        if chosen not in quit_words:
            recs = engine.get_content_recommendations(chosen)
            print()
            #for entry in recs.values:
            #    print(entry)
            for i in range(len(recs.values)):
                print(i, recs.values[i])
            print('\nWould you like to know more about any of these titles?')
            more = input('Type the title or "exit":  \n')
            if more in quit_words:
                break
            if more not in recs.values:
                print("That wasn't in the list of choices.")
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

print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')

