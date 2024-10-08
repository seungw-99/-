'''
# 관계연산자(비교연산자_
>, >=, <, <=, ==, !=
양옆을 비교한 결과를 참 또한 거짓으로 제공한다.

== : 서로 같은가?
!= : 서로 다른가?

a == b: a와 b가 같으면 True, 다르면 False
a != b: a와 b가 다르면 True, 같으면 False
'''
a = 10 > 5
b = 10 < 10
print('a=', a, type(a))
print('b=', b)
print()

# '==' 연산
print((10==10))
print('Rat' == 'rat')

# '!=' 연산자는 서로 값이 다르면 참
print(10 != 10)
print('Rat' != 'rat')
print()

#관계연산자는 파이썬에서 한줄에 여러개 사용 가능
print(30 > 20 > 10)
print(30 > 20 == 10)