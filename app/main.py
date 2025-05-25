from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, conint
from app.core import get_word_counts
from app.utils import counter_to_freq_dict, filter_ignore_list, filter_percentile

app = FastAPI(
    title="Wikipedia Word-Frequency API",
    description="Traverse Wikipedia articles to compute word frequencies",
    version="1.0.0"
)

class KeywordRequest(BaseModel):
    article: str
    depth: conint(ge=0)
    ignore_list: list[str]
    percentile: conint(ge=0, le=100)

@app.get("/word-frequency")
def word_frequency(article: str = Query(..., description="Title of starting article"),
                     depth: int = Query(0, ge=0, description="Search depth")):
    try:
        word_counts = get_word_counts(article, depth)
        word_freq_dict = counter_to_freq_dict(word_counts)
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error")
    return word_freq_dict

@app.post("/keywords")
def keywords(request: KeywordRequest):
    try:
        word_counts = get_word_counts(request.article, request.depth)
        word_counts = filter_ignore_list(word_counts, request.ignore_list)
        word_counts = filter_percentile(word_counts, request.percentile)
        word_freq_dict = counter_to_freq_dict(word_counts)
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error")
    return word_freq_dict