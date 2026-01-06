import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

_vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

def semantic_consistency_score(text: str) -> float:
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 5]
    if len(sentences) < 2:
        return 1.0

    tfidf = _vectorizer.fit_transform(sentences)
    sims = []

    for i in range(len(sentences) - 1):
        sim = cosine_similarity(tfidf[i], tfidf[i + 1])[0][0]
        sims.append(sim)

    return float(np.mean(sims))