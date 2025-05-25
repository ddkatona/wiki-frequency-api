import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org/w/api.php"

def get_wikipedia_article_html(title: str):
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",
        "format": "json",
        "formatversion": 2
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    html_string = data.get("parse", {}).get("text", "")
    return BeautifulSoup(html_string, 'html.parser')