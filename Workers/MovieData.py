
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from zipfile import ZipFile
from ast import literal_eval
from nltk.stem.snowball import SnowballStemmer
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
        # Strip out 'name' from keywords
        data['keywords'] = data['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        # Remove keywords that occur only once
        s = data.apply(lambda x: pd.Series(x['keywords']), axis=1).stack().reset_index(level=1, drop=True)
        s.name = 'keyword'
        s = s.value_counts()
        d = s[s == 1]
        data['keywords'] = data['keywords'].apply(lambda x: (i for i in x if i not in d))
        # Replace NaN with an empty string
        data['overview'] = data['overview'].fillna('')
        data['tagline'] = data['tagline'].fillna('')
        # see about genre...
        data['genres'] = data['genres'].fillna('[]').apply(literal_eval).apply(
            lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        # Convert values to strings for concatenation
        data['keywords'] = data['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
        data['tagline'] = data['tagline'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
        data['overview'] = data['overview'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
        # Stem
        data['wordsalad'] = data['overview'] + data['tagline'] + data['keywords'] + data['genres']
        data['wordsalad'] = data['wordsalad'].fillna('')
        data['wordsalad'] = data['wordsalad'].apply(lambda x: ' '.join(x))
        # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')
        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(data['wordsalad'])
        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return data, cosine_sim, tfidf_matrix

    def filter_keywords(self, s):
        words = []
        for i in self:
            if i in s:
                words.append(i)
        return words

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


