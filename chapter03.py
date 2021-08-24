from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# Web crawlers are called such because they crawl across the web. At their core is an
# element of recursion. They must retrieve page contents for a URL, examine that page
# for another URL, and retrieve that page, ad infinitum.

# Beware, however: just because you can crawl the web doesn’t mean that you always
# should. The scrapers used in previous examples work great in situations where all the
# data you need is on a single page. With web crawlers, you must be extremely consci‐
# entious of how much bandwidth you are using and make every effort to determine
# whether there’s a way to make the target server’s load easier.


# Grabs all the articles from Kevin Bacon's page
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bs = BeautifulSoup(html, "html.parser")
# articles = bs.find("div", {"id": "bodyContent"}).find_all(
#     "a", href=re.compile("^(/wiki/)((?!:).)*$")
# )
# for link in articles:
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# Randomize
random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen("http://en.wikipedia.org{}".format(article_url))
    bs = BeautifulSoup(html, "html.parser")
    return bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile("^(/wiki/)((?!:).)*$")
    )


# Keeps crawling link by link
links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)

# Avoid crawling the same page twice
pages = set()


def get_unique_links(page_url):
    global pages
    html = urlopen("http://en.wikipedia.org{}".format(page_url))
    bs = BeautifulSoup(html, "html.parser")
    for link in bs.find_all("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                # Encountered a new page
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                get_unique_links(new_page)


get_unique_links()
