import os
import requests

from dotenv import load_dotenv

load_dotenv()

PIXABAY_API = os.getenv('PIXABAY_API')

def img_search(message):

    URL = f"https://pixabay.com/api/?key={PIXABAY_API}&q={message}&image_type=photo"
    
    r = requests.get(URL)

    data = r.json()

    return data['hits'][8]['webformatURL']

