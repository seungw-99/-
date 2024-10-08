'''
# 튜플(tuple)
튜플명 = (데이터0, 데이터1, 데이터2..)
튜플 특징: 순서O, 중복O, 변경X
'''
a = (10, 20, 30, 20, 10)
b = (20, 30, 'Sun', 'day', 'Morning')
c = (30, True, ('Sun', 'day', 'Morning'))
print('a=', a, type(a), len(a))

# 튜플 인덱싱
print(a[3])
print(b[3])
print(c[-1])
print()

# 튜플 슬라이싱
print(a[1:4])
print(b[0:5:2]) #[시작값:끝값:증감값] 얼만큼씩 건너뛰면서 선택할지
print(b[::2])
print(b[::-1])
print(c[-1][::2])
print('='*20)
####################
d = (1,2,3)
e = (4,5,6)

# 튜플 연산
f = d+e
print('f=', f)
g = e*3
print('g=', g)

# 찾으려 하는 데이터의 인덱스 반환
print(g.index(5))
print(g.index(5, 2)) # 5값을 2번 인덱스 부터 탐색

# 찾으려 하는 데이터의 개수 세기
print(g.count(4))
