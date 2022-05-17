# from urllib.request import urlopen

import requests # For accessing internet
import re # For formatting text
from bs4 import BeautifulSoup # To get the content and access html in interenet

def get_url(search_item):
    '''
    search_item : string of the search queary

    returns     : List of string of url
    '''
    black_list = ["google.com","google.co","google.co.in"]
    pattern = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    page = requests.get("https://www.google.com/search?q="+search_item)
    soup = BeautifulSoup(page.content,"html.parser")
    link = soup.findAll("a")
    url_lists = []
    for link in soup.find_all("a",href=re.compile(pattern)):
        url_text = (re.split(":(?=http)",link["href"].replace("/url?q=","")))[0]
        url_text = url_text.split("&sa=U&ved")[0]
        if any(word in url_text for word in black_list):
            continue
        url_lists.append(url_text)
    return url_lists

def get_content(url):
    '''
    To get the contents of the url

    url    : string containing the url

    return : a list of string containing content

    '''
    page  = requests.get(url).text
    soup  = BeautifulSoup(page, "html.parser")
    content  = []
    data = ''
    for data in soup.find_all(['p','h1','h2','h3']):
        content.append(data.get_text())
    #print(content)
    return content

#get_content("https://en.wikipedia.org/wiki/Wikipedia:How_to_be_civil")