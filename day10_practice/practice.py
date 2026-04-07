import numpy as np
import statistics as statistics
'''
a = [1, 2, 3]
b = [4, 5, 6]

print(np.add(a,b))
print(np.dot(a,b))
print(np.linalg.norm(a))
print(np.linalg.norm(b))

data = [1,2,2,3,4,100]
print(np.mean(data))
print(np.median(data))
print(statistics.mode(data))

np.random.seed(1000)
front = 0
def random_answer():
    return np.random.choice(["앞","뒤"]) 
for i in range(10000):
    a = random_answer()
    if a == "앞":
        front += 1
print(front/(i+1))

A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]
print(np.add(A,B))
print(np.dot(A,B))
print(A @ B) # 여기서 선행조건 A = np.array(A) 식의 넘파이 리스트로 바꿔야함

v = [1,5,2,6,10]
print(np.mean(v))
print(np.median(v))
#평균은 이상치(outlier)의 영향을 받지만
#중앙값은 데이터의 순서만 보기 때문에
#이상치의 영향을 덜 받는다.
'''
data = np.array([
    [170, 65],
    [180, 72],
    [175, 68],
    [160, 55],
    [165, 60]
])
print(np.mean(data,axis =0))
print(np.median(data,axis=0))
#print(data-[172, 70])
# 각 사람간 유클리드 거리를 계산해라
target = np.array([172,70])
dist = np.linalg.norm(data - target, axis=1)
print(dist)
print(np.argmin(dist))
# 현 데이터로 봤을때 평균수치와 차이가 큰 데이터가 들어와서 평균은 많이 오른다.
# 5개에서 6개로 되지만 중앙값 계산을 보았을때 3~4번째의 평균이니 큰 차이는 나지 않는다
#새로 들어오는 데이터가 이상치이기 때문이다.

print(np.arange(20).reshape(4,5))