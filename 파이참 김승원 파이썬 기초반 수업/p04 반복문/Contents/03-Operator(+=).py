'''
# 복합 대입 연산자
+=, -=, *=, /=, %=, **=
사칙연산자 + 대입연산자
'''
from itertools import count

a = 100

a += 10 #a = a+10 을 줄여쓴 형태
print(a)

a -=10 #a = a - 10 을 줄여쓴 코드
print(a)

a *= 5
print(a)
a //= 50
print(a)
a %= 4
print(a)
a **= 3
print(a)
print()

# += 연산
num = 100
num += 10
num += 20
num += 30
print('num:', num)

# 1~10 까지의 수 더하기
sum = 0 #총합을 표현할 변수
for num in range(1, 11):
    sum += num
    print(num, '번쨰 sum =', sum)
print('총합:', sum)

# 1~10 까지 짝수들의 합 구하기
sum = 0
for i in range(1, 11):
    if i%2==0:
        sum += i
print('짝수합:', sum)

# 1~200 까지 13의 배수 개수 구하기
count = 0 # 개수를 셀 변수
for i in range(1, 201):
    if i%13==0:
        count+=1
print('13의 배수의 개수:', count)
