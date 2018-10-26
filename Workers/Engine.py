

"""
Recieves user data from GUI
Retrieves DataStorage from csv file

"""

from Workers import MovieData, UserHandler
from sklearn.neighbors import KNeighborsClassifier as knn


class Engine:

    def __init__(self):
        self.movie_data = MovieData
        self.user_handler = UserHandler

    def collect(self, preferences, user):
        # collects user data from Window class
        profile = self.user_handler.get_profile(user, preferences)

    def apply_knn(self):
        # where the magic happens
        # should return a predicted class that can be used to recall
        # recommended movies from the data set
        pass







