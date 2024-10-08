'''
# 인덱싱과 슬라이싱
인덱싱(indexing): 특정 위치의 데이터를 추출한다. [3]
슬라이싱(slicing): 특정 범위의 데이터들을 추출한다. [2:5]

# [a:b]
[a이상:b미만]
a,b는 정수만 가능

happy = 'My weekend'
index : [0123456789]
'''
happy = 'My weekend'

# 문자열 인덱싱
print(happy[0])
print(happy[1])
print(happy[2]+happy[3])
print(happy[-1]) # 끝에서 첫번째 문자 추출
print()

# 문자열 슬라이싱
print(happy[0:2])
print(happy[:2]) # 처음 부터 2번 인덱스 전 까지
print(happy[3:7])
print(happy[3:-3])
print(happy[3:10])
print(happy[3:]) # 3번 인덱스 부터 끝 까지
print(happy[:]) # 전체 선택