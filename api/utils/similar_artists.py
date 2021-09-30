import pandas as pd

# top 5 similar artists
def similiar_artists(name):
    df_art_cos = pd.read_csv('kalosha_bot/api/data/datadf_art_cos.csv')
    
    return df_art_cos[name].sort_values(ascending=False)[1:6]
    

