# day09_linear_algebra_basic.py

# ============================================
# 선형대수 기초
# 1) 벡터의 차원 = 원소의 개수
# 2) 벡터 덧셈 = 같은 위치끼리 더함
# 3) 스칼라곱 = 모든 원소에 같은 수를 곱함
# 4) 내적 = 같은 위치 원소를 곱해서 전부 더함
# 5) 행렬 크기 = 행 x 열
# ============================================


# 1. 벡터와 차원
vector_a = [1, 5, 2, 6, 10]

print("1. 벡터와 차원")
print("vector_a =", vector_a)
print("차원 =", len(vector_a))   # 원소 개수 = 차원
print()


# 2. 벡터 덧셈
vector_b = [2, 1, 3, 4, 5]

vector_add = []
for i in range(len(vector_a)):
    vector_add.append(vector_a[i] + vector_b[i])

print("2. 벡터 덧셈")
print("vector_a =", vector_a)
print("vector_b =", vector_b)
print("vector_a + vector_b =", vector_add)
print()


# 3. 스칼라곱
scalar = 3
scalar_result = []

for num in vector_a:
    scalar_result.append(num * scalar)

print("3. 스칼라곱")
print("scalar =", scalar)
print("vector_a * scalar =", scalar_result)
print()


# 4. 내적(dot product)
dot_product = 0

for i in range(len(vector_a)):
    dot_product += vector_a[i] * vector_b[i]

print("4. 내적")
print("vector_a · vector_b =", dot_product)
print()


# 5. 행렬(matrix)
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix_a)
cols = len(matrix_a[0])

print("5. 행렬")
print("matrix_a =", matrix_a)
print("행 개수 =", rows)
print("열 개수 =", cols)
print("행렬 크기 =", rows, "x", cols)
print()


# 6. 3x3 행렬 예시
matrix_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows_b = len(matrix_b)
cols_b = len(matrix_b[0])

print("6. 3x3 행렬 예시")
print("matrix_b =", matrix_b)
print("행렬 크기 =", rows_b, "x", cols_b)
print()


# 7. 정리 출력
print("7. 핵심 정리")
print("- 벡터의 차원 = 원소 개수")
print("- 벡터 덧셈 = 같은 위치 원소끼리 더하기")
print("- 스칼라곱 = 벡터의 모든 원소에 같은 수 곱하기")
print("- 내적 = 대응 원소끼리 곱한 뒤 모두 더하기")
print("- 행렬 크기 = 행 x 열")