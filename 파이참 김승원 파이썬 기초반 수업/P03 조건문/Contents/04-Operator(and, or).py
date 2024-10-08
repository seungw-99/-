'''
# 논리 연산자
and, or, not
조건식에 대한 결과를 참 또한 거짓으로 제공한다.

A and B : 양쪽 조건식이 둘 다 참인 경우 => 결과도 참
A or B : 둘 중 하나의 조건식이라도 참인 경우=> 결과도 참
not A : A의 논리값에 반대 결과 출력
'''
a = 50
b = 30
c = 10
print('and 예시1:', a>30 and b>10)
print('and 예시2:', a>30 and b>30)
print('or 예시1:', a>30 or b>30)
print('or 예시2:', a>50 or b>30)
print(a > b > c) #a>b and b>c
print('not 예시1:', not a>30)
print('not 예시2:', not a>b>c) #a<=b or b<=c
print()

# 조건문과 논리연산자 함께 사용하기
# if A and B
math = 70
science = 80
if mach>=80 and science>=80:
    print('컴공에 합격입니다')
else:
    print('컴공에 불합격입니다')

# if A or B
music = 70
art = 70
if music>= 90 or art>=90:
    print('예술대에 합격입니다')
else:
    print('예술대에 불합격입니다')
