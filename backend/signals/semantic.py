from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model = SentenceTransformer("all-MiniLM-L6-v2")
def semantic_consistency_score(text: str) -> float:
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 10]

    if len(sentences) < 2:
        return 1.0  # single sentence = consistent

    embeddings = model.encode(sentences)
    sims = cosine_similarity(embeddings)

    upper = sims[np.triu_indices(len(sentences), k=1)]
    return float(np.mean(upper))
