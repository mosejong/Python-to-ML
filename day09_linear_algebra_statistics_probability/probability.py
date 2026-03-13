# 팩토리얼 (!) !n = 1부터 n까지의 곱
def fac(n) :
    if n == 0: 
        return 1
    else :
        return n * fac(n-1) # 재귀함수활용
print(fac(4))

from itertools import permutations          # 순서 적용 , 중복 X
from itertools import combinations          # 순서 X, 중복 X
from itertools import product               # 순서와 중복 둘다 적용
from itertools import combinations_with_replacement     #중복만 적용

#순서 상관있고 1~6 숫자중 3번 고르는 경우
print(len(list(permutations([1,2,3,4,5],3))))
#순서 상관없고 1~6 숫자중 3번 고르는 경우
print(len(list(combinations([1,2,3,4,5],3))))
#순서 상관있고 1~6 숫자중 중복가능하게 3번 고르는 경우
print(len(list(product([1,2,3,4,5],repeat=3))))
#순서 상관없고 1~6 숫자중 중복가능하게 3번 고르는 경우.
print(len(list(combinations_with_replacement([1,2,3,4,5],3))))
# product에서 repeat 기억하기...


import random
answer_Q1andQ2 = 0
answer_Q2 = 0
answer_Q1orQ2 = 0
answer_Q1 = 0
random.seed(1000)

# 함수 정의 
def random_answer():
    return random.choice(["A", "B"])

# 30명의 응답 결과
for i in range(100000): #시도 횟수
    Q1 = random_answer()
    Q2 = random_answer()
    if Q2 == "A":
        answer_Q2 += 1
    if Q2 == "A" and Q1 == "A":
        answer_Q1andQ2 += 1
    if Q2 == "A" or Q1 == "A":
        answer_Q1orQ2 += 1
        
# 조건부 확률과 독립
print( "P(B|A):", answer_Q1andQ2/answer_Q2)
print( "P(B|O):", answer_Q1andQ2/answer_Q1orQ2)