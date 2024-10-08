'''
# while 반복문
while 문은 무한 반복 혹은 반복할 횟수가 정해져 있지 않았을 때 사용.

    while 조건식:
        반복문..
- 조건식이 참이면 반복문 계속 진행
- 조건식이 거짓이 되면 반복 중지
'''
# 1~3 반복 출력하기
num = 1
while num<=3:
    print(num)
    num+=1
print('='*10)

#== for문과 while문의 비교 ==#
# 0~4까지 5번 반복 출력
for i in range(0,5): # range(시작값, 끝값, 증감값)
    print(i)
print()


# while문~
i = 0 # 시작값
while i<5: # 끝값
    print(i)
    i+=1 # 증감값
print('='*10)

# 1~10 까지의 합 구하기
sum = 0
i = 1
while i!=11:
    sum += i
    i+=1
print('총합:', sum)

# 1~10 홀수만 한줄로 출력하기
i = 1
while i<=10:
    if i%2==1:
        print(i, end=' ')
    i+=1