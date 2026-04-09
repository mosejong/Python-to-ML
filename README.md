# Python-to-AI

Python 기초부터 머신러닝, 딥러닝, AI 프로젝트까지 학습 과정을 기록하는 저장소입니다.  
AI Human 교육 과정을 기반으로, 매일 학습한 내용과 복습 코드, 실습 내용을 정리하고 있습니다.

---

## 📌 About

이 저장소는 단순 코드 저장이 아니라  
**학습 흐름 (Python → ML → DL → AI)** 을 기록하는 것을 목표로 합니다.

- 직접 작성한 코드 중심
- 복습 기반 학습 기록
- 개념 + 실습 함께 정리
- 시행착오와 디버깅 과정까지 기록

이 저장소는 학습 과정 속에서 직접 구현한 코드와 복습 기록을 함께 정리하는 공간입니다.

---

## 🛠 Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras
- PyTorch
- Git / GitHub

---

## 🚀 Projects

- **Day20 API Project** : 공공데이터 API 호출, 페이지네이션 처리, 지도 시각화 실습
- **Day21 Chatbot Project** : 텍스트 전처리 기반 챗봇 구현
- **공공데이터 분석 프로젝트** : 지역 데이터 기반 분석 및 활용 아이디어 확장

---

## 📚 Learning Log

| Day   | Topic |
|------|------|
| Day02 | Python 기본 문법 |
| Day03 | 클래스 / 상속 |
| Day04 | 미니 게임 구현 |
| Day05 | 문제 풀이 |
| Day06 | 파일 처리 |
| Day07 | Git / GitHub |
| Day08 | NumPy |
| Day09 | 선형대수 / 통계 |
| Day10 | 전처리 / 시각화 |
| Day11 | 머신러닝 입문 |
| Day12 | 데이터 분석 |
| Day13 | 클러스터링 / PCA |
| Day14 | Decision Tree / Ensemble |
| Day15 | Deep Learning 기초 / Perceptron |
| Day16 | TensorFlow와 MLP 기초 학습 |
| Day17 | 딥러닝 개념과 CNN 기초 학습 |
| Day18 | 이미지 데이터 이해와 PyTorch 파이프라인 구현 |
| Day19 | 순차 데이터와 RNN 기초 / 온도 예측 앙상블 실험 |
| Day20 | OpenAPI 기초, 공공데이터 API 호출, 페이지네이션, 지도 시각화(folium) |
| Day21 | NLP 기초 / 텍스트 전처리 / 챗봇 프로젝트 |
| Day22 | NLP 심화 / Naive Bayes 감정 분석 / 문장 및 문서 유사도(Cosine Similarity) |
| Day23 | NLP 심화: Seq2Seq + Attention 번역 모델 구현 및 성능 최적화 |

---

## 📂 Structure

```text
Python-to-AI/
├── day02/
├── day03/
├── day04/
├── day05/
├── day06/
├── day07/
├── day08_numpy/
├── day09_linear_algebra_statistics_probability/
├── day10_practice/
├── day11_ml/
├── day12/
├── day13_ml/
├── day14_ml/
├── day15_dl/
├── day16_dl/
├── day17_dl_cnn/
├── day18_pytorch/
├── day19_rnn/
├── day20_api/
├── day21_chatbot/
├── day22_nlp_advance/
├── day23_attention_nmt/
└── README.md
```

---

## 🔥 Recent Update

### Day 23: NLP Deep-Dive (Embedding to Attention Mechanism)

단순한 텍스트 처리를 넘어, 자연어 처리 모델의 발전 흐름과 데이터 수치화(Embedding), 그리고 최신 아키텍처의 핵심인 Attention 메커니즘을 심도 있게 학습했습니다.

#### 🔹 텍스트 벡터화 및 임베딩 (Text Vectorization & Embedding)
- **임베딩 기법의 진화**: 
  - **BoW & TF-IDF**: 통계적 기법을 통해 문장 내 키워드 가중치를 산출하는 법을 학습.
  - **Word2Vec & Fasttext**: 주변 맥락(Context) 기반의 추론 임베딩 이해. 특히 Fasttext의 자모 단위 분석을 통한 한국어 오타 대응 성능 확인.
  - **Subword Tokenization**: BPE(Byte Pair Encoding) 등을 통해 미등록 단어(OOV) 문제를 해결하는 전략 파악.

#### 🔹 Attention 메커니즘 ★ (Core Mechanism)
- **발전 흐름**: 규칙 기반 → 통계 기반(HMM, CRF) → 딥러닝 기반(RNN/LSTM → Attention) 변천사 정리.
- **Seq2Seq의 한계 극복**: 고정된 Context Vector의 정보 손실 문제를 해결하기 위해 디코더가 인코더의 특정 상태에 집중하게 만드는 Attention 구현.
- **Query, Key, Value 원리**: 
  - **Query**(요청)와 **Key**(핵심)를 내적(Dot-product)하여 **Attention Score** 산출.
  - 스코어 기반으로 **Value**(내용)를 가중합(Weighted Sum)하여 최종 문맥 벡터를 생성하는 전 과정 실습.

#### 🛠️ 실전 트러블슈팅 (Trouble Shooting)
- **성능 최적화**: 대용량 데이터 전처리 시 파이썬 루프의 병목 현상을 해결하기 위해 `lookup_indices`를 적용, **전처리 속도를 7분에서 7초로 100배 개선**.
- **환경 및 버전 대응**: `torchtext` 버전 파편화 이슈를 특수 토큰 수동 주입 로직으로 해결하며 개발 환경 호환성의 중요성 체감.

---

## 📖 Study Rule

* 매일 학습 내용 기록
* 직접 코드 작성
* 복습 후 정리
* GitHub 업로드

---

## 📝 Note

프로젝트 진행이나 복습 과정으로 인해
업로드 간격이 일정하지 않을 수 있습니다.

단순 진도를 나가는 것보다,
**이해하고 다시 정리하는 학습**을 목표로 하고 있습니다.

---

## 👨‍💻 Author

* GitHub: [mosejong](https://github.com/mosejong)