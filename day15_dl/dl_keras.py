import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from keras import layers
from tensorflow.keras.callbacks import EarlyStopping

train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

X = train.drop(columns=['label', 'ID'])
y = train['label']

train_X, test_X, train_y, test_y = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Keras용 전처리
train_X_nn = train_X.to_numpy().astype("float32") / 255.0
test_X_nn = test_X.to_numpy().astype("float32") / 255.0

# 라벨 인코딩
le = LabelEncoder()
train_y_nn = le.fit_transform(train_y)
test_y_nn = le.transform(test_y)

# 모델 구성
model_ke = keras.Sequential([
    layers.Input(shape=(1024,)),
    layers.Dense(512, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(10, activation="softmax")
])

model_ke.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 조기 종료
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model_ke.fit(
    train_X_nn,
    train_y_nn,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

test_loss, test_acc = model_ke.evaluate(test_X_nn, test_y_nn)
print("Keras:", test_acc)