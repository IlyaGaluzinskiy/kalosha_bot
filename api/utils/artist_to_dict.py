
import os
import pickle

from api.utils.songs_clean_lemmatize import clean_and_lemmatize




def artist_dict(name):

    if os.path.isfile('api/data/text_dict.pickle'):

        text_dict = pickle.load(open('api/data/text_dict.pickle', 'rb'))
        with open(f'api/data/songs_txts/{name}.txt', encoding='utf-8', newline='') as f:
            song = f.read()            
            text_dict[name] = clean_and_lemmatize(song)

            pickle.dump(text_dict, open('api/data/text_dict.pickle', 'wb'))
    else:

        text_dict = {}
        for filename in os.listdir(f'api/data/songs_txts'):
            if filename.endswith('.txt'):
                try:
                    with open(f'api/data/songs_txts/{filename}', encoding='utf-8', newline='') as f:
                        song = f.read()
                        text_dict[filename[:-4]] = clean_and_lemmatize(song)
                except:
                    print(filename)

        pickle.dump(text_dict, open('api/data/text_dict.pickle', 'wb'))

