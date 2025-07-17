from transformers import AutoTokenizer
from config import MODEL_NAME, MAX_LENGTH

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=MAX_LENGTH)