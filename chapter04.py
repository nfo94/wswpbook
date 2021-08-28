import requests
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    """
    Flexible printing function controls output
    """

    def print(self):
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.title_tag = title_tag
        self.body_tag = body_tag


def get_page(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, "html.parser")


def scrape_brookings(url):
    bs = get_page(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class": "post-body"})
    return Content(url, title, body)


url = "https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/"

content = scrape_brookings(url)
print("-" * 100)
print("Title: {}".format(content.title))
print("URL: {}\n".format(content.url))
print(content.body)
