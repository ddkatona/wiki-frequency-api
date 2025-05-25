import re
from urllib.parse import unquote
from bs4 import Tag


# Return all p tags that don't have any attributes (these make up the wikipedia article content)
def get_paragraph_from_page_soup(page_soup: Tag) -> list[Tag]:
    return [p for p in page_soup.find('div').find_all("p", recursive=False) if not p.attrs]

def get_links(paragraphs: list[Tag]) -> list[str]:
    links = [a.get('href') for p in paragraphs for a in p.find_all('a')]
    return [unquote(link).split('/')[2] for link in links if is_link_relevant(link)]

def is_link_relevant(link: str) -> bool:
    if link is None:
        return False
    pattern = r'^/wiki/[^/:]+$'
    return re.match(pattern, link) is not None