# Wikipedia Word Frequency API

## Installation

```
pip install -r requirements.txt
```
Recommended Python version: 3.9

---

## Running the Application

Start the FastAPI server with:

```
uvicorn main:app --reload
```

The API will be accessible at: `http://127.0.0.1:8000`

---

## Interpretation

### Language
Since article names are ambiguous and the API doesn't have a language parameter the specified article must be in English. 

### Content Extraction
Both the words and links are extracted from the regular paragraphs of the article, not the entire webpage.

This is because the amount of links on a regular Wikipedia page can be extremely high, so I wanted to reduce them to a more managable amount for the API.
It also makes more sense for the word counting to always originate from free-flowing text.

### Percentile calculation
Results are filtered from the highest frequency words:
- `percentile=20` means the top 20% most frequent words
- `percentile=0` means no words
- `percentile=100` means all words

The percentiles are rounded for 2 decimals for clarity.

### Frequencies after filtering
In `/keywords`, the frequencies are still calculated based on the entire set of words, 
not just the remaining ones after the `ignore_list` and `percentile` filtering.

### Tokenization
Words can't have any non-letter characters in them.

Words that are only `1` length are removed for convenience even before the `ignore_list` is applied.

---

## Additional Notes
According to some sources the average amount of links on a Wikipedia page is around 30. 
This means that at a `depth` setting of 2, the server has to download 900 pages on average.

There is no way around it, this is going to be really slow. 
So the recommendation is to use the API at most with a `depth` of 0 or 2
(unless the starting article has unusually low amount of links).