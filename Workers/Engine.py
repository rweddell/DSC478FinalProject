

"""
Receives user data from GUI
Retrieves DataStorage from csv file
"""

from Workers import MovieData
import wikipedia
import numpy as np
import pandas as pd


class Engine:

    def __init__(self):
        self.movie_data = MovieData.MovieData()

    # A home brew KNN function using Cosine Similarity
    def get_content_recommendations(self, title, n):
        # Get the index of the movie that matches the title
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        # Get cosine similarity matrix from MovieData
        cosine_sim = self.movie_data.cosine_sim
        # Get the pairwise similarity scores of all movies with that movie &
        # sort the movies based on the indices of the similarity scores
        sim_scores = np.flip(np.argsort(cosine_sim[idx]))
        # Get the indices of the 10 most similar movies
        movie_indices = sim_scores[0, 1:(n + 1)]
        # Get the movies based on indices and sort them according to weighted score
        movies = self.movie_data.data.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'scores']]
        movies = movies.sort_values('scores', ascending=False)
        # Return the top 10 most similar movies
        return movies[['title', 'vote_count', 'vote_average', 'scores']]

    def get_top_movies(self, n):
        # Sort movies based on weighted score
        top_movies = self.movie_data.data.sort_values('scores', ascending=False)
        return top_movies[['title', 'vote_count', 'vote_average', 'scores']].head(n)

    def get_top_genre(self, genre, n):
        g = self.movie_data.data.apply(lambda x: pd.Series(x['genres']), axis=1).stack().reset_index(level=1, drop=True)
        g.name = 'genre'
        gen_data = self.movie_data.data.drop('genres', axis=1).join(g)
        top_genre = gen_data[gen_data['genre'] == genre].sort_values('scores')
        return top_genre[['title', 'vote_count', 'vote_average', 'scores']].head(n)

    def find_summary(self, ename):
        # returns the first paragraph (as a string) of the wikipedia article most closely associated with the word
        ambiguities = []
        brief = ""
        try:
            brief = wikipedia.summary(ename + ' the movie')
        except (wikipedia.exceptions.DisambiguationError, UserWarning) as exc:
            print("Ambiguity error")
            ambiguities = exc.options
            brief = ""
        except wikipedia.exceptions.PageError:
            print("No page found for : {}".format(ename))
        while brief == "" and ambiguities != []:
            try:
                while ambiguities != []:
                    option = ambiguities.pop()
                    clarify = input("Did you mean {}? y/n :  ".format(option)).lower()
                    if clarify == "y":
                        brief = wikipedia.summary(option)
                        break
                    else:
                        pass
            except wikipedia.exceptions.DisambiguationError as cxe:
                print("Ran out of options. Try another word.")
        if brief == "":
            print("Ran out of options. Try another word.")
        return brief
