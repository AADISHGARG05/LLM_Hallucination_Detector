import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

MODEL_PATH = "trained_models/distilbert_hallucination"

_tokenizer = None
_model = None

def _load_model():
    global _tokenizer, _model
    if _model is None:
        _tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
        _model = DistilBertForSequenceClassification.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float32
        )
        _model.eval()

def predict_hallucination_prob(text: str) -> float:
    _load_model()

    inputs = _tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = _model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)

    return probs[0][1].item()