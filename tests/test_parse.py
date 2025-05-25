from bs4 import BeautifulSoup
from app.parse import get_links, get_paragraph_from_page_soup, is_link_relevant

def test_get_paragraph_from_page_soup():
    html = """
    <div>
        <p>This paragraph has no attributes.</p>
        <p class="intro">This paragraph has an attribute.</p>
        <p>This is another paragraph without attributes.</p>
        <span>This is a span, not a p.</span>
        <p id="id">Paragraph with id attribute</p>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = get_paragraph_from_page_soup(soup)
    assert len(paragraphs) == 2
    texts = [p.text for p in paragraphs]
    assert "This paragraph has no attributes." in texts
    assert "This is another paragraph without attributes." in texts

def test_is_link_relevant():
    # Valid links
    assert is_link_relevant("/wiki/Python")
    assert is_link_relevant("/wiki/Artificial_intelligence")
    # Invalid links
    assert not is_link_relevant("/wiki/File:Example.jpg")
    assert not is_link_relevant("/wiki/Python/Guide")
    assert not is_link_relevant("/w/index.php?title=Python")

def test_get_links():
    html = """
    <div>
        <p>This is a <a href="/wiki/Python">link to Python</a> and <a href="/wiki/JavaScript">JavaScript</a>.</p>
        <p class="intro">Ignored paragraph attribute <a href="/wiki/File:Image.jpg">file link</a></p>
        <p>Another paragraph with a <a href="/wiki/AI">AI link</a>.</p>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = get_paragraph_from_page_soup(soup)
    links = get_links(paragraphs)
    assert "Python" in links
    assert "JavaScript" in links
    assert "AI" in links
    assert "File:Image.jpg" not in links