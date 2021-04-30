from app import app
import urllib.request,json
from .models import quote
import requests

Quote =quote.Quote

#Getting the quotes base url
base_url = app.config["QOUTES_API_BASE_URL"]

def get_quotes():
    '''
    Function that gets the json response to the url request
    '''
    response=requests.get(base_url).json()
    random_quote = Quote(response.get("author"), response.get("quote"))

    return random_quote
