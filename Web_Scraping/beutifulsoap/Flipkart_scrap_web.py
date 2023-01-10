import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
product_prices = []
product_description = []
product_review = []
for i in range(2,11):
    url = "https://www.flipkart.com/search?q=mobile+under+40000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    print(names)
    for i in names:
        name = i.text
        product_name.append(name)

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")

    for i in price:
        price = i.text
        product_prices.append(price)

    descriptions = box.find_all("ul", class_="_1xgFaf")

    for i in descriptions:
        desc = i.text
        product_description.append(desc)

    reviews = box.find_all("ul", class_="_1xgFaf")

    for i in reviews:
        review = i.text
        product_review.append(review)

    df = pd.DataFrame({"product_name": product_name, "product_prices": product_prices,
                      "product_description": product_description, "product_review": product_review})
    print(df)
    df.to_csv("beutifulsoap_Filpkart_mobile_under_4000.csv")
