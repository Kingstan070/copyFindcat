import requests
import re
from bs4 import BeautifulSoup

def get_url(search_item):
    '''
    search_item : string of the search queary

    returns     : None
    '''
    page = requests.get("https://www.google.com/search?q="+search_item)
    soup = BeautifulSoup(page.content,"html.parser")
    link = soup.findAll("a")
    for link in soup.find_all("a",href=re.compile(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")):
        url_text = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        if "google.com" in url_text:
            continue
        print(url_text)
