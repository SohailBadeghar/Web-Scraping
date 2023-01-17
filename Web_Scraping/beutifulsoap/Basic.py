from bs4 import BeautifulSoup
import requests
# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title)

# for link in soup.find_all('a'):
#     print(link.get('href'))

html_doc = """
<html><head><title>Tutorials Point</title></head>
<body>
<p class="title"><b>The Biggest Online Tutorials Library, It's all Free</b></p>
<p class="prog">Top 5 most used Programming Languages are:
<a href="https://www.tutorialspoint.com/java/java_overview.htm" class="prog" id="link1">Java</a>,
<a href="https://www.tutorialspoint.com/cprogramming/index.htm" class="prog" id="link2">C</a>,
<a href="https://www.tutorialspoint.com/python/index.htm" class="prog" id="link3">Python</a>,
<a href="https://www.tutorialspoint.com/javascript/javascript_overview.htm" class="prog" id="link4">JavaScript</a> and
<a href="https://www.tutorialspoint.com/ruby/index.htm" class="prog" id="link5">C</a>;
as per online survey.</p>
<p class="prog">Programming Languages</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# If you want the <head> tag
print(soup.head)

print( soup.title)

# To get all the tag’s attribute, you can use find_all() method −
print( soup.find_all("a"))

# To get specific tag (like first <b> tag) in the <body> tag.
print(soup.body.b)

# Using a tag name as an attribute will give you only the first tag by that name −
print(soup.a)


print(len(soup.contents))
