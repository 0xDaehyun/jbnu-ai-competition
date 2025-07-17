from config import MODEL_NAME
from data_loader import load_data, split_data
from tokenizer import tokenize_function
from model import load_model
from train import train_model
from predict import predict_labels
from submit import create_submission
from datasets import Dataset
from transformers import AutoTokenizer

# ✅ tokenizer 정의
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def main():
    # 데이터 불러오기
    train_df, test_df = load_data("/content/drive/MyDrive/AI 경진대회/train.csv",
                                  "/content/drive/MyDrive/AI 경진대회/test.csv")

    # 데이터 나누기
    train_texts, val_texts, train_labels, val_labels = split_data(train_df)

    # HuggingFace Dataset 변환 및 토큰화
    train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels}).map(tokenize_function, batched=True)
    val_dataset = Dataset.from_dict({"text": val_texts, "label": val_labels}).map(tokenize_function, batched=True)

    # 모델 준비 및 학습
    model = load_model(MODEL_NAME, num_labels=len(set(train_labels)))
    trainer = train_model(model, tokenizer, train_dataset, val_dataset)

    # 예측 및 제출
    pred_labels = predict_labels(trainer, test_df)
    create_submission(test_df, pred_labels)


if __name__ == "__main__":
    main()