from bs4 import BeautifulSoup
import requests


# 1.Fetch the pages (write the website you wish to scrape within parentheses)
result = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
# 2.Get the page content
content = result.text
# 3. Create the soup
soup = BeautifulSoup(content, "lxml")