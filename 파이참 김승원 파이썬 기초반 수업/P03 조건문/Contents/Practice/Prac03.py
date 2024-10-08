'''
Q)  사용자로부터 입력 받은 두 수의 합과 차를 구하여 출력하시오.
    단, 두 수의 차는 값이 양수가 나오도록 출력하시오.

    ↓ 실행화면 ↓
   정수 입력: 30
   정수 입력: 50
   두 수의 합은 80
   두 수의 차는 20
'''
num1 = int(input('정수 입력:'))
num2 = int(input('정수 입력:'))
print('두 수의 합은', num1+num2)

#if-else
if num1>=num2:
    print('두 수의 차는',num1-num2)
else:
    print('두 수의 차는', num2-num1)

# if 한번만 사용
sub = num1 - num2
if sub<0:
    # sub = num2=num1
    sub = -sub
print('두 수의 차는', sub)