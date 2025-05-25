from nltk.tokenize import WordPunctTokenizer
from collections import Counter

tokenizer = WordPunctTokenizer()

def tokenize_text(text: str) -> list[str]:
    words = tokenizer.tokenize(text)
    return [w.lower() for w in words if w.isalpha() and len(w) > 1]

def filter_ignore_list(counter: Counter, ignore_list: list[str]) -> Counter:
    ignore_set = set(word.lower() for word in ignore_list)
    return Counter({w: c for w, c in counter.items() if w not in ignore_set})

def filter_percentile(counter: Counter, percentile: int) -> Counter:
    cutoff = int(len(counter) * percentile / 100)
    return Counter(dict(counter.most_common()[:cutoff]))

def counter_to_freq_dict(counter: Counter) -> dict:
    total = sum(counter.values())
    return {
        word: {'count': count, 'percentage': round((count / total) * 100, 2)}
        for word, count in counter.most_common()
    }