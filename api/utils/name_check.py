import os

from dotenv import load_dotenv
import lyricsgenius as lg

load_dotenv()
API_TOKEN = os.getenv('GENIUS_TOKEN')
# number of songs
k = 10



def name_check(name):
    # if name not in names:
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, remove_section_headers=True)
        response = (genius.search_artist(name, max_songs=1, sort='popularity'))
        true_name = response.name
        return true_name

    except:
        print(f"{name} not found in Genius")
        return 'name_error'
