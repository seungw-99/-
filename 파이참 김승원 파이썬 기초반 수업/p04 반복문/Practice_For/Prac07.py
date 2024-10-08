'''
Q1) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성하시오.

↓ 실행화면 ↓
*
**
***
****
*****

Q2) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성하시오.

    *
   **
  ***
 ****
*****

i번째줄
빈칸: (5-i)개
별표: i개
'''
# Q1)
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()
print()

# 문자열*숫자
for i in range(1, 6):
    print('*'*i)
print()

# Q2)
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()
print()

# 문자열*숫자
for i in range(1,6):
    print(' '*(5-i)+'*'*i)