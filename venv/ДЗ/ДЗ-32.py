from bs4 import BeautifulSoup


def get_copywriter(tag):
    whois = tag.find("div", class_="whois")
    if "Copywriter" in whois:
        return tag
    return None


f = open('index.html', encoding="utf-8").read()
soup = BeautifulSoup(f, "html.parser")
copywriter = []
row = soup.find_all("div", class_="row")
for i in row:
    cw = get_copywriter(i)
    if cw:
        copywriter.append(cw)
print(copywriter)

# row = soup.find_all("div", class_="name")
# row = soup.find_all("div",class_="row")[1].find(class_="name").text
# row = soup.find_all("div", {"data-set":"salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# все данные по копирайтерам
# print(row)

import re
from bs4 import BeautifulSoup


def get_salary(s):
    pattern = r"\d+"


res = re.search(pattern, s).group()
print(res)
f = open('index.html', encoding="utf-8").read()
soup = BeautifulSoup(f, "html.parser")
row = soup.find_all("div", {"data-set": "salary"})
for i in row:
    get_salary(i.text)

import requests

# res = requests.get("https://ru.wordpress.org")
# # print(res)
# # print(res.status_code)
# print(res.text)
