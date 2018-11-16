
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

# Should split the data into sets in this class


class MovieData:

    def __init__(self):

        self.data_path = os.path.join(os.getcwd(), 'DataStorage')
        self.datafile = pd.read_csv(os.path.join(self.data_path, 'movies_metadata.csv'))
        # TODO: call preprocess to get target variable from data
        # self.datafile could be split into target and data
        # should probably change with each search
        self.data = self.datafile.copy()
        self.target = 'This variable should contain the target data'
        # Construct a reverse map of indices and movie titles
        self.indices = pd.Series(self.data.index, index=self.data['title']).drop_duplicates()
        # Below could be target if we go for most similar as only feature.
        self.cosine_sim = self.data.preprocess()

    def __getattr__(self, item):
        return "Attribute does not exist."

    def preprocess(self):
        # TODO: at least get target variables from data, but clean if necessary & reduce dimension size
        # have to normalize all this crap: get_dummies()?
        # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')
        # Replace NaN with an empty string
        self.data['overview'] = self.data['overview'].fillna('')
        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(self.data['overview'])
        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return cosine_sim


    def reassign_target(self, new_target):
        # new_target should be a column name in the movie data set
        self.target = new_target

    def split_data(self, test_size):
        # not sure if we need this function
        return train_test_split(self.data, self.target, test_size, random_state=33)


def test_movie():
    md = MovieData()
    print(md.datafile)
    genres = []
    '''
    for thing in md.datafile.Genre:
        if thing not in genres:
            genres.append(thing)
    for thing in sorted(genres):
        print(thing)
    '''

test_movie()


