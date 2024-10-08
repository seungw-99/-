'''
# while 무한루프 형태
조건식을 참으로 시작하여 반복문 무한 실행
무한반복을 멈추려면 조건문과 break 명령이 필요

    while True:
        반복문..
        if 조건식:
            break

# break
반복문 빠져나옴. 탈출(exit)
if문과 함께 사용

# continue
다음 반복으로 건너뜀
continue 다음 줄 부터의 실행문은 스킵
'''
# 1~5 반복출력
num = 1
while True:
    print(num)
    if num==5:
        break
    num+=1
print()

# 1~20 사이 짝수 출력하기
a = 1
while True:
    if a%2==0:
        print(a, end=' ')
    a+=1
    if a==21:
        break
print()
print('='*20)

#== 입력 받아서 whlie문 탈출하기 ==#
# 'Q'를 입력하면 무한반복 종료
while True:
    print('반복을 멈추려면 Q를 입력하세요')
    a = input('입력: ')
    if a == 'Q':
        break

# 숫자 -1을 입력하면 무한반복 종료
while True:
    num = int(input('숫자 입력(종료는 -1): '))
    if num==-1:
        print('프로그램을 종료합니다.')
        break
print('='*20)

# continue문
# 1~20 사이 5의 배수를 제외하고 출력
for i in range(1, 21):
    if i%5==0:
        continue
    print(i, end=' ')