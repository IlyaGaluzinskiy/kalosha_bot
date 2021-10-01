import pandas as pd

# top 5 similar artists
def similiar_artists(name):
    df_art_cos = pd.read_csv('api/data/datadf_art_cos.csv', index_col=0)
    
    return df_art_cos[name].sort_values(ascending=False)[1:6]
    

# df_art_cos = pd.read_csv('api/data/datadf_art_cos.csv', index_col=0)
# print(df_art_cos.head())
