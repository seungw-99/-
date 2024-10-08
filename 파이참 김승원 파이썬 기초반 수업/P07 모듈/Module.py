'''
# 모듈 (module) - 파이썬 코드 파일
    import 모듈 이름

모듈은 변수나 함수 또는 클래스 등의 파이썬 코드를 작성해 놓은 파일이다.
모든 코드들을 암기해서 직접 만들어서 사용할 수 없기에,
많이 사용되거나 유용한 기능들을 미리 작성해둔 모듈을 가져와서 사용한다.

표준 모듈: 파이썬에 기본적으로 내장되어 있는 모듈
        math, random, datetime, time...
외부 모듈: 다른 사람들이 만들어서 배포한 모듈. 추가 다운.
        numpy, pandas, flask, beautifulsoup..
'''
# 1. math 모듈
import math
from random import random

print(math.pi)
print(math.e)
print(math.sin(3.14/2))
print(math.cos(3.14/2))
print(math.ceil(5.5)) # 올림
print(math.floor(5.5)) # 내림
print(round(5.5)) # 반올림 cf) 기본 제공 함수(print, len, sum..)
print(round(3.141592, 2))
print(abs(-10))

# 모듈 전부 가져오기
from math import *
print(pi)
print(cos(0))
print('='*30)

# 2. random 모듈
import random as rd # as 별칭
print(rd.random())
print(rd.uniform(1, 5)) # 랜덤 실수
print(rd.randrange(1,10, )) # 랜덤 정수(이상, 미만, 스텝)
print(rd.randint(1, 5)) # 랜덤 정수(이상, 이하)

# 로또 번호 생성1
lotto = []
for i in range(6):
    num = rd.randint(1, 45)
    while True: # 서로 겹치지 않게 번호 뽑기
        if num not in lotto:
            lotto.append(num)
            break
        num = rd.randint(1, 45)
lotto.sort()
print('로또번호:', lotto)

# 표본 추출하기
# 모집단 데이터들에서 k개 선택
print(rd.sample([1,2,3,4,5], 2))

# 로또 번호 생성2
# a = []
# for i in range(1, 46):
#     a.append(i)
a = [i for i in range(1, 46)] #if i%2==0]
lotto = rd.sample(a, 6)
lotto = rd.sample(range(1,46), 6)
lotto.sort()
print('로또 번호2:', lotto)
print('='*30)

# 3. datetime 모듈
import datetime as dt
print(dt.datetime.now())
now = dt.datetime.now()
print(f'{now.year}년 {now.month}월 {now.hour}일')
print('='*30)

# 4. time 모듈
import time as t
print(t.time())

start = t.time() # 시작 시간
# a = []
# for i in range(100000):
#     a.append(i)
a = [i for i in range(100000)]
end = t.time() # 종료 시간
runtime = end-start # 실제 실행 시간
print(f'실행시간: {runtime}초')

print('3초간 정지')
t.sleep(3)
print('후 실행합니다.')
