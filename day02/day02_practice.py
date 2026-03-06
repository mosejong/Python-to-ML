# ==============================
# Python 연습 - Day 02
# ==============================

# ------------------------------
# 문제 1: 가장 점수가 높은 학생 찾기
# ------------------------------

students = [
    {"name": "민수", "score": 75},
    {"name": "지연", "score": 92},
    {"name": "철수", "score": 88},
    {"name": "영희", "score": 60},
    {"name": "가영", "score": 95}
]

best_score = students[0]["score"]
best_name = students[0]["name"]

for st in students:
    if st["score"] > best_score:
        best_score = st["score"]
        best_name = st["name"]

print("최고 점수 학생:", best_name, best_score)


# ------------------------------
# 문제 2: 짝수만 더하기 (리스트 컴프리헨션)
# ------------------------------

numbers = [3, 7, 2, 9, 12, 15, 8]

even_sum = sum(x for x in numbers if x % 2 == 0)

print("짝수 합:", even_sum)


# ------------------------------
# 문제 3: 10 이상 숫자 리스트 만들기
# ------------------------------

over_ten = [x for x in numbers if x >= 10]

print("10 이상 숫자:", over_ten)


# ------------------------------
# 문제 4: 평균 구하기
# ------------------------------

average = sum(numbers) / len(numbers)

print("평균:", average)