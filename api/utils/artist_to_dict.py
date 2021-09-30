
import os
import pickle

from songs_clean_lemmatize import clean_and_lemmatize




def artist_dict(name):

    if os.path.isfile('kalosha_bot/api/data/text_dict.pickle'):

        text_dict = pickle.load(open('kalosha_bot/api/data/text_dict.pickle', 'rb'))
        with open(f'kalosha_bot/api/data/{name}.txt', encoding='Latin', newline='') as f:
            song = f.read()
            print(song)
            
            text_dict[name] = clean_and_lemmatize(song)

            pickle.dump(text_dict, open('kalosha_bot/api/data/text_dict.pickle', 'wb'))
    else:

        text_dict = {}
        for filename in os.listdir(f'kalosha_bot/api/data'):
            if filename.endswith('.txt'):
                try:
                    with open(f'kalosha_bot/api/data/{filename}', 'rb', newline='') as f:
                        song = f.read()
                        text_dict[filename[:-4]] = clean_and_lemmatize(song)
                except:
                    print(filename)

        pickle.dump(text_dict, open('kalosha_bot/api/data/text_dict.pickle', 'wb'))



# artist_dict('The Killers')

# text_dict = pickle.load(open('C:/Users/napis/Desktop/telegrambot/kalosha_bot/api/data/text_dict.pickle', 'rb'))

# print(text_dict['Arcade Fire'])
