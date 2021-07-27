from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


# generic function to receive an url, try to open it and get it's title
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title.prettify())
