from urllib.request import urlopen
from bs4 import BeautifulSoup

def make_listing(card):
        return {
                "id": card["data-card-id"],
                "title": card.find("p", class_="jorato-case-card__headline").text.strip(),
                "rent": int(card["data-rent"]),
                }


def get_current_listings(url):
    

    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("article", class_="jorato-case-card")
    return [make_listing(card) for card in cards]
