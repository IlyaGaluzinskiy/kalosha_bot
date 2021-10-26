# from lyricsgenius.api.public_methods import artist
import pandas as pd

def artist_list(l = 10):
    text_dict = pd.read_csv('api\data\exist_artists.csv')
    artists = text_dict['author']
    return artists[:len(artists) -1]

