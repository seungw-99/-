'''
Q)   사용자로부터 4개의 요리 메뉴를 입력 받아서 리스트에 저장하고,
   무작위로 하나의 메뉴를 추첨하여 3초후 화면처럼 결과를 나타내시오.

   ↓ Console ↓
   메뉴: 김밥
   메뉴: 라면
   메뉴: 떡볶이
   메뉴: 짜장면
   추첨중입니다...
   추첨된 메뉴는 떡볶이 입니다.
'''
import random as rd
import time as t
# a = []
# for i in range(4):
#     a.append(input('메뉴: '))
a = [input('메뉴: ') for i in range(4)]
print('추첨중입니다...')
t.sleep(3)

# ans = a[rd.randint(0, 3)]
ans = rd.sample(a, 1) [0]
print(f'추첨된 메뉴는 {ans} 입니다.')
