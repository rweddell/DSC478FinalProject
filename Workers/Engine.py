

"""
Receives user data from GUI
Retrieves DataStorage from csv file
"""

from Workers import MovieData, UserHandler
from sklearn.neighbors import NearestNeighbors as nn
import numpy as np


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
        # Get the pairwise similarity scores of all movies with that movie
        print(cosine_sim[idx])
        #sim_scores = list(enumerate(cosine_sim[idx]))
        # Sort the movies based on the similarity scores
        #sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = np.flip(np.argsort(cosine_sim[idx]))
        # Get the scores of the 10 most similar movies
        print(sim_scores)
        print(sim_scores.shape)
        sim_scores = sim_scores[0, 1:11]
        print(sim_scores)
        # Get the movie indices
        #movie_indices = [i[0] for i in sim_scores]
        #print(movie_indices)
        # Return the top 10 most similar movies
        return self.movie_data.data['title'].iloc[sim_scores]


    def get_top_movies(self, n):
        # Sort movies based on weighted score
        top_movies = self.movie_data.data.sort_values('score', ascending=False)
        return top_movies[['title', 'vote_count', 'vote_average', 'score']].head(n)




