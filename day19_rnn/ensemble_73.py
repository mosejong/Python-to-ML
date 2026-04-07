import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# =========================================================
# [데이터 구조 요약]
# ---------------------------------------------------------
# train.csv는 시간 순서대로 이어진 데이터이며,
# X00 ~ X39 : 기상청 관련 입력 변수
# Y00 ~ Y17 : 일부 센서 온도값
# Y18        : 최종 예측 대상 센서값
#
# 결측 구조를 보면
# - 앞 4320행(30일): Y00 ~ Y17 존재, Y18 결측
# - 뒤 432행(3일) : Y18 존재, Y00 ~ Y17 결측
#
# 즉, Y18만 직접 학습하려고 하면 마지막 432행밖에 활용할 수 없다.
# 그래서 이번 코드는 아래 두 가지 관점을 함께 사용했다.
#
# 1) 앞 4320행에서는 Y00 ~ Y17의 평균값(y_mean)을 대표 온도로 보고 학습
#    -> 전체적인 온도 흐름 학습
#
# 2) 뒤 432행에서는 실제 Y18을 직접 학습
#    -> Y18 센서 고유 특성 반영
#
# 최종 제출값은 두 모델의 예측을 가중 평균하여 생성
# =========================================================

# ==============================
# 1. 데이터 불러오기
# ==============================
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')
submission = pd.read_csv('./sample_submission.csv')

# ==============================
# 2. 대표 온도(y_mean) 학습용 데이터 준비
# ==============================
# 앞 4320행은 Y18은 없지만 Y00 ~ Y17은 존재하므로
# 여러 센서의 평균을 대표 온도로 만들어 학습에 사용
mean_train = train.iloc[:4320].copy().reset_index(drop=True)
mean_test = test.copy().reset_index(drop=True)

# 시간대 주기 정보를 반영하기 위한 변수
# 하루 단위를 144개 구간으로 보고 순환하는 시간 인덱스 생성
mean_train['time_mod_144'] = np.arange(len(mean_train)) % 144
mean_test['time_mod_144'] = np.arange(len(mean_test)) % 144

# Y00 ~ Y17 평균값 생성
sensor_cols = [f'Y{i:02d}' for i in range(18)]
mean_train['y_mean'] = mean_train[sensor_cols].mean(axis=1)

# 대표 온도 예측에 사용한 입력 변수
# 중요도 확인 후 성능이 좋았던 변수들만 사용
mean_features = [
    'X32', 'X00', 'X31', 'X07', 'X12',
    'X28', 'X20', 'X30', 'time_mod_144', 'X11'
]

X_mean_train = mean_train[mean_features]
y_mean_train = mean_train['y_mean']
X_mean_test = mean_test[mean_features]

# ==============================
# 3. Y18 직접 예측용 데이터 준비
# ==============================
# 뒤 432행은 실제 Y18 값이 존재하므로
# 이 구간에서는 Y18을 직접 학습하는 모델을 따로 만든다.
direct_train = train.iloc[4320:].copy().reset_index(drop=True)
direct_test = test.copy().reset_index(drop=True)

# 동일한 방식으로 시간 정보 추가
direct_train['time_mod_144'] = np.arange(len(direct_train)) % 144
direct_test['time_mod_144'] = np.arange(len(direct_test)) % 144

# Y18 직접 예측에서 성능이 좋았던 핵심 변수만 사용
direct_features = ['X38', 'X20', 'X11', 'X30', 'time_mod_144']

X_direct_train = direct_train[direct_features]
y_direct_train = direct_train['Y18']
X_direct_test = direct_test[direct_features]

# ==============================
# 4. 모델 정의
# ==============================
# 대표 온도 예측 모델
mean_model = RandomForestRegressor(
    n_estimators=700,
    max_depth=6,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features=4,
    random_state=42,
    n_jobs=-1
)

# Y18 직접 예측 모델
direct_model = RandomForestRegressor(
    n_estimators=700,
    max_depth=6,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features=3,
    random_state=42,
    n_jobs=-1
)

# ==============================
# 5. 학습
# ==============================
mean_model.fit(X_mean_train, y_mean_train)
direct_model.fit(X_direct_train, y_direct_train)

# ==============================
# 6. 예측
# ==============================
pred_mean = mean_model.predict(X_mean_test)         # 전체적인 온도 흐름 예측
pred_direct = direct_model.predict(X_direct_test)   # Y18 직접 예측

# ==============================
# 7. 앙상블
# ==============================
# 대표 온도 기반 예측에 더 큰 비중을 두고,
# direct 예측을 보정값처럼 섞어서 최종 예측 생성
final_pred = 0.7 * pred_mean + 0.3 * pred_direct

# ==============================
# 8. 제출 파일 저장
# ==============================
submission['Y18'] = final_pred
submission.to_csv('./submission_blend.csv', index=False)

print('submission_blend.csv 저장 완료')
print(submission.head())

## 모델 아이디어
#
#이 데이터는 `Y18`의 실제값이 마지막 432행에만 존재하고, 앞 4320행에는 `Y00 ~ Y17`만 존재하는 구조이다.  
#그래서 마지막 구간만 사용하면 학습 데이터가 너무 적어지는 문제가 있다.
#
#이를 보완하기 위해,
#- 앞 4320행에서는 `Y00 ~ Y17`의 평균값을 대표 온도로 보고 전체적인 흐름을 학습하고,
#- 마지막 432행에서는 `Y18`을 직접 학습한 뒤,
#- 두 예측값을 가중 평균하여 최종 제출값을 생성했다.
#