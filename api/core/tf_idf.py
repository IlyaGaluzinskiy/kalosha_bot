from nltk import text
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
# ngram_range - set to collebrate the results
tfidf = TfidfVectorizer(ngram_range=(1,3))

def tf_idf():
    # need to create a dict of song texts
    
    text_dict = pickle.load(open('api/data/text_dict.pickle', 'rb'))
    tfidf_repr = tfidf.fit_transform(text_dict.values())
    artists_similarity = 1 - pairwise_distances(tfidf_repr, metric="cosine")
    dict_artist_simil = dict(zip(text_dict.keys(), artists_similarity))

    df_art_cos = pd.DataFrame(dict_artist_simil, index = text_dict.keys())
    df_art_cos.to_csv('api/data/datadf_art_cos.csv')

# text_dict = pickle.load(open('api/data/text_dict.pickle', 'rb'))
# print(text_dict['Scooter'])