import random
import time
import glob

# 라이브러리관련 문제집 해답
# filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
print(list(filter(lambda x: x>0,[1,-2,3,-5,8,-3])))

# map과 lambda를 사용해서 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어보자.
print(list(map(lambda x : x*3,[1,2,3,4])))

# glob모듈을 사용해서 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 만들어보자.
print(glob.glob("*.py"))

# time모듈을 사용해서 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
# 2018/04/03 17:20:32
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
import random

a = []

while len(a) < 6:
    r = random.randint(1,45)
    if r not in a :
        a.append(r)

print(a)


print(random.sample(range(1,46),6)) # 추가적인 공부하다 한줄로 표현할 수 있는 방법 찾음