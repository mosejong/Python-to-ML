# 2026-04-09 TIL - NLP 2

## Today I Learned
- 자연어 처리의 주요 작업(텍스트 분류, 감성 분석, 번역, 요약 등)
- 텍스트 벡터화 과정(Text Standardization, Tokenization, Vocabulary Indexing)
- Bag of Words, TF-IDF, Word2Vec, FastText, Doc2Vec 개념
- Seq2Seq의 한계와 Attention의 필요성
- Transformer에서 Query, Key, Value가 사용되는 방식

---

## 1. TextVectorization 실습

```python
from tensorflow.keras.layers import TextVectorization

texts = [
    "I love NLP",
    "NLP is fun",
    "I love deep learning"
]

vectorize_layer = TextVectorization(
    max_tokens=1000,
    output_mode="int",
    output_sequence_length=5
)

vectorize_layer.adapt(texts)

result = vectorize_layer(texts)

print(result.numpy())
print(vectorize_layer.get_vocabulary()[:10])
```

### 배운 점
- 텍스트를 자동으로 소문자화하고 토큰 단위로 나눌 수 있다.
- `adapt()`를 사용해 어휘 사전을 만든다.
- 출력 모드를 `"int"`로 설정하면 각 단어가 숫자 인덱스로 변환된다.

---

## 2. Bag of Words 실습

```python
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "I love NLP",
    "I love AI",
    "AI loves data"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

### 배운 점
- 단어 등장 횟수를 기준으로 문장을 벡터화할 수 있다.
- 단어 순서는 반영되지 않고 빈도만 반영된다.

---

## 3. TF-IDF 실습

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "I love NLP",
    "I love AI",
    "AI loves data"
]

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(docs)

print(tfidf.get_feature_names_out())
print(X.toarray())
```

### 배운 점
- 자주 등장하지만 큰 의미가 없는 단어의 가중치는 낮아진다.
- 특정 문서에서 특징적으로 등장하는 단어를 더 중요하게 반영할 수 있다.

---

## 4. Tokenization 실습

```python
from tensorflow.keras.preprocessing.text import Tokenizer

texts = [
    "맛있다",
    "맛있어요",
    "맛있었다"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

print(tokenizer.word_index)
print(tokenizer.texts_to_sequences(texts))
```

### 배운 점
- 띄어쓰기나 형태가 조금만 달라도 서로 다른 단어로 인식될 수 있다.
- 같은 의미를 가진 표현도 형태가 달라지면 다른 토큰으로 처리될 수 있음을 확인했다.
- 이런 한계를 보완하기 위해 subword 방식이 사용된다는 점을 이해했다.

---

## 5. Attention 개념 정리

### Seq2Seq의 한계
- 입력 문장을 하나의 Context Vector에만 압축하면 긴 문장에서 정보 손실이 발생할 수 있다.

### Attention의 역할
- 출력 단어를 만들 때마다 입력 문장 전체를 참고한다.
- 현재 필요한 정보에 더 집중할 수 있다.

### 핵심 요소
- **Query**: 지금 무엇이 필요한가
- **Key**: 어떤 정보가 중요한가
- **Value**: 실제 전달할 정보

---

## 6. Transformer 개념 정리
- Transformer는 Attention 메커니즘을 중심으로 동작한다.
- 문장 전체를 한 번에 보고 단어 간 관계를 파악할 수 있다.
- RNN 기반 구조보다 병렬 처리에 유리하다.

---

## 7. 느낀 점
오늘은 자연어 처리의 전처리와 임베딩 개념부터 Attention, Transformer까지 흐름을 연결해서 정리했다.  
특히 Bag of Words와 TF-IDF는 직접 코드로 보니까 차이가 더 잘 보였고, Attention은 왜 필요한지 Seq2Seq 한계와 같이 보니까 이해가 더 쉬웠다.

---

## 8. 다음에 복습할 것
- Word2Vec / FastText 차이 정리
- Query, Key, Value를 예시로 다시 설명해보기
- Transformer 구조 그림으로 복습하기