# 📅 2026-03-25 (Day13 - ML: Clustering)

## 📌 오늘 배운 내용

### 1. 비지도학습 (Unsupervised Learning)

* 정답(label)이 없는 데이터를 학습하는 방법
* 데이터의 구조나 패턴을 스스로 찾음

---

### 2. 클러스터링 (Clustering)

* 유사한 데이터끼리 그룹(군집)으로 묶는 방법

#### ✔ 목표

* **군집 내 유사성 최대화**
* **군집 간 유사성 최소화**

---

### 3. 클러스터링 종류

* **하드 클러스터링**

  * 데이터가 특정 군집에 속함 (0 또는 1)
* **소프트 클러스터링**

  * 여러 군집에 속할 확률로 표현 (0~1 사이 값)

---

## 💻 실습 (KMeans)

```python
from sklearn.cluster import KMeans

X = [
    [2, 3],
    [3, 4],
    [10, 10],
    [11, 11],
    [1, 0]
]

model = KMeans(n_clusters=2)
model.fit(X)

print("labels:", model.labels_)
print("centers:", model.cluster_centers_)
```

---

## 🔍 클러스터 개수 결정 (Elbow Method)

* `inertia_` 값을 이용해 적절한 k값 선택
* k가 증가할수록 inertia는 감소하지만,
  특정 지점 이후 감소폭이 줄어듦

```python
for k in range(1, 6):
    model = KMeans(n_clusters=k)
    model.fit(X)
    print(k, model.inertia_)
```

👉 결과 해석

* k=1 → k=2 : 큰 폭 감소
* k=2 → 이후 : 감소폭 작음

➡️ **최적의 클러스터 수 = 2**

---

## 🧠 핵심 개념 정리

* `labels_` : 각 데이터의 군집 번호
* `cluster_centers_` : 각 군집의 중심 좌표
* `inertia_` : 군집 내 거리의 합 (작을수록 좋음)

---

## 🤔 느낀 점

* 단순히 코드 실행보다 **데이터가 왜 이렇게 나뉘는지 이해하는 것이 중요**
* 클러스터 개수(k)를 어떻게 정하느냐가 결과에 큰 영향을 줌
* 이상치(outlier)가 있을 경우 군집 결과가 달라질 수 있음

---

## 🔥 한 줄 정리

👉 클러스터링은 비슷한 데이터끼리 자동으로 묶어 패턴을 찾는 방법이며, k값 선택이 핵심이다.
