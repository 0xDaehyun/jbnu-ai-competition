# JBNU AI Competition 🤖

본 저장소는 **전북대학교 AI 경진대회**에 참가해  
생성형 AI와 사람이 작성한 텍스트를 구분하는  
분류 모델을 개발한 코드 및 결과물을 정리한 공간입니다.

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

- **XLM-RoBERTa 모델** 기반 Transformer 활용
- HuggingFace의 **Trainer API**를 이용한 간편한 학습
- 토큰화 및 패딩을 통한 균일한 입력 데이터 구성
- Train/Test 데이터셋 분할로 안정적 검증 수행

---

## 🛠 사용 기술 스택

| 기술                | 용도                    |
|---------------------|-------------------------|
| Python 3.x          | 전체 코드 구현          |
| HuggingFace Transformers | NLP 모델 (XLM-RoBERTa) 활용 |
| PyTorch             | 딥러닝 모델 및 학습 구현 |
| scikit-learn        | 데이터 분할 및 평가      |
| datasets            | HuggingFace 데이터 처리  |
| pandas, numpy       | 데이터 처리 및 분석      |

---

## ⚙️ 하이퍼파라미터 설정 (config.py)

| 파라미터명        | 값              |
|-------------------|----------------|
| MODEL_NAME        | xlm-roberta-base |
| MAX_LENGTH        | 256             |
| BATCH_SIZE        | 8               |
| NUM_EPOCHS        | 3               |
| LEARNING_RATE     | 2e-5            |

---

## 📂 프로젝트 구조
