'''
Q)  사용자로부터 세 개의 숫자를 입력 받은 후
    가장 큰 숫자를 출력하라.

    ↓ 실행화면 ↓
    정수1 입력: 10
    정수2 입력: 9
    정수3 입력: 20
    가장 큰 수: 20
'''
num1 = int(input('정수1 입력: '))
num2 = int(input('정수2 입력: '))
num3 = int(input('정수3 입력: '))

#논리 연산자
if num1>=num2 and num1>=num3:
    print('가장 큰 수:', num1)
elif num2>=num3:
    print('가장 큰수:', num2)
else:
    print('가장 큰 수:', num3)

# 최대값을 저장할 변수 도입
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
print('가장 큰수:', max)

