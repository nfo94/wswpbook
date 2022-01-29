from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def get_courses(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        courses = bs.find_all("a", attrs={"class": "product-item-link"})
        for a in courses:
            print(f'Curso: {a["title"]}')
    except AttributeError as e:
        return None


courses = get_courses("https://loja.unifacsonline.com.br/graduacao")
