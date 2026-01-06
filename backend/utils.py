def aggregate_risk(model_prob, semantic_score, linguistic_score):
    final_risk = (
        0.45 * model_prob
        + 0.4 * (1 - semantic_score)
        + 0.15 * linguistic_score
    )
    if final_risk < 0.3:
        label = "Low"
    elif final_risk < 0.6:
        label = "Medium"
    else:
        label = "High"

    return round(final_risk, 3), label
