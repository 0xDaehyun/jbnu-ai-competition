import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(train_path, test_path):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def split_data(train_df):
    return train_test_split(
        train_df["text"].tolist(), train_df["label"].tolist(), test_size=0.2, random_state=42
)