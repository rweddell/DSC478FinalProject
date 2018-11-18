
import warnings
from Workers.Display import *
with warnings.catch_warnings(record=True) as warn:
    from Workers import Engine


# The main script for a machine-learning movie recommender



print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")

chosen = ''

quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']

engine = Engine.Engine()

search = [engine.get_content_recommendations, engine.get_rating_recommendations]

while chosen not in quit_words:
    cls()
    pil_display('WORLDS GREATEST MOVIE RECOMMENDER')
    #print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER\n")
    # TODO: here, we can add a case statement where the use can decide what search to perform: TFIDF vs Rating
    kid = input("Are you looking for a kid's movie? : \n")
    chosen = input("Enter a movie title or type 'exit' to quit:  \n")
    search_type = 2
    while search_type not in [0,1]:
        search_type = int(input('Are you looking for movies related by Content or similar ratings?\n'
                                '[0] Content\n'
                                '[1] Ratings\n'))
        if search_type not in [0,1]:
            print("Please provide an answer of 0 or 1")
    recs = []
    try:
        if chosen not in quit_words:
            # TODO: this is where the chosen search would be performed
            recs = search[search_type](chosen)
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
cls()
print()
print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')

