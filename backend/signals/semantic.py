from sentence_transformers import SentenceTransformer
import numpy as np

_model = None

def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def semantic_consistency_score(text: str) -> float:
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 5]
    if len(sentences) < 2:
        return 1.0

    model = _get_model()
    embeddings = model.encode(sentences)

    sims = []
    for i in range(len(embeddings) - 1):
        sim = np.dot(embeddings[i], embeddings[i+1]) / (
            np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[i+1])
        )
        sims.append(sim)

    return float(np.mean(sims))