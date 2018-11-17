
from Workers import Engine

"""
The main script for the machine-learning movie recommender
"""

def find_title(title, engineer, k=5):
    return engineer.apply_knn(title)


def find_genre(genre, engineer, k=5):
    # 'genre' should be a list
    sims = []
    for entry in genre:
        pass
    pass


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

while chosen not in quit_words:
    chosen = input('Enter a title for similarity:  ')
    try:
        if chosen not in quit_words:
            engine = Engine.Engine()
            recs = engine.apply_knn(chosen)
            print(recs.values)
            more = input('Would you like more recommendations for similar movies to ' + chosen + '? y/n:  ')
            if more is 'y':
                recs = engine.apply_knn(chosen)
                print(recs.values)
                print("Ha, it's the same stuff.")
            print("Type 'exit' to quit or,")
    except:
        print('Sorry, we could not find that movie')

print('Thanks for using the GREATEST MOVIE RECOMMENDER EVER')

