'''
= : 대입연산자
오른쪽의 데이터를 왼쪽 변수에 저장한다.
'''
a = 10 #변수a에 정수10을 대입 (a<-10)
print(a)

b = 20
print(b)

b = a # a의 값을 b에 대입
print(b)
b = a + 100 #(a+100) 결과를 b에 대입
print(b)
a = b = 50 #50을 b에 대입한 후, b값을 a에 대입
print('a=', a)
print('b=', b)

c = 'summer'
print('c=', c)