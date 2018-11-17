
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from zipfile import ZipFile
import os

# Should split the data into sets in this class


class MovieData:

    def __init__(self):

        self.data_path = os.path.join(os.getcwd(), 'DataStorage')
        self.datafile = pd.read_csv(os.path.join(self.data_path, 'short_metadata.csv'), low_memory=False)
        # Create reduced dimension data set & cosine similarity matrix
        self.data, self.cosine_sim, self.tfidf_matrix = self.preprocess()
        # not sure we need a target variable...
        self.target = 'This variable should contain the target data'
        # Construct a reverse map of indices and movie titles
        self.indices = pd.Series(self.data.index, index=self.data['title'])

    def __getattr__(self, item):
        return "Attribute does not exist."

    def preprocess(self):
        # TODO: at least get target variables from data, but clean if necessary & reduce dimension size
        # Calculate the minimum number of votes required to be in the chart (90th percentile)
        min_votes = self.datafile['vote_count'].quantile(0.90)
        #print(min_votes)
        # Calculate mean average vote across entire dataset ala IMDB
        mean_score = float(self.datafile['vote_average'].mean())
        # Filter out all qualified movies into a new DataFrame (about 4555 entries)
        data = self.datafile.loc[self.datafile.vote_count >= min_votes].copy()
        # Append weighted scores to new DataFrame
        #data['score'] = self.weighted_rating(data, min_votes, mean_score)
        # Drop duplicates
        data.drop_duplicates(inplace=True)
        # Reassign indices of data
        print(data.head())
        data.reset_index(drop=True, inplace=True)
        print(data.head())
        # Get credits & keywords then merge them with movie metadata
        #creds = pd.read_csv(os.path.join(self.data_path, 'credits.csv'))
        keywords = pd.read_csv(os.path.join(self.data_path, 'keywords.csv'))
        # Convert IDs to int. Required for merging
        keywords['id'] = keywords['id'].astype('int')
        #creds['id'] = creds['id'].astype('int')
        #print(data.head())
        #print('Type of data' + str(type(data)))
        #print(data.columns)
        data['id'] = data['id'].astype('int')
        # Merge keywords and credits into dataframe
        #data = data.merge(creds, on='id')
        data = data.merge(keywords, on='id')
        # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')
        # Replace NaN with an empty string
        data['overview'] = data['overview'].fillna('')
        print(data.shape)
        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(data['overview'])
        print(tfidf_matrix.shape)
        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return data, cosine_sim, tfidf_matrix

    # still not sure this is needed
    def reassign_target(self, new_target):
        # new_target should be a column name in the movie data set
        self.target = new_target

    # or this...
    def split_data(self, test_size):
        return train_test_split(self.data, self.target, test_size, random_state=33)

    # Function that computes the weighted rating of each movie
    def weighted_rating(self, df, m, c):
        size = len(df['vote_count'])
        #print(m, c)
        wr = []
        for i in range(size):
            v = df['vote_count'].loc[i].astype(float)
            r = df['vote_average'].loc[i].astype(float)
            #print(v,r)
            wr.append(v / (v + m) * r) + (m / (m + v) * c)
        # Calculation based on the IMDB formula
        return pd.Series(wr)


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

#test_movie()


