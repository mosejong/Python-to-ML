#pip install scikit-learn
'''
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.random.randint(0, 10, 50)    # 데이터
y = np.random.randint(0, 2, 50)     # 답안지, 라벨, 타겟
print(x[:10])
print(y[:10])
    #test_size 0.2는 트레인셋이 80% 테스트셋이 20% 즉 위에서 50개중 40개가 트레인(학습), 테스트(문제풀이) 10개
train_x, test_x, train_y, test_y = train_test_split(x,y, test_size=0.2, random_state=2026)
print(train_x[:10], test_x[:10], len(train_x), len(test_x))
print(train_y[:10], test_y[:10], len(train_y), len(test_y))
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'age': [20, 22, 25, 28, 30],
    'salary': [2000, 2500, 3000, 3500, 4000]
}

df = pd.DataFrame(data)

X = df[['age']]
y = df['salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)
print(X_test)
print(pred)