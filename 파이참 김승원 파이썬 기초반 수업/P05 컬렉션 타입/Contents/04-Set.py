'''
# 집합(Set)
집합명 = {데이터, 데이터, 데이터..)
집합 특징: 데이터만 들어있음. 순서X, 중복X, 변경O
'''
a = {10, 15, 20, 15, 10}
b = {'winter', 'spring', 'fall', 'summer'}
c = set('apple')
print(a, type(a), len(a))
print(b)
print(c) # 랜덤x
print()

# 집합 데이터 추가, 삭제
s = {1,2,4}
s.add(3)
print(s)
s.update([6,7,8])
print(s)
s.remove(6)
print(s)
print()

# 집합 기능
a = {1,2,3,4}
b = {3,4,5,6}
print('교집합:', a & b)
print('합집합:', a | b)
print('차집합:', a - b)
print('대칭차집합:', a ^ b)
print('합집합-차집합:', (a|b) - (a&b))
print('부분집합:', {1,2} < a)
print()

# 비어 있는 집합 만들기
k = {} # 딕셔너리로 인식
print(k, type(k))

k = set() # 비어 있는 집합 생성
print(k, type(k))
k.add(10)
print(k)

