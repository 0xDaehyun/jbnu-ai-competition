import pandas as pd

def create_submission(test_df, pred_labels, output_path="/content/submission.csv"):
    submission = pd.DataFrame({
        "id": test_df["id"],
        "label": pred_labels
    })
    submission.to_csv(output_path, index=False)
    print(f"✅ 제출 파일 생성 완료: {output_path}")