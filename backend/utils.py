def aggregate_risk(model_prob, semantic_score, linguistic_score):
    risk = (
        0.7 * model_prob
        + 0.2 * (1 - semantic_score)
        + 0.1 * linguistic_score
    )

    if risk > 0.6:
        label = "High"
    elif risk > 0.4:
        label = "Medium"
    else:
        label = "Low"

    return risk, label
