
from Workers import Engine
import os

"""
The main script for the machine-learning movie recommender
"""


def cls():
    # clears the console when called from shell/cmd
    os.system('cls' if os.name=='nt' else 'clear')


print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")

genres = ['Action', 'Adventure', 'Animation' 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science'
          'Thriller', 'War', 'Western']

genrestring = ''
for g in genres:
    genrestring = genrestring + g + ' '

chosen = ''
quit_words = ['exit', 'close', 'quit', 'no', 'n']

engine = Engine.Engine()

while chosen not in quit_words:
    cls()
    print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")
    chosen = rawinput("Enter a movie title or type 'exit' to quit:  ")
    recs = []
    try:
        if chosen not in quit_words:
            recs = engine.get_content_recommendations(chosen)
            print(recs.values)
            for i in range(len(recs)):
                print(str(i) + '  ' + str(recs[i]))
            print('Would you like to know more about any of these titles?')
            more = input('Type the name or index of movie, or type "exit"')
            if more in quit_words:
                break
            else:
                if type(more) == int:
                    more = recs[more]
                print(engine.find_summary(more))
        larry = input('was it good for you?')

    except KeyError:
        print('Sorry, we could not find that movie')
    except ValueError as val:
        print(val)
        print('Something went wrong')

print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')

