# JBNU AI Competition

본 저장소는 전북대학교에서 진행한 **AI 경진대회** 참가를 위한 프로젝트 코드 및 결과물을 정리한 공간입니다.

---

## 📌 대회 개요

- **대회명**: JBNU AI Competition
- **주제**: 생성형 AI와 사람이 작성한 텍스트 분류 모델 개발
- **기간**: 2025.05 ~ 2025.06
- **주최**: 전북대학교

---

## 🧠 문제 설명

사용자로부터 입력받은 텍스트가 **사람이 쓴 글인지**, **AI가 쓴 글인지** 분류하는 자연어 처리 모델을 개발합니다.

---

## 🛠 기술 스택

- Python 3.x
- Transformers (Hugging Face)
- PyTorch
- scikit-learn
- pandas, numpy

---

## 📂 프로젝트 구조

```bash
├── config.py                # 하이퍼파라미터 설정
├── data_loader.py          # 데이터 로딩 및 전처리
├── tokenizer.py            # 토크나이저 설정
├── model.py                # 모델 정의
├── train.py                # 학습 루프
├── predict.py              # 추론 및 결과 저장
├── submit.py               # 제출 파일 생성
├── main.py                 # 전체 실행 파이프라인
├── requirements.txt        # 의존 패키지 목록
└── README.md               # 현재 문서
