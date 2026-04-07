a = 10
b = 20
print(f'{a} + {b} = {a+b}')

numbers = [5, 7, 2, 9, 1, 10, 4, 6, 8, 3]
print(sorted(numbers)[-1])

text = "Python is fun!"
text_split = text.split(' ')
a = list(''.join(text_split))
a.reverse()
print(''.join(a))

def add_numbers(a,b):
    return a+b
print(add_numbers(1,2))

Copynumber = 5
if Copynumber % 2 == 0 :
    print("짝수")
elif Copynumber % 2 == 1:
    print("홀수")

for x in range(1,11) :
    if x % 2 == 1:
        print(x)

# 리스트는 수정이 자유롭지만 튜플은 수정은 간접적으로 할 수 있음
# 둘다 순서는 보장

Copysample_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
for x in Copysample_dict : 
    if Copysample_dict[x] == 30 :
        print(x)

list_a = []
for x in range(1,11):
    list_a.append(x*x)
print(list_a)

with open('day06\question.txt', 'w') as f:
    f.write('Hello, World!\nWelcom to Python.')

a = int(input('정수 입력  : '))
try :
    print(10/a)
except ZeroDivisionError :
    print('0으로 나눌 수 없습니다.')

numbers = [1, 2, 3, 4, 5]
a = list(map(lambda x : x*2,numbers))
print(a)

class Rectangle():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a * self.b

class Square(Rectangle):
    def area(self):
        return self.a * self.a

import re
Copytext = "Phone number: 010-1234-5678, age: 25"
list_c = []
p = re.compile('\d')
m = p.findall(Copytext)
list_c.append(m)
print(list_c)

numbers = [1, 2, 3, 4, 5, 3, 4, 2, 1, 6, 7, 8, 9, 10]
num = []
for i in numbers :
    if i not in num:
        num.append(i)
print(num)

txt = "Hello Python"
result = txt.swapcase()
print(result)

for x in range(1,101):
    if x % 3 == 0 and x % 5 != 0:
        print(x, end= ' ')
print()
def get_odd_numbers(a):
    b = []
    for x in a:
        if x % 2 == 1:
            b.append(x)
    print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_odd_numbers(a)
