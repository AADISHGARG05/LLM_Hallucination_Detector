# 🧠 Multi-Signal Hallucination Detection System for LLM-Generated Text

An **explainable, end-to-end machine learning system** that detects **hallucination risk** in AI-generated text using **multiple complementary signals**, including a fine-tuned BERT classifier, semantic consistency analysis, and linguistic uncertainty detection.

> ⚠️ This project **does NOT perform fact-checking or web search**.  
> Instead, it detects **hallucination patterns** learned from data.

---

## 🔗 Live Demo (Deployment)

🚀 **Deployment Link:**  
👉 *Will be updated soon*

---

## 📌 Problem Statement

Large Language Models (LLMs) such as ChatGPT, Gemini, and Claude often generate text that is:

- Fluent and confident
- Grammatically correct
- **Factually incorrect or fabricated (hallucinated)**

This is risky in domains like:
- Education
- Healthcare
- Research
- Enterprise AI systems

Most existing solutions rely on **search, RAG, or fact verification**, which are:
- Heavy to deploy
- Costly
- Infrastructure-dependent

---

## 🎯 Project Goal

To build a **lightweight, ML-driven hallucination detection layer** that:

- Works **without external search**
- Uses **learned and linguistic patterns**
- Produces an **explainable hallucination risk score**
- Can be easily integrated into real-world systems

---

## 🧠 Core Idea

> **Hallucination is not a single signal — it is a pattern.**

This system detects hallucinations by combining **multiple independent signals**, rather than relying on a single model.

---

## 🏗️ System Architecture

LLM-Generated Text
↓
Signal 1: BERT-Based Hallucination Classifier
Signal 2: Semantic Consistency Analysis
Signal 3: Linguistic Uncertainty Analysis
↓
Weighted Risk Aggregation
↓
Hallucination Risk Score (Low / Medium / High)
↓
Web UI (Flask + HTML/CSS/JS)

---

## 🔍 Hallucination Signals

### 🔹 Signal 1: ML / DL Classifier (Core Signal)

- **Model:** Fine-tuned `bert-base-uncased`
- **Datasets:**
  - HaluEval
  - TruthfulQA (converted to binary labels)
- **Output:** Probability that text is hallucinated

📌 Demonstrates **supervised ML + deep learning skills**

---

### 🔹 Signal 2: Semantic Consistency Analysis

**Intuition:**  
Hallucinated text often:
- Jumps between topics
- Lacks internal coherence
- Contains weak semantic flow

**Method:**
- Split text into sentences
- Generate sentence embeddings (Sentence-BERT)
- Compute average cosine similarity

Low consistency → higher hallucination risk

---

### 🔹 Signal 3: Linguistic Uncertainty Analysis

**Intuition:**  
Hallucinated answers often contain:
- Hedging language (`may`, `might`, `possibly`)
- Vague phrasing
- Irregular sentence structure

**Features Used:**
- Hedging word density
- Modal verb frequency
- Sentence length variance

---

## 📊 Risk Aggregation (Explainable)

Final hallucination risk is computed as a **weighted combination**:

```text
Final Risk =
0.45 × Model Probability
+ 0.40 × (1 − Semantic Consistency)
+ 0.15 × Linguistic Uncertainty
```

📂 Project Structure
llm-hallucination-detector/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   └── predict.py
│   ├── signals/
│   │   ├── semantic.py
│   │   └── linguistic.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── analyze.html
│
├── static/
│   ├── css/
│   └── js/
│
├── experiments/
│   ├── 01_data_preparation.ipynb
│   ├── 02_ml_models.ipynb
│   └── 03_bert_classifier.ipynb
│
├── trained_models/
│   ├── bert_hallucination/
│   ├── logreg.pkl
│   ├── rf.pkl
│   └── tfidf.pkl
│
├── data/
├── requirements.txt
└── README.md



👨‍💻 Author

Aadish Garg
AI / Machine Learning Enthusiast
🔗 LinkedIn: https://www.linkedin.com/in/aadish-garg/
💻 GitHub: https://github.com/AADISHGARG05
