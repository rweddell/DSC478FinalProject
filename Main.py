
from Workers import Engine

"""
The main script for the machine-learning movie recommender
"""

def find_title(title, engineer, k=5):
    return engineer.get_content_recommendations(title)


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
close_words = ['exit', 'close', 'quit']

while chosen not in close_words:
    chosen = input('Enter a title for similarity:  ')
    engine = Engine.Engine()
    recs = engine.get_content_recommendations(chosen)
    print(recs)

