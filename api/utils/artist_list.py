# from lyricsgenius.api.public_methods import artist
import pandas as pd
import random

def artist_list(l = 20):
    text_dict = pd.read_csv('api\data\exist_artists.csv')
    artists = text_dict['author']
    number = random.randint(0, len(artists) - l + 1)
    return artists[number:number+l]

