import numpy as np
from datasets import Dataset
from tokenizer import tokenize_function

def predict_labels(trainer, test_df):
    test_dataset = Dataset.from_pandas(test_df).map(tokenize_function, batched=True)
    predictions = trainer.predict(test_dataset)
    logits = predictions.predictions
    return np.argmax(logits, axis=1)