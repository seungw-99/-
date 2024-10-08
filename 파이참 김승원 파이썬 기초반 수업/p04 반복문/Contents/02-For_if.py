'''
#반복문과 조건문 함께 사용
for i in range(a,b):
    if 조건식:
        반복문..

'''
# 짝수 출력하기
for i in range(1, 20):
    if i%2==0:
        print(i, end=' ')
print()

# 7의 배수 출력하기
for i in range(1, 100):
    if i%7==0:
        print(i, end=' ')
print()

# 월드컵 개최연도 출력하기
for cup in range(2002, 2023):
    if (cup-2002)%4==0: #cup%4==2
        print(cup)