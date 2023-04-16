import requests
from bs4 import BeautifulSoup


def get_data(html):
    soup = BeautifulSoup(html,"lxml") #"html.parser"
    p2 = soup.find_all("div",class_="ad-block")


def get_html(url):
    res = requests.get(url)
    return res.text


def main():
    url = "https://www.bnkomi.ru/"

    if __name__ == '__name__':
        main()
