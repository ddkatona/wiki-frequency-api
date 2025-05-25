from collections import Counter
from app.fetch import get_wikipedia_article_html
from app.utils import tokenize_text
from app.parse import get_paragraph_from_page_soup, get_links


# Takes an article title and returns the word counts and links in the article
def get_words_and_links(title):
    main_content_tag = get_wikipedia_article_html(title)
    # Extract p tags (excluding sidebars, lists, image descriptions, tables)
    paragraphs = get_paragraph_from_page_soup(main_content_tag)
    # Combine paragraphs into a single string
    article_text = " ".join([a.get_text() for a in paragraphs])
    tokenized_words = tokenize_text(article_text)
    return Counter(tokenized_words), get_links(paragraphs)

def get_word_counts(title, depth):
    counter = Counter()
    visited_articles = set()
    articles_to_visit = [title]
    for i in range(depth + 1):
        # print(f"Depth: {i}, Links: {len(articles_to_visit)}")
        next_layer_articles = list()
        for title in articles_to_visit:
            if title in visited_articles:
                continue
            # print(f"{title}")
            word_counts, articles = get_words_and_links(title)
            counter += word_counts
            visited_articles.add(title)
            next_layer_articles.extend(articles)
        articles_to_visit = next_layer_articles
    return counter