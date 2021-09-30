import re

import nltk
# from nltk.corpus import stopwords # opt
# stop_words = set(stopwords.words('english')) # opt

nltk.download('punkt') # opt
from nltk.stem import WordNetLemmatizer



def clean_and_lemmatize(text):
    #cleaning
    text = text.lower()
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+',' ',text)
    text = re.sub(r'[^\w\s]','', text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub('r<.*?>',' ', text)
#     text = reg_tok.tokenize(text)
    # filtering
#     text = " ".join([word for word in text if not word in STOPWORDS and len(word) > 2])
    word_list = text.split()
    # lemmatization
    text = ' '.join([WordNetLemmatizer().lemmatize(w) for w in word_list])
#     text = text.split()
    return text