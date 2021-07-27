from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, "html.parser")
nameList = bs.find_all("span", {"class": "green"})
print(type(nameList))

for name in nameList:
    print(name.get_text())

headers = bs.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
print("headers: ", headers)
colors = bs.find_all("span", {"class": {"green", "red"}})
print("colors: ", colors)

prince = bs.find_all(text="the prince")
print("prince: ", prince)
title = bs.find(id="title")
print("title: ", title)

# Navigating the HTML tree
tree = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs2 = BeautifulSoup(tree, "html.parser")
print(bs2.prettify())

for child in bs2.find("table", {"id": "giftList"}).children:
    print(child)

for sibling in bs2.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

parent = bs2.find(
    "img", {"src": "../img/gifts/img1.jpg"}
).parent.previous_sibling.get_text()
print(parent)

# Using regex
images = bs2.find_all("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for img in images:
    print(img["src"])

# Attributes
imgs = bs2.img.attrs["src"]
print("imgs")

# Lambda expressions
two_attrs = bs2.find_all(lambda tag: len(tag.attrs) == 2)
print(two_attrs)
print(bs2.find_all(lambda tag: tag.get_text() == "Or maybe he's only resting?"))
