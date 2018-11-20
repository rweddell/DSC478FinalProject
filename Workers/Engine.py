

"""
Receives user data from GUI
Retrieves DataStorage from csv file
"""

from Workers import MovieData
import numpy as np


class Engine:

    def __init__(self):
        self.movie_data = MovieData.MovieData()

    def get_content_recommendations(self, title, n):
        """
        Custom KNN function using Cosine Similarity
        :param title: movie title: string
        :param n: number of desired recommendations: int
        :return: pd.Series(top n movies similar to title)
        """
        # Get the index of the movie that matches the title
        idx = self.movie_data.data.title[self.movie_data.data.title == title].index
        # Get cosine similarity matrix from MovieData
        cosine_sim = self.movie_data.cosine_sim
        # Get the pairwise similarity scores of all movies with that movie &
        # sort the movies based on the indices of the similarity scores
        sim_scores = (np.flip(np.sort(cosine_sim[idx])))
        sim_scores = sim_scores[0, 1:(n + 1)]
        sim_indices = np.flip(np.argsort(cosine_sim[idx]))
        # Get the indices of the 10 most similar movies
        movie_indices = sim_indices[0, 1:(n + 1)]
        # Get the movies based on indices and sort them according to weighted score
        movies = self.movie_data.data.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'scores']]
        # Append similarity scores to movies
        movies['similarity%'] = sim_scores * 100
        movies = movies.sort_values('scores', ascending=False).reset_index()
        # Return the top 10 most similar movies
        return movies[['title', 'vote_count', 'vote_average', 'scores', 'similarity%']]

    def get_top_movies(self, n):
        """
        Sort movies based on weighted score
        :param n: int
        :return: pd.Series(top n movies based on weighted score)
        """
        top_movies = self.movie_data.data.sort_values('scores', ascending=False).reset_index()
        return top_movies[['title', 'vote_count', 'vote_average', 'scores']].head(n)

    def get_top_genre(self, genre, n):
        """
        Sort selected genre movie grouping
        :param genre: string
        :param n: int
        :return: pd.Series(top movies for 'genre')
        """
        top_genre = self.movie_data.gen_data[self.movie_data.gen_data['genres'] == genre].sort_values('scores', ascending=False).reset_index()
        return top_genre[['title', 'vote_count', 'vote_average', 'scores']].head(n)
