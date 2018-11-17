
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from zipfile import ZipFile
from ast import literal_eval
import os


class MovieData:

    def __init__(self):

        self.data_path = os.path.join(os.getcwd(), 'DataStorage')
        self.data_unzip()
        self.datafile = pd.read_csv(os.path.join(self.data_path, 'movies_metadata.csv'), low_memory=False)
        self.ratings = pd.read_csv(os.path.join(self.data_path, 'ratings_small.csv'), low_memory=False)[['userId', 'movieId', 'rating']]
        # Create reduced dimension data set & cosine similarity matrix
        self.data, self.cosine_sim, self.tfidf_matrix = self.preprocess()
        # Construct a reverse map of indices and movie titles
        self.indices = pd.Series(self.data.index, index=self.data['title'])

    def __getattr__(self, item):
        return "Attribute does not exist."

    def preprocess(self):
        # TODO: at least get target variables from data, but clean if necessary & reduce dimension size
        # Calculate the minimum number of votes required to be in the chart (90th percentile)
        min_votes = self.datafile['vote_count'].quantile(0.90)
        # Calculate mean average vote across entire dataset ala IMDB
        mean_score = float(self.datafile['vote_average'].mean())
        # Filter out all qualified movies into a new DataFrame (about 4555 entries)
        data = self.datafile.loc[self.datafile.vote_count >= min_votes].copy()
        # Append weighted scores to new DataFrame
        data['scores'] = data.apply(lambda x: (x['vote_count']/(x['vote_count']+min_votes) *
                                              x['vote_average']) + (min_votes/(min_votes+x['vote_count']) * mean_score), axis=1)
        # Drop duplicates
        data.drop_duplicates(inplace=True)
        # Reassign indices of data
        data.reset_index(drop=True, inplace=True)
        # Convert IDs to int. Required for merging
        data['id'] = data['id'].astype('int')
        # Get keywords then merge them with movie metadata
        keywords = pd.read_csv(os.path.join(self.data_path, 'keywords.csv'))
        keywords['id'] = keywords['id'].astype('int')
        # Merge keywords into dataframe
        data = data.merge(keywords, on='id')
        data['keywords'] = data['keywords'].apply(literal_eval)
        data['keywords'] = data['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        #links_small = pd.read_csv(os.path.join(self.data_path, 'links_small.csv'), low_memory=False)
        #links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
        #data = data[data['id'].isin(links_small)]
        # print(data.shape)
        data['tagline'] = data['tagline'].fillna('')
        data['description'] = data['overview'] + data['tagline'] + data['keywords']
        data['description'] = data['description'].fillna('')
        # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')
        # Replace NaN with an empty string
        data['overview'] = data['overview'].fillna('')
        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(data['overview'])
        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return data, cosine_sim, tfidf_matrix

    def data_unzip(self):
        zip_ref = ZipFile(os.path.join(self.data_path, 'movies_metadata.zip'), 'r')
        zip_ref.extractall(self.data_path)
        zip_ref.close()


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


