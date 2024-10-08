'''
중첩 반복문
    for i in range(a,b): # 외부 for문
        실행문A
        for j in range(c,d): # 내부 for문
            실행문B
        실행문C

실행순서
    외부 for문에 진입하면
        실행문A를 먼저 수행하고,
        내부 for문에 진입하여 실행문B를 반복 수행하고,
        실행문C를 수행한 후
    다시 외부 for문 처음으로 돌아가서 전체 반복을 진행
'''
# 이중 for문
for i in range(1,5):
    for j in range(1,4):
        print(f'i = {i} | j = {j}')
print('='*20)

# 구구단 3단 출력하기
for j in range(1, 10):
    # print(3, 'x', i, '=', 3*i)
    print(f'{3} x {j} = {3*j}')
print('='*20)

# 구구단 출력하기1
for i in range(2,10): # 2~9단 범위
    print(f'{i}단')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
print('='*10)

'''
예제) 구구단 출력하기2 
2단: 2 4 6 8 10 12 14 16 18
3단: 3 6 9 12 15 18 21 24 27
4단: 4 8 12 16 20 24 28 32 36
5단: 5 10 15 20 25 30 35 40 45
6단: 6 12 18 24 30 36 42 48 54
7단: 7 14 21 28 35 42 49 56 63
8단: 8 16 24 32 40 48 56 64 72
9단: 9 18 27 36 45 54 63 72 81
'''
for i in range(2,10): # 2~9단 범위
    print(f'{i}단:', end=' ')
    for j in range(1, 10):
        print(i*j, end=' ')
    print()