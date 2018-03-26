import requests
from requests.auth import HTTPBasicAuth

resp = requests.get(
    'http://everai.labportico.com/zips/', 
    auth=HTTPBasicAuth('scrapper', 'scrapperAI'))

from html.parser import HTMLParser



