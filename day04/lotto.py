import random
'''
print('1번 방법')               이방법은 6번진행해서 중복나오면 값이 6개가 아니라 5개 이하로도 나올 수 있음
num = []                        따라서 while 문으로 6개 나올때까지 진행하는게 맞음

for x in range(6) :
    x = random.randint(1,45)
    
    if x not in num :
        num.append(x)

print(sorted(num))
'''

print('1-2번 방법')
num = []

while len(num) < 6 :
    x = random.randint(1,45)

    if x not in num :
        num.append(x)

print(num)

print('2번 방법')

num = random.sample(range(1,46),6)

print(sorted(num))

print('문제 5세트 로또 생성')

for x in range(5) :
    num = sorted(random.sample(range(1,46),6))
    bonus = random.randint(1,45)
    while bonus in num :
        bonus = random.randint(1,45)
    print(f'{x+1}회차 : {num} + 보너스 {bonus}')