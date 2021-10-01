import os

from dotenv import load_dotenv
# from joblib import Parallel, delayed

load_dotenv()
API_TOKEN = os.getenv('GENIUS_TOKEN')

def parser(name, k=10):
    c = 0 
    import lyricsgenius as lg
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True, sleep_time=1 , retries=2)
        response = genius.search_artist(name, max_songs=k, sort='popularity')
        songs = response.songs   
        s = [song.lyrics for song in songs]
        name = response.name

        with open(f"api/data/songs_txts/{name}.txt", "w", encoding='utf-8') as f:
            f.write("\n \n".join(s)) 
        c += 1
        print(f"Songs grabbed:{len(s)}")   
    except:
        print(f"some exception at {name}: {c}")

# songs = Parallel(n_jobs=20, verbose=1)(delayed(get_lyrics)(i, 10) for i in names)
