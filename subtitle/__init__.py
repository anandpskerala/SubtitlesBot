import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://isubtitles.org"

def search_sub(query):
    r = requests.get(f"{BASE_URL}/search?kwd={query}").text
    soup = bs(r, "lxml")
    list_search = soup.find_all("div", class_="row")
    index = []
    title = []
    keywords = []

    second_soup = bs(str(list_search), 'lxml')
    headings = second_soup.find_all("h3")

    third_soup = bs(str(headings), "lxml")
    search_links = third_soup.find_all("a")

    i = 0

    for a in search_links:
        i += 1
        index.append(i)
        title.append(a.text)
        key = a.get("href").split("/")
        keywords.append(key[1])

    return index, title, keywords


def get_lang(keyword):
    url = f"{BASE_URL}/{keyword}"
    request = requests.get(url).text
    fourth_soup = bs(request, "lxml")
    filesoup = fourth_soup.find_all("table")
    fifth_soup = bs(str(filesoup), "lxml")
    table_soup = fifth_soup.find_all("a")
    language = []
    index = []
    link = []
    i = 0
    for b in table_soup:
        if b["href"].startswith("/download/"):
            i += 1
            h = b.get("href").split("/")
            buttoname = h[3]
            if buttoname not in language:
                index.append(i)
                language.append(buttoname)
                link.append(f"{BASE_URL}{b.get('href')}")
    return index, language, link
