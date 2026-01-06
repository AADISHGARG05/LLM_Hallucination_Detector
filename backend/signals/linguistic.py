import re
import numpy as np
HEDGING_WORDS = [
    "may", "might", "possibly", "probably", "could",
    "seems", "appears", "likely", "generally", "often"
]
def linguistic_uncertainty_score(text: str) -> float:
    text = text.lower()
    words = text.split()

    hedge_count = sum(word in HEDGING_WORDS for word in words)
    hedge_ratio = hedge_count / max(len(words), 1)

    sentences = re.split(r"[.!?]", text)
    sentence_lengths = [len(s.split()) for s in sentences if len(s.split()) > 0]

    variance = np.var(sentence_lengths) if sentence_lengths else 0

    score = min(1.0, hedge_ratio * 5 + variance / 100)
    return float(score)
