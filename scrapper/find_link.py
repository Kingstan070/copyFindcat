import requests
from bs4 import BeautifulSoup

def get_url(search_item):
    '''
    search_item : string of the search queary

    returns     : None
    '''
    url = "https://www.google.com/search?q="+search_item
    response = requests.get(url)
    doc = BeautifulSoup(response.text,"html.parser")
    mydivs = doc.find_all("div", class_="yuRUbf")
    for div in mydivs:
        print(div)
