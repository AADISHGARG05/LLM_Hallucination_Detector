import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from model.predict import predict_hallucination_prob
from signals.semantic import semantic_consistency_score
from signals.linguistic import linguistic_uncertainty_score
from utils import aggregate_risk


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze-page")
def analyze_page():
    return render_template("analyze.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    text = data.get("text", "")

    if not text or len(text.strip()) < 20:
        return jsonify({
            "error": "Input text must be at least 20 characters long."
        }), 400

    # --- Lazy-loaded inference ---
    model_prob = predict_hallucination_prob(text)
    semantic_score = semantic_consistency_score(text)
    linguistic_score = linguistic_uncertainty_score(text)

    # --- Risk aggregation ---
    final_risk, label = aggregate_risk(
        model_prob,
        semantic_score,
        linguistic_score
    )

    return jsonify({
        "hallucination_risk": round(final_risk, 3),
        "risk_label": label,
        "signals": {
            "model_probability": round(model_prob, 3),
            "semantic_consistency": round(semantic_score, 3),
            "linguistic_uncertainty": round(linguistic_score, 3)
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )