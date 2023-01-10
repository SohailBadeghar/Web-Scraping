import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
product_prices = []
product_description = []
product_review = []
for i in range(1):
    url = "https://www.amazon.in/s?k=mobile+under+40000&crid=1GRSVP7YYZ2VB&sprefix=mobile+under+40000%2Caps%2C368&ref=nb_sb_noss_" + str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    print(soup.prettify())
    # box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
