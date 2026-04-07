# 점프 투 파이썬 코딩면허시험 1번문제부터 복습하기.
'''
print('1번문제')
print('#'.join(('a:b:c:d').split(':')))

print('2번문제')
a = {'A': 90, 'B' : 80}
a['C'] = 70
print(a['C'])

print('3번문제')
print('List + List = 새로운 값인 List가 나오고 \nextend로 합친 리스트는 기존 List에 더하는 방식으로 차이가 있음')

print('4번문제')
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
B = list(filter(lambda x : x >= 50, A))
print(sum(B))

print('5번문제')
a = [0, 1]
num = int(input('정수 : '))
x = 0
while num >= a[x] + a[x+1]:
    a.append(a[x] + a[x+1])
    x += 1
print(a)

print('6번문제')
a = input('숫자 입력(단 ,로 구분지어 입력)').split(',')
sum = 0
for x in a:
    sum += int(x)
print(sum)

print('7번문제')
a = int(input('몇단?'))
for x in range(1,10):
    print(a*x, end= ' ')

'''

'''
print('8번 txt파일내용을 역순으로 저장')
with open('day05/abc.txt') as f :
    lines = f.readlines()

with open('day05/abc.txt', 'w') as f:
    for line in reversed(lines):
        f.write(line)
'''
'''
print('9번-txt파일에서 총합과 평균값 구해서 새파일저장')
with open('day05/sample.txt') as f:
    lines = f.readlines()
sum = 0
avg = 0
for x in lines :
    sum += int(x)
    avg = sum / len(lines)
with open('day05/result.txt', 'w') as f :
    f.write(f'sum : {sum}\navg : {avg}')
'''
print('10번 calculator 클래스 만들기')
'''
class Calculator:
    def __init__(self, list_a):
        self.list_a = list_a
    def sum(self):
        sum = 0
        for x in self.list_a :
            sum += x
        print(sum)
    def avg(self):
        sum = 0 
        avg = 0
        for x in self.list_a :
            sum += x
        avg = sum / len(self.list_a)
        print(avg)

cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])
cal1.sum()
cal1.avg()
cal2.sum()
cal2.avg()
'''
'''
print('11번문제')
1. cd C:\doit 이동 후 import mymod
2. from mymod import *
3. from mymod import 함수이름
4. sys.path.append("C:/doit") 후 import mymod

'''




print('12번 문제')
result = 0
try:
    [1,2,3][3]          #try 인덱스에러라서 +3위치로
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3         # 여기서 마지막인 finally로
finally:
    result += 4         # 여기서 종료

print(result)           # 답은 7