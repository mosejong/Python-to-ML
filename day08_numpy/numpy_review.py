import numpy as np
###### 기초 문제 ########
'''
arr = np.arange(12).reshape(3,4)

print(arr[1])
print(arr[:,1:])
print(arr[arr % 2 == 0])

arr_1 = np.arange(1,6)
print(arr_1 + 10)
print(arr_1 * 3)

matrix = np.arange(8).reshape(2,4)

A = np.arange(3).reshape(3,1)
B = np.arange(3)
print(A+B)

arr = np.arange(1,17).reshape(4,4)
print(arr[:2,:2])
'''
#-----NumPy 실전 문제 세트 1-----#
'''
arr = np.arange(20).reshape(4,5)

print(arr[2])
print(arr[:,-1])
print(arr[1:3, 1:4])
print(arr[arr >10])
array = np.arange(2,11,2)
print(array+3)
print(array/2)
print(np.arange(12).reshape(3,4))
A = np.array[[1,2],
            [3,4]]

B = np.array[[5,6],
             [7,8]]

m = np.concatenate([A,B],0)
n = np.concatenate([A,B],1)
print(m)
print(n)

A = np.arange(1,4).reshape(3,1)
B = np.arange(10,31,10)
print(A+B)

arr = np.arange(1,13).reshape(3,4)
print(arr.sum())
print(arr.mean())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
'''
# ----- NumPy 훈련 문제 (진짜 실력 늘어나는 문제) ----- #
'''
arr = np.arange(1,26).reshape(5,5)

print(arr[1:4,1:4])
print(arr[arr%2==0])
print(arr.sum(0))
print(arr.mean(1))
print(arr.argmax())
'''
#-----NumPy 심화 연습 (오늘 범위)-----#
arr = np.arange(5)
arr_1 = np.arange(5).reshape(5,1)
print(arr+arr_1)

arr = np.arange(1,26).reshape(5,5)
i = np.arange(5)
print(arr[i,i])

arr = np.arange(1,13).reshape(3,4)
arr = np.sort(arr*-1,1)
print(arr*-1)
#print(arr[:, ::-1]) 가 원래정답@@@@@꼭 다시보기

arr = np.arange(10)
arr[arr % 2 == 0] = 0
print(arr)


arr = np.arange(1,5)
arr_1 = np.arange(1,5).reshape(4,1)
print(arr*arr_1)

arr = np.array([[3,1,2],
                [9,7,8],
                [6,4,5]])
print(np.sort(arr,1))

arr = np.arange(1,13).reshape(3,4)
print(arr[arr.sum(1) > 20])

print()
arr = np.arange(1,26).reshape(5,5)
arr_a = arr.copy()
arr_a[[0,1,3,4],:] = 0.
arr[:,[0,1,3,4]] = 0
arr[2,2]= 0
print(arr + arr_a)

