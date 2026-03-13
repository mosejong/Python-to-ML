# TIL - 2026.03.13

## Today I Learned

오늘은 **선형대수, 통계, 확률** 기초 개념을 학습했다.

---

# 1. Linear Algebra

## Vector
벡터는 여러 값을 하나의 구조로 표현한 것이다.

예시

[1, 5, 2, 6, 10]

원소가 5개이므로 **5차원 벡터**이다.

---

## Matrix
행렬은 행(row)과 열(column)로 이루어진 2차원 구조이다.

예시

[
[1, 2],
[3, 4]
]

위 행렬은 **2 x 2 행렬**이다.

---

## Matrix Multiplication

행렬 곱은 **앞 행렬의 열 수 = 뒤 행렬의 행 수**일 때 가능하다.

예

A = 2 x 3  
B = 3 x 2  

결과 = **2 x 2**

NumPy 예시

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

A @ B
np.dot(A,B)

---

# 2. Statistics

## Mean (평균)

평균은 **데이터 전체 합을 개수로 나눈 값**이다.

mean = sum(data) / len(data)

예

data = [1,5,2,6,10]

mean = 4.8

---

## Median (중앙값)

데이터를 **정렬했을 때 가운데 값**

예

data = [1,5,2,6,10]

정렬

[1,2,5,6,10]

median = 5

---

## Mode (최빈값)

데이터에서 **가장 많이 등장한 값**

예

data = [1,1,2,3,4]

mode = 1

---

## Variance (분산)

데이터가 **평균으로부터 얼마나 퍼져 있는지** 나타내는 값

데이터가 평균 주변에 모이면  
→ 분산 작음

데이터가 넓게 퍼지면  
→ 분산 큼

---

## Standard Deviation (표준편차)

표준편차는 **분산의 제곱근**

데이터 퍼짐 정도를 더 직관적으로 나타낸다.

정리

데이터가 평균 근처  
→ 표준편차 작음

데이터가 넓게 퍼짐  
→ 표준편차 큼

---

## Outlier (이상치)

다른 값들과 크게 차이 나는 값

예

data = [1,2,3,4,100]

평균은 크게 증가하지만  
중앙값은 크게 변하지 않는다.

그래서 데이터를 분석할 때

mean + median

둘 다 확인하는 것이 중요하다.

---

# 3. Probability

## Factorial

n! = n × (n-1) × ... × 1

예

4! = 4 × 3 × 2 × 1 = 24

파이썬 구현

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

---

## Permutation (순열)

순서 O  
중복 X

from itertools import permutations

---

## Combination (조합)

순서 X  
중복 X

from itertools import combinations

---

## Product

순서 O  
중복 O

from itertools import product

repeat 옵션 사용

---

## Combinations with Replacement

순서 X  
중복 O

from itertools import combinations_with_replacement

---

# 4. Monte Carlo Simulation

랜덤 실험을 여러 번 반복하여 확률을 계산하는 방법

for i in range(100000):

시도 횟수를 늘릴수록 결과가 실제 확률에 가까워진다.

---

# 5. Law of Large Numbers (큰 수의 법칙)

시도 횟수가 많아질수록  
실험 결과가 실제 확률에 가까워진다.

예

동전 확률

P(head) = 0.5

시도 횟수 증가

100 → 흔들림  
1000 → 안정  
10000 → 0.5 근처

---

# 6. Conditional Probability (조건부 확률)

조건부 확률 공식

P(A | B) = P(A ∩ B) / P(B)

의미

B가 발생했을 때  
A가 발생할 확률

---

# What I Felt

선형대수, 통계, 확률 개념을 정리하면서 서로 연결된다는 느낌을 받았다.

특히 확률 실험에서 시도 횟수를 늘릴수록 결과가 50%에 가까워지는 것을 보면서  
큰 수의 법칙을 직접 확인할 수 있어서 흥미로웠다.