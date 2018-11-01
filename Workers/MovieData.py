
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Should split the data into sets in this class


class MovieData:

    def __init__(self):
        os.chdir('DataStorage')
        self.datafile = pd.read_csv('movies_metadata.csv')
        os.chdir('..')
        os.chdir('Workers')
        # TODO: call preprocess to get target variable from data
        # self.datafile could be split into target and data
        # should probably change with each search
        self.data = 'something totally cool'
        self.target = 'something else totally cool'

    def preprocess(self):
        # TODO: at least get target variables from data, but clean if necessary
        # have to normalize all this crap: get_dummies()?
        # what does preprocessing mean for this data?
        pass

    def reassign_target(self, new_target):
        # new_target should be a column name in the movie data set
        self.target = new_target

    def split_data(self, test_size):
        # not sure if we need this function
        return train_test_split(self.data, self.target, test_size, random_state=33)


'''
def test_movie():
    md = MovieData()
    print(md.datafile.head())


test_movie()
'''

