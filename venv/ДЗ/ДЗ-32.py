# from bs4 import BeautifulSoup
#
#
# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# row = soup.find_all("div", class_="name")
# row = soup.find_all("div",class_="row")[1].find(class_="name").text
# row = soup.find_all("div", {"data-set":"salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# все данные по копирайтерам
# print(row)
#
# import re
# from bs4 import BeautifulSoup


# def get_salary(s):
#     pattern = r"\d+"
#
#
# res = re.search(pattern, s).group()
# print(res)
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)
#
# import requests

# res = requests.get("https://ru.wordpress.org")
# # print(res)
# # print(res.status_code)
# print(res.text)

# Парсинг данных с сайтов


# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f,
#                      "https://pitbikemarket.ru/tehnika/?utm_medium=cpc&utm_source=eLama-yandex&utm_campaign=master-tovary-top-rf&utm_content=cid|83101186|gid|5130014931|aid|13472572222|adp|no|dvc|desktop|pid|7|rid|7|did|7|pos|premium1|adn|search|crid|0|&utm_term=")
# row = soup.find_all("div", class_="index-header-kdkEW")
# print(row)
# #Do you need to install a parser library?

from bs4 import BeautifulSoup

f = open('index.html').read()
soup = BeautifulSoup(f, "https://yandex.ru/images").read
row = soup.find_all("div", class_="PopularRequestList-Item PopularRequestList-Item_pos_3")
print(row)
