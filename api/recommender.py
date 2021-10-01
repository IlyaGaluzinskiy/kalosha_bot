# import sys
# sys.path.append('c:\\Users\\napis\\Desktop\\PythonDS\\Projects\\FlaskTest\\flask_test\\api\\utils')
# sys.path.append('c:\\Users\\napis\\Desktop\\PythonDS\\Projects\\FlaskTest\\flask_test\\api\\core')

import pandas as pd

from api.utils.name_check import name_check
from api.utils.similar_artists import similiar_artists
from api.utils.artist_to_dict import artist_dict
from api.core.parser import parser
from api.core.tf_idf import tf_idf




def rec_music(name):
    
    try:
        checked_name = name_check(name)
        # pd series with artist for those we have lyrics
        exist_authors = pd.read_csv('api/data/exist_artists.csv')

        if checked_name in exist_authors.values:
            return similiar_artists(checked_name)
    
        else:
            # parser - song texts
            parser(checked_name)
            print('Parser end')
            # time.sleep(3.)
            artist_dict(checked_name)
            print('artist_dict done')
            tf_idf()
            print('tf_idf is done')
            # add artist to artists data file
            exist_authors.loc[exist_authors.index.max() + 1] = checked_name
            exist_authors.to_csv('api/data/exist_artists.csv')

            return similiar_artists(checked_name)

    except:
        print('Something wrong with rec_music')


# print(rec_music('scooter'))

