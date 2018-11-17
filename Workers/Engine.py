

"""
Receives user data from GUI
Retrieves DataStorage from csv file
"""

from Workers import MovieData, UserHandler
import wikipedia
import numpy as np
import warnings
with warnings.catch_warnings(record=True) as warn:
    from sklearn.neighbors import NearestNeighbors as nn


class Engine:

    def __init__(self):
        self.movie_data = MovieData.MovieData()

    def apply_knn(self, title):
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        idxa = self.movie_data.tfidf_matrix[idx]
        neigh = nn(n_neighbors=10)
        neigh.fit(self.movie_data.tfidf_matrix)
        # Get index of k nearest neighbors
        kneighbors = neigh.kneighbors(idxa, return_distance=False)
        print(kneighbors)
        kneighbors = np.squeeze(kneighbors)
        return self.movie_data.data['title'].iloc[kneighbors]

    def get_content_recommendations(self, title):
        # Get the index of the movie that matches the title
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        # Get cosine similarity matrix from MovieData
        cosine_sim = self.movie_data.cosine_sim
        # Get the pairwise similarity scores of all movies with that movie
        #sim_scores = list(enumerate(cosine_sim[idx]))
        # Sort the movies based on the similarity scores
        #sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = np.flip(np.argsort(cosine_sim[idx]))
        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[0, 1:11]
        # Return the top 10 most similar movies
        return self.movie_data.data['title'].iloc[sim_scores]

    def get_top_movies(self, n):
        # Sort movies based on weighted score
        top_movies = self.movie_data.data.sort_values('score', ascending=False)
        return top_movies[['title', 'vote_count', 'vote_average', 'score']].head(n)

    def find_summary(self, ename):
    # returns the first paragraph (as a string) of the wikipedia article most closely associated with the word
        ambiguities = []
        brief = ""
        try:
            brief = wikipedia.summary(ename + ' movie')
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
