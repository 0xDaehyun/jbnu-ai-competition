# JBNU AI Competition 🤖

본 저장소는 **전북대학교 AI 경진대회**에 참가해  
생성형 AI와 사람이 작성한 텍스트를 구분하는  
분류 모델을 개발한 코드 및 결과물을 정리한 공간입니다.  
코드는 **Jupyter Notebook** 환경에서 실행되었습니다.

<aside>
**🏆 JBNU AI Competition**: 사람과 생성형 AI가 작성한 텍스트를 구분하는 분류 모델 개발

- **기간:** 2025.05 – 2025.06  
- **팀 구성:** 팀 프로젝트, 3명  
- **사용 기술:** Python, PyTorch, HuggingFace Transformers & Datasets, scikit-learn, pandas, numpy  
- **주요 기술:** HuggingFace Trainer API & XLM-RoBERTa 기반 텍스트 분류  
- **개발 방식:** `config.py` 기반 하이퍼파라미터 관리 및 자동 검증 파이프라인 구축  
- **결과 및 성과:**  
  - Private Leaderboard: **38위**, F1 Score **0.9752**  
  - Public  Leaderboard: **44위**, F1 Score **0.9712**  
</aside>

---

## 📌 대회 개요

| 항목       | 내용                      |
|------------|---------------------------|
| **대회명** | JBNU AI Competition      |
| **주제**   | 생성형 AI와 사람의 글 분류 |
| **기간**   | 2025.05 ~ 2025.06        |
| **주최**   | 전북대학교                 |

---

## 🧠 문제 정의

주어진 텍스트를 입력받아, 작성자가 **사람인지**,  
아니면 **생성형 AI인지**를 정확히 판별하는  
자연어 처리(NLP) 모델을 구축하는 것이 목표입니다.

---

## 🚀 프로젝트 특징 및 접근 방법

- **Jupyter Notebook**에서 단계별 실험 및 시각화  
- **XLM-RoBERTa 모델** 기반 Transformer 활용  
- HuggingFace의 **Trainer API**를 이용한 간편한 학습  
- 토큰화 및 패딩을 통한 균일한 입력 데이터 구성  
- Train/Test 데이터셋 분할로 안정적 검증 수행  

---

## 🛠 사용 기술 스택

| 기술                       | 용도                               |
|----------------------------|------------------------------------|
| Jupyter Notebook           | 개발 환경 및 실험 기록             |
| Python 3.x                 | 전체 코드 구현                     |
| HuggingFace Transformers   | NLP 모델 파인튜닝                  |
| HuggingFace Datasets       | 데이터셋 로드·전처리               |
| PyTorch                    | 딥러닝 모델 및 학습 구현           |
| scikit-learn               | 데이터 분할 및 평가 지표 계산      |
| pandas, numpy              | 데이터 처리 및 분석                |

---

## ⚙️ 하이퍼파라미터 설정 (`config.py`)

| 파라미터명        | 값               |
|-------------------|-----------------|
| MODEL_NAME        | xlm-roberta-base |
| MAX_LENGTH        | 256              |
| BATCH_SIZE        | 8                |
| NUM_EPOCHS        | 3                |
| LEARNING_RATE     | 2e-5             |

---
## 🎯 결과 및 성과
- Private Leaderboard: **38위**, F1 Score **0.9752**  
- Public  Leaderboard: **44위**, F1 Score **0.9712**  

---

🔗 GitHub: https://github.com/0xDaehyun/jbnu-ai-competition  
