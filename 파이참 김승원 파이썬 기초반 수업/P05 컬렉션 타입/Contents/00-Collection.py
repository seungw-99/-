'''
#== 컬렉션 타입 ==#
여러 개의 데이터를 저장하고 관리하는 자료형
리스트, 튜플, 딕셔너리, 집합

#== 컬렉션 타입과 반복분 ==#
    for 반복 변수 in 컬렉션 타입:
    실행문..

#== 컬렉션 타입에서 자료 찾기 ==#
    자료 in 컬렉션 타입
찾는 자료가 컬렉션 타입에 있는지? True/False

# iterable 객체
list, tuple, dict, set, range, str 등 반복 가능한 객체
'''
from multiprocessing.managers import ProcessLocalSet

listA = [10, 20, 30, 20, 10]
tupB = (10, 20, 30, 20, 10)
dictC = {'a':10, 'b':20, 'c':30}
setD = {10, 20, 30, 20, 10}

print('listA =', listA)
print('tupB =', tupB)
print('dictC =', dictC)
print('setD =', setD)

for data in listA:
    print(data)

for data in (5, 10, 15):
    print(data, end=' ')
print()

for key in dictC: # 딕셔너리는 key를 기본값으로 가져온다.
    print(key, dictC[key]) # key, value

for value in dictC.values(): # 딕셔너리 value만 전부 가져오기
    print(value)

for e in {'금', '토', '일'}:
    print(e)
print('='*20)

#== 반복문에서 리스트 활용하기 ==#
nums = [10, 20, 30, 40]

# 리스트 평균 구하기1
total = 0
for i in nums: # i <- [10, 20, 30, 40]: 리스트의 데이터
    total += i
print('리스트 평균:', total/len(nums))

# 리스트 평균 구하기2
total = 0
for i in range(len(nums)): # i <- (0,1,2,3) : 리스트의 인덱스
    total += nums[i]
print('리스트 평균:', total/len(nums))

# 파이썬 내장 함수
print('총합:', sum(nums))
print('평균:', sum(nums)/len(nums))
print('최대:', max(nums))
print('최소:', min(nums))
print('='*20)

#== 컬렉션 타입에서 자료 찾기 ==#
a = ['coke', 'banana']
b ={'num1':100, 'num2':20}
c = 'apple'
print('cake' in a)
print('pizza' in a)
print('pizza' not in a)
print(100 in b) # 딕셔너리는 key를 기본으로 탐색한다.
print(100 in b.values())
print('num2' in b)
print('e' in c)
print('ppl' in c)
print()

for i in 'fall':
    print(i)
