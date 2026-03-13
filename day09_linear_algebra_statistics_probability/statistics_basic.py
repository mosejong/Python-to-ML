# day09_statistics_basic.py

# ============================================
# 통계 기초
# - 평균 (mean)
# - 중앙값 (median)
# - 최빈값 (mode)
# - 분산 (variance)
# - 표준편차 (standard deviation)
# ============================================

import statistics


# 1. 데이터
data = [1, 5, 2, 6, 10]

print("data =", data)
print()


# 2. 평균 (Mean)
mean_value = statistics.mean(data)

print("평균 (mean)")
print(mean_value)
print()


# 3. 중앙값 (Median)
median_value = statistics.median(data)

print("중앙값 (median)")
print(median_value)
print()


# 4. 최빈값 (Mode)
print("최빈값 (mode)")
try:
    mode_value = statistics.mode(data)
    print(mode_value)
except statistics.StatisticsError:
    print("최빈값 없음")
print()


# 5. 분산 (Variance)
variance_value = statistics.variance(data)

print("분산 (variance)")
print(variance_value)
print()


# 6. 표준편차 (Standard Deviation)
std_value = statistics.stdev(data)

print("표준편차 (standard deviation)")
print(std_value)
print()


# 7. 이상치 예시
data_outlier = [1, 2, 3, 4, 100]

print("이상치 예시")
print("data =", data_outlier)
print("mean =", statistics.mean(data_outlier))
print("median =", statistics.median(data_outlier))