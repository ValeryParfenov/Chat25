from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "gpt2"

_tokenizer = None
_model = None

def _load_model():
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return _tokenizer, _model


def generate_response(prompt: str, max_new_tokens: int = 40) -> str:
    tokenizer, model = _load_model()
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text
