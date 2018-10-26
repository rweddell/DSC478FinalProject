
import pandas as pd
from sklearn.model_selection import train_test_split

# Should split the data into sets in this class


class MovieData:

    def __init__(self):
        self.data = pd.read_csv('DataStorage\movies_metadata.csv')
        # TODO: call preprocess to get target variable from data
        # self.data is split into targets and clean (or a better name)
        self.clean = 'something totally cool'
        self.targets = 'something else totally cool'

    def preprocess(self):
        # TODO: at least get target variables from data, but clean if necessary
        # have to normalize all this crap: get_dummies()?
        pass

    def split_data(self, test_size):
        return train_test_split(self.data, self.targets, test_size, random_state=33)






