'''
# 리스트(list)
리스트명 = [데이터0, 데이터1, 데이터2...]
데이터에 순서를 매겨 늘어놓은 자료 구조
리스트 특징: 순서o, 중복o, 변경o
'''
a = [10, 20, 30, 20, 10]
b = [20, 30, 'Sun', 'day', 'Morning']
c = [30, True, ['Sun', 'day', 'Morning']]
print('a=', a, type(a))

# 리스트 인덱싱
print(a[0])
print(a[2])
print(a[-2])
print(b[2]+b[3])
print(b[-1]*3)
print(c[2])
print(c[2][0]) # 이중 리스트 데이터 접근
print('='*20)

# 리스트 슬라이싱
print(a[1:3])
print(a[:2])
print(b[2:])
print(b[-3:])
print(c[1:2])
print(c[2][1:])
print('='*20)
#####################
d = [1,2,3,4,5]
e = [6,7,8]

# 리스트 연산
print(d+e)
print(d*2)

# 리스트 개수 구하기
print(len(d))
print(len(d+e))
print('='*20)
#####################
k =[1,2,4]

#== 리스트 데이터 추가, 수정, 삭제 ==#
## 추가
k.append(100) # 리스트 끝에 새로운 데이터 추가
print(k)
k.append('28일')
print(k)

k.insert(2, 3) # 해당 인덱스에 데이터 추가 (2, 3 하면 자동으로 인덱스와 오브젝트가 입력된다
print(k)
k.insert(-1, '8월')
print(k)
print()

## 수정
k[4] = 5 # 리스트 인덱스의 데이터 수정
print(k)
k[2:5] = [4,8,16]
print(k)
print()

## 삭제
del k[3] # 리스트 인덱스의 데이터 삭제
print(k)
del k[-2]
print(k)
del k[:3]
print(k)

k.remove(16) # 해당 데이터 삭제
print(k)
k.remove('28일')
print(k)
print('='*20)
#######################
# 비어 있는 리스트 만들기
k = []
print(k, type(k))
k.append(10)
print(k)

k = list()
print(k)
k.append(20)
print(k)
print('='*20)

#== 리스트 관련 함수==#
nums = [10, 30, 20, 5, 25]
foods = ['apple', 'cake', 'milk', 'bread']

# 찾으려는 데이터 인덱스 반환
print(nums.index(20))
print(foods.index('cake'))

# 오름차순 정렬
nums.sort()
print(nums)
foods.sort()
print(foods)

# 내림차순 정렬
nums.sort(reverse=True)
print(nums)

# 리스트 확장
nums.extend([0,-5, -10])
print(nums)
foods += [1,2]
print(foods)

# 역순으로 정렬
foods.reverse()
print(foods)
# foods.sort()

# 데이터 비우기
foods.clear()
print(foods)



