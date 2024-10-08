'''
Q1) 숫자 하나를 입력해서 팩토리얼 값을 구하라.

    예) 5를 입력하면
    5 * 4 * 3 * 2 * 1 결과를 계산해서 출력

    ↓ 실행화면 ↓
    팩토리얼 입력: 5
    5! = 120
'''
num = int(input('팩토리얼 입력: '))
fac = 1
for i in range(num, 0, -1): #range(1, num+1)
    fac *= i
print(f'{num}! = {fac}')
