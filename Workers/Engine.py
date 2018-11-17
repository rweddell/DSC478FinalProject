

"""
Receives user data from GUI
Retrieves DataStorage from csv file
"""

from Workers import MovieData, UserHandler
import warnings
import wikipedia
from sklearn.neighbors import NearestNeighbors as nn
import numpy as np
warnings.filterwarnings('ignore')



class Engine:

    def __init__(self):
        self.movie_data = MovieData.MovieData()
        self.user_handler = UserHandler.UserHandler()

    def collect(self, preferences, user):
        # collects user data from Window class
        profile = self.user_handler.get_profile(user, preferences)

    # bet i can turn this into an indie/blockbuster detector
    def apply_knn(self, title):
        # where the magic happens
        # should return a predicted class that can be used to recall
        # recommended movies from the data set
        # MAY need to transform to np.array
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        idxa = self.movie_data.tfidf_matrix[idx]
        #print(idxa.shape)
        #print(idxa)
        neigh = nn(n_neighbors=10)
        neigh.fit(self.movie_data.tfidf_matrix)
        # Get index of k nearest neighbors
        kneighbors = neigh.kneighbors(idxa, return_distance=False)
        print(kneighbors)
        kneighbors = np.squeeze(kneighbors)
        #print(kneighbors)
        #movie_indices = [i[0] for i in kneighbors]
        #print("sup")
        #print(movie_indices)
        return self.movie_data.data['title'].iloc[kneighbors]

    # NOTE: This shit runs but it sucks at making predictions...
    def get_content_recommendations(self, title):
        # Get the index of the movie that matches the title
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        # Get cosine similarity matrix from MovieData
        cosine_sim = self.movie_data.cosine_sim
        # Sort the movies based indices of the similarity scores
        sim_scores = np.flip(np.argsort(cosine_sim[idx]))
        # Get the indices of the 10 most similar movies
        movie_indices = sim_scores[0, 1:26]
        # Get the movies based on indices
        movies = self.movie_data.data.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'scores']]
        movies = movies.sort_values('scores', ascending=False).head(10)
        # Return the top 10 most similar movies
        #return self.movie_data.data['title'].iloc[movies.index]
        return movies 

    def get_top_movies(self, n):
        # Sort movies based on weighted score
        top_movies = self.movie_data.data.sort_values('score', ascending=False)
        return top_movies[['title', 'vote_count', 'vote_average', 'score']].head(n)


    # returns the first paragraph (as a string) of the wikipedia article most closely associated with the word
    def find_summary(self, ename):
        # TODO: deal with the disambiguation warning
        # could start off with taking the first entry for the word from wikipedia
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
