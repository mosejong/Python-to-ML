# Decision Tree vs Bagging vs Random Forest 비교 실습

# 문제

# iris 데이터셋을 사용하여 다음 모델들의 성능을 비교하시오.

# 1. DecisionTreeClassifier

# 2. BaggingClassifier (base: DecisionTree)

# 3. RandomForestClassifier

#

# 조건:

# - train_test_split(test_size=0.3, random_state=42)

# - accuracy_score 사용

#

# 목표:

# - 단일 트리 vs 앙상블(Bagging, RandomForest) 성능 비교

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.metrics import accuracy_score

# 데이터 로드

X, y = load_iris(return_X_y=True)

# 데이터 분할

train_X, test_X, train_y, test_y = train_test_split(
X, y, test_size=0.3, random_state=42
)

# 모델 생성

d_model = DecisionTreeClassifier(random_state=42)

b_model = BaggingClassifier(
estimator=DecisionTreeClassifier(),
n_estimators=10,
random_state=42
)

r_model = RandomForestClassifier(random_state=42)

# 모델 학습

d_model.fit(train_X, train_y)
b_model.fit(train_X, train_y)
r_model.fit(train_X, train_y)

# 예측

pred_d = d_model.predict(test_X)
pred_b = b_model.predict(test_X)
pred_r = r_model.predict(test_X)

# 성능 평가

print(f"Decision Tree 정확도 : {accuracy_score(test_y, pred_d):.4f}")
print(f"Bagging 정확도 : {accuracy_score(test_y, pred_b):.4f}")
print(f"Random Forest 정확도 : {accuracy_score(test_y, pred_r):.4f}")

# 결론:

# iris 데이터셋은 비교적 단순한(EZ한) 데이터이기 때문에

# 대부분의 모델에서 높은 성능을 보인다.

# 따라서 모델 간 성능 차이가 크게 나타나지 않을 수 있다.
