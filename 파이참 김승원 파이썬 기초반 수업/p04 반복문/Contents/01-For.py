'''
# for 반복문
for문은 코드 실행을 정해진 회수 만큼 반복할 때 사용한다.

# for문의 일반적인 형태
    for 반복변수 in 범위:
        반복문...
######################
# for문과 range()
    for i in range(a,b):
        반복문..
1. range(시작값,끝값)
2. a부터 b이전 까지 반복
3. i의 범위: a <= i < b
########################
    for i in range(b):
        반복문..
1. range(끝값)
2. i의 범위: 0 <= i < b
3. b번 반복
######################
    for i in range(a,b,n):
        반복문..
1. range(시작값, 끝값, 중간값)
2. a부터 b이전까지 n만큼 건너뛰며 반복
3. a,b,n은 정수만 가능
'''
# 0~4까지 5번 반복 출력
for i in range(0,5): # i <- (0,1,2,3,4)
    print(i)

# 1~10까지 자연수 출력
for i in range(1,11):
    print(i)

# 8~21 까지 수를 한줄로 출력
for j in range(8, 22):
    print(j, end=' ')
print() #한줄 안띄면 붙어서 출력됨
print('='*30)

#== range(b) ==#
# 0~4까지 5번 반복 출력
for i in range(5):
    print(i)

# '수요일' 3번 반복 출력
for i in range(3):
    print('수요일')
print('='*20) #구분선

#== range(a,b,n) ==#
# 1~10 범위에서 2씩 건너뛰면서 반복
for k in range(1, 10, 2):
    print(k)

# 1~40 사이 3의 배수만 한줄로 출력하기
for i in range(3, 40, 3):
    print(i, end=' ')
print()

# 10~1 범위에서 2씩 감소하면서 한줄로 출력
for i in range(10, 1, -2):
    print(i, end=' ')
print()

# '카운트다운' 5~1 까지 출력하기
for i in range(5, 0, -1):
    print('카운트다운', i)