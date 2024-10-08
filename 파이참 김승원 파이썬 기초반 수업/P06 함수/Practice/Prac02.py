'''
Q)  정수를 입력 받아 해당 정수의 약수를
    모두 출력하는 함수를 만들고 실행하시오.
    함수명: show_divisor
    매개변수: 정수형 1개
    리턴값: 없음

   ↓ 실행화면 ↓
   정수입력: 8
   1 2 4 8
'''
def show_divisior(n):
    for i in range(1, n+1):
        if n%i==0:
            print(i, end=' ')
n = int(input('정수 입력: '))
show_divisior(n)