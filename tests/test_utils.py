from app.utils import tokenize_text, filter_ignore_list, filter_percentile, counter_to_freq_dict
from collections import Counter

def test_tokenize_text():
    assert tokenize_text("This is a test! Hello, World 123. Test.") == ['this', 'is', 'test', 'hello', 'world', 'test']
    assert tokenize_text("ABC-DEF") == ['abc', 'def']
    assert tokenize_text("Hungary's population is 9.6 million.") == ['hungary', 'population', 'is', 'million']
    assert tokenize_text("remove a single character") == ['remove', 'single', 'character']
    assert tokenize_text("remove \nspecial characters") == ['remove', 'special', 'characters']

def test_filter_ignore_list():
    c1 = Counter({"apple": 2, "banana": 3, "cherry": 1})
    ignore1 = ["banana"]
    result1 = filter_ignore_list(c1, ignore1)
    assert result1 == Counter({"apple": 2, "cherry": 1})

    # Empty list
    c2 = Counter({"apple": 1, "banana": 2})
    ignore2 = []
    result2 = filter_ignore_list(c2, ignore2)
    assert result2 == c2

    # Empty counter
    c3 = Counter()
    ignore3 = ["apple"]
    result3 = filter_ignore_list(c3, ignore3)
    assert result3 == Counter()

    # Test 6: Ignore all words
    c4 = Counter({"apple": 1, "banana": 2})
    ignore4 = ["apple", "banana"]
    result4 = filter_ignore_list(c4, ignore4)
    assert result4 == Counter()


def test_filter_percentile():
    c = Counter({"apple": 5, "banana": 3, "cherry": 7, "date": 1})

    assert filter_percentile(c, 50) == Counter({"cherry": 7, "apple": 5})
    assert filter_percentile(c, 100) == c
    assert filter_percentile(c, 0) == Counter()
    assert filter_percentile(c, 25) == Counter({"cherry": 7})
    assert filter_percentile(c, 33) == Counter({"cherry": 7})

    c_empty = Counter()
    assert filter_percentile(c_empty, 50) == Counter()

def test_counter_to_freq_dict():
    c1 = Counter({"apple": 5, "banana": 3, "cherry": 2})

    result1 = counter_to_freq_dict(c1)
    expected1 = {
        "apple": {"count": 5, "percentage": 50.0},
        "banana": {"count": 3, "percentage": 30.0},
        "cherry": {"count": 2, "percentage": 20.0},
    }
    assert result1 == expected1

    c2 = Counter()
    result2 = counter_to_freq_dict(c2)
    expected2 = {}
    assert result2 == expected2

    c3 = Counter({"one": 1})
    result3 = counter_to_freq_dict(c3)
    expected3 = {"one": {"count": 1, "percentage": 100.0}}
    assert result3 == expected3