
from Workers import Engine

"""
The main script for the machine-learning movie recommender
"""

print("WELCOME TO THE WORLD'S GREATEST MOVIE RECOMMENDER")

genres = ['Action', 'Adventure', 'Animation' 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science'
          'Thriller', 'War', 'Western']

genrestring = ''
for g in genres:
    genrestring = genrestring + g + ' '

chosen = ''
quit_words = ['exit', 'close', 'quit']

engine = Engine.Engine()

while chosen not in quit_words:
    chosen = input('Enter a movie title:  ')
    try:
        if chosen not in quit_words:
            recs = engine.apply_knn(chosen)
            print(recs.values)
            print("Type 'exit' to quit or,")
    except KeyError:
        print('Sorry, we could not find that movie')

print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')

